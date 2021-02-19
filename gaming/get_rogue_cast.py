"""
Get arguments from Excel document for SQL statement
"""
import json
import os
import uuid
from typing import List, Tuple
# import numpy as np
# import pandas as pd

import settings
import sql
from db.pg import pg_cursor
from utils import represents_int, check_remote_resource, get_category, str_replace, is_none, to_link_str

cursor = pg_cursor()


def rogue_cast(product_rage: List[int], catalog, check_resource: bool) -> Tuple[list, list, list, List[str]]:
    """gaming catalog"""
    # fixme catalog = pd.read_excel(catalog_file)

    product_uuids = []
    products = []
    images = []
    videos = []

    # unique product for every row of document
    for _idx, cols in catalog.iterrows():
        item_id = cols['#']
        if cols['Ready for upload?'] != 'Yes':
            continue

        if item_id not in product_rage:
            continue
        print(item_id)  # check item number

        # columns to variables
        category = cols['Category']
        # TODO for mapping category from Excel to DB
        if category == 'VGA':
            category = 'GPU'
        elif category == 'PSU':
            category = 'Power Supply'
        elif category == 'Monitor':
            category = 'Monitors'
        elif category == 'Memory':
            category = 'Internal Memory Module'

        product_id = cols['Product Id (do not edit)']
        variant_id = cols['Variant Id (do not edit)']
        attributes = cols['Filtering attributes (From "Attribute sets" sheet)']
        description_list = [
            cols['Description text 1 (closer to beginning of the video)'],
            cols['Description text 2 (middle of the video)'],
            cols['Description text 3 (middle of the video)'],
            cols['Description text 4 (closer to end of the video)']
        ]
        full_attributes = cols['Full attributes']
        upc = cols['UPC']

        is_new = not is_none(product_id)
        # FIXME is_new = product_id is not np.nan and str(product_id) != 'nan'

        # availability from Excel
        availability = 'in stock'
        if cols['Stock'] == 0:
            availability = 'out of stock'
        # availability from PostgreSQL
        if is_new:
            cursor.execute(sql.PRODUCT_AVAILABILITY % str(product_id))
            availability_in_db = cursor.fetchall()
            if availability_in_db:
                availability = availability_in_db[0][0]
            else:
                availability = 'out of stock'

        prepared_attributes = {}
        if not is_none(attributes):
            for attr in attributes.split('\n'):
                values = attr.split(':')

                if values[0] is None:
                    continue
                if len(values[0].split(' ')) > 1:
                    key = values[0].title().replace(' ', '').replace(',', '')
                    key = key[0].lower() + key[1:]
                else:
                    key = values[0][0].lower() + values[0][1:]

                value = values[1].replace('\\xa0', '').strip()
                value = value.replace('\\xa0', '').replace('\u200e', '')

                if represents_int(value):
                    value = int(value)

                if len(values) == 1:
                    value += '; ' + values[0].strip()
                    continue

        # product price can be in several columns
        price = cols['New Rougecast Listing Price, $']

        if is_none(price):
        # FIXME if is_none(price) or str(price).replace('\\xa0', '').strip() == '':
            price = cols['Rougecast Listing Price, $']

        if price == 'EOL':
            product_delete = sql.GAMING_UPDATE_DELETED_AT
            products.append(product_delete % (str(product_id)))
            continue

        price = str(price).replace('\\xa0', '').strip()
        price = float(price)

        if is_none(variant_id):
            variant_id = str(variant_id).replace('\n', '').replace('\t', '').strip()
        else:
            variant_id = str(uuid.uuid4())

        descriptions = []

        for description in description_list:
            if not is_none(description):
            # FIXME if description is not np.nan and str(description) != 'nan':
                descriptions.append(str(description))

        specifications = None
        if not is_none(full_attributes):
        # FIXME if full_attributes is not np.nan and str(full_attributes) != 'nan':
            specifications = full_attributes

        image_links = []
        str_id = str(item_id)
        for _root, _dirs, files in os.walk('./gaming/static/' + str_id):
            for file in files:
                if ' ' in file:
                    continue
                if file == '.DS_Store':
                    continue
                product_image = f'{settings.GAMING_URL}/Product_Desc/{str_id}/{file}'
                if check_resource:
                    check_remote_resource(product_image, str_id)

                image_links.append(product_image)

        property_ = {
            "price": price,
            "variantId": variant_id,
            "manufacturer": cols['Manufacturer'],
            "orderLimit": None,
            "sku": cols['SKU'],
            "condition": "new",
            "salePrice": 0,
            "availability": availability,
            "salePriceEffectiveDate": None,
            "descriptions": descriptions,
            "specifications": specifications,
            "images": image_links,
        }
        if not is_none(upc):
            property_['upc'] = upc

        property_.update(prepared_attributes)
        properties = [property_]
        properties_str = json.dumps(properties)
        properties_str = str(properties_str).replace("'", "''")

        category_uuid = get_category(tbl='categories', value=category,)

        product_title = cols['Description'].strip().replace('\n', '')
        product_title = (product_title[:250] + '..') if len(product_title) > 250 else product_title

        # if a product ID exists, we update the product without inserting pictures and videos
        if is_new:
            product_update = sql.GAMING_UPDATE_PRODUCTS
            products.append(product_update % (properties_str, str(product_id)))
            continue

        # generate a transaction, check links for liveliness
        product_uuid = str(uuid.uuid4())
        product_uuids.append(product_uuid)
        product = sql.GAMING_INSERT_PRODUCTS

        products.append(product % (product_title, '', category_uuid, product_uuid, '', product_uuid, properties_str))

        file_name = to_link_str(cols['MFG'])
        file_name = str_replace(file_name)

        product_image = f'{settings.GAMING_URL}/Product_Images/2.0/{file_name}_medium.png'
        product_video = f'{settings.GAMING_URL}/Product_Videos/Video/{item_id}/master.m3u8'
        product_cover = f'{settings.GAMING_URL}/Product_Videos/Covers/{file_name}.jpg'

        if check_resource:
            check_remote_resource(product_image, str_id)
            check_remote_resource(product_video, str_id)
            check_remote_resource(product_cover, str_id)

        image = sql.INSERT_IMAGES
        images.append(image % (product_uuid, product_image))

        video_uuid = str(uuid.uuid4())
        video = sql.INSERT_VIDEOS
        videos.append(video % (product_uuid, video_uuid, 1, product_video, product_cover))

    return products, videos, images, product_uuids
