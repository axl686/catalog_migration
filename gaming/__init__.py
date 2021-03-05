import json
import os
import uuid
from typing import List

import settings
import utils
from utils import app, pg, sql


class RogueCast(app.Application):

    def __init__(self, input_file: str, out_file_path: str):
        super().__init__(input_file, out_file_path)

    def parse_excel(self, product_rage: List[int], check_resource: bool) -> None:
        """gaming catalog"""

        self._uuids.clear()
        self._products.clear()
        self._images.clear()
        self._videos.clear()

        for _idx, cols in self._catalog.iterrows():
            item_id = cols['#']
            if cols['Ready for upload?'] != 'Yes':
                continue

            if item_id not in product_rage:
                continue
            print(item_id)  # FIXME check item number

            # columns to variables
            category = cols['Category']
            if category in settings.CATEGORY_MAP:
                category = settings.CATEGORY_MAP[category]

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

            is_new = not utils.is_none(product_id)

            # availability from Excel
            availability = 'in stock'
            if cols['Stock'] == 0:
                availability = 'out of stock'
            # availability from PostgreSQL
            # if is_new:
            #     availability_in_db = pg.pg_execute(sql.PRODUCT_AVAILABILITY % str(product_id))
            #     if availability_in_db:
            #         availability = availability_in_db[0][0]
            #     else:
            #         availability = 'out of stock'

            prepared_attributes = {}
            if not utils.is_none(attributes):
                for attr in attributes.split('\n'):
                    values = attr.split(':')

                    if values[0] is None:
                        continue
                    # if len(values[0].split(' ')) > 1:
                    #     key = values[0].title().replace(' ', '').replace(',', '')
                    #     key = key[0].lower() + key[1:]
                    # else:
                    #     key = values[0][0].lower() + values[0][1:]

                    value = values[1].replace('\\xa0', '').strip()
                    value = value.replace('\\xa0', '').replace('\u200e', '')

                    if utils.represents_int(value):
                        value = int(value)

                    if len(values) == 1:
                        value += '; ' + values[0].strip()
                        continue

            # product price can be in several columns
            price = cols['New Rougecast Listing Price, $']

            if utils.is_none(price):
                price = cols['Rougecast Listing Price, $']

            if price == 'EOL':
                product_delete = sql.GAMING_UPDATE_DELETED_AT
                self._products.append(product_delete % (str(product_id)))
                continue

            price = str(price).replace('\\xa0', '').strip()
            price = float(price)

            if not utils.is_none(variant_id):
                variant_id = str(variant_id).replace('\n', '').replace('\t', '').strip()
            else:
                variant_id = str(uuid.uuid4())

            descriptions = []

            for description in description_list:
                if not utils.is_none(description):
                    descriptions.append(str(description))

            specifications = None
            if not utils.is_none(full_attributes):
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
                        utils.check_remote_resource(product_image, str_id)

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
            if not utils.is_none(upc):
                property_['upc'] = upc

            property_.update(prepared_attributes)
            properties = [property_]
            properties_str = json.dumps(properties)
            properties_str = str(properties_str).replace("'", "''")

            category_uuid = utils.get_data(tbl='categories', value=category, )

            product_title = cols['Description'].strip().replace('\n', '')
            product_title = (product_title[:250] + '..') if len(product_title) > 250 else product_title

            if is_new:
                product_update = sql.GAMING_UPDATE_PRODUCTS
                self._products.append(product_update % (properties_str, str(product_id)))
                continue

            product_uuid = str(uuid.uuid4())
            self._uuids.append(product_uuid)
            product = sql.GAMING_INSERT_PRODUCTS

            self._products.append(
                product % (product_title, '', category_uuid, product_uuid, '', product_uuid, properties_str))

            file_name = utils.to_link_str(cols['MFG'])
            file_name = utils.str_replace(file_name)

            product_image = f'{settings.GAMING_URL}/Product_Images/2.0/{file_name}_medium.png'
            product_video = f'{settings.GAMING_URL}/Product_Videos/Video/{item_id}/master.m3u8'
            product_cover = f'{settings.GAMING_URL}/Product_Videos/Covers/{file_name}.jpg'

            if check_resource:
                utils.check_remote_resource(product_image, str_id)
                utils.check_remote_resource(product_video, str_id)
                utils.check_remote_resource(product_cover, str_id)

            image = sql.INSERT_IMAGES
            self._images.append(image % (product_uuid, product_image))

            video_uuid = str(uuid.uuid4())
            video = sql.INSERT_VIDEOS
            self._videos.append(video % (product_uuid, video_uuid, 1, product_video, product_cover))

        # call parent class method _build_migration for write a file
        self._build_migration()
