import logging
import math
import uuid

import settings
import utils
from utils import app, sql


class Wim(app.Application):

    def __init__(self, input_file: str, out_file_path: str):
        super().__init__(input_file, out_file_path)

    def parse_excel(self, check_resource: bool):
        """
        WIM CATALOG
        group catalog by SKU,
        because in the data, each line is a video and not a product,
        one product can be found in many videos
        """
        # product_collection = sql.INSERT_COLLECTIONS
        # product_collections = []
        self._uuids.clear()
        self._products.clear()
        self._images.clear()
        self._videos.clear()
        video_dict = {}

        catalog = self._catalog.groupby('SKU')

        for _name, group in catalog:

            product_uuid = str(uuid.uuid4())
            self._uuids.append(product_uuid)

            product_item = group.reset_index(drop=True).iloc[0]

            category = product_item["Category"]
            title = product_item["Title"].replace("'", r"\'")
            price = product_item["Price"]
            sku = product_item["SKU"]
            brand = str(product_item["Brand"]).strip()

            if utils.is_none(price):
                logging.warning(f'{title} has no price!!!')
                continue

            if utils.is_none(category):
                logging.warning(f'{title} has no category!!!')
                continue

            category_uuid = utils.get_category(tbl='categories', value=category)
            brand_uuid = utils.get_category(tbl='brands', value=brand)
            shop_uuid = utils.get_category(tbl='shops', value=brand)

            styles = []
            properties = []

            for _idx, cols in group.iterrows():
                for style in str(cols["Style"]).split(","):
                    styles.append(str(style.split("-")[1]).strip())

                    styles = list(set(styles))

                for size in str(cols["Size"]).split(","):
                    if size in settings.SIZE_MAP:
                        size = settings.SIZE_MAP[size.strip().lower()]
                    property_ = {
                        "size": size,
                        "brand": brand,
                        "color": cols["Color"],
                        "price": math.ceil(float(cols["Price"])),
                        "condition": "new",
                        "salePrice": 0,
                        "sku": sku,
                        "styles": ", ".join(styles),
                        "availability": "in stock",
                        "salePriceEffectiveDate": None
                    }
                    if property_ not in properties:  # drop duplicates
                        properties.append(property_)

            for one_property in properties:
                one_property["variantId"] = str(uuid.uuid4())

            properties = list({frozenset(item.items()): item for item in properties}.values())
            properties_str = str(properties).replace("'", "\"").replace("None", "null")

            product_title = title.strip().replace("\n", "").replace("'s", "")
            product_description = product_item.get("Description", title).strip().replace("\n", "").replace("'s", "")

            self._products.append(sql.WIM_INSERT_PRODUCTS % (
                product_title,
                product_description,
                category_uuid,
                product_uuid,
                shop_uuid,
                brand_uuid,
                product_uuid,
                properties_str
            ))

            group['rank'] = group['Video #'].rank(method='max')
            # print(group)  # FIXME check group

            for _idx, cols in group.iterrows():
                video_name = utils.to_link_str(cols['Video #'])
                if utils.is_none(video_name):
                    continue
                video_name = utils.str_replace(video_name)
                image_name = utils.to_link_str(sku)

                product_video = '{}/Product_Videos/v2/{}master.m3u8'.format(settings.WIM_URL, video_name)
                product_cover = '{}/Product_Videos/v2/{}preview.jpg'.format(settings.WIM_URL, video_name)
                product_image = '{}/Product_Images/batch3/{}.jpg'.format(settings.WIM_URL, image_name)

                image = sql.INSERT_IMAGES
                self._images.append(image % (product_uuid, product_image))
                self._images = list(set(self._images))

                video_uuid = str(uuid.uuid4())
                if video_name in video_dict:
                    video_uuid = video_dict[video_name]
                else:
                    video_dict[video_name] = video_uuid

                if check_resource:
                    utils.check_remote_resource(product_video)
                    utils.check_remote_resource(product_cover)
                    utils.check_remote_resource(product_image)

                # ts = cols["Second Start"]
                # if len(str(ts)) == 1:
                #     ts = f"0{ts}"

                self._videos.append(
                    sql.INSERT_VIDEOS % (
                        product_uuid,
                        video_uuid,
                        int(cols['rank']),
                        product_video,
                        product_cover
                    )
                )

        #         for style in str(cols["Style"]).split(","):
        #             style = style.split("-")
        #
        #             if style[0] == 'nan':
        #                 continue
        #
        #             collection_uuid = None
        #             for category_ in settings.WIM_COLLECTION:
        #                 if category_["position"] == int(style[0].strip()):
        #                     collection_uuid = category_["id"]
        #                     break
        #
        #             product_collections.append(product_collection % (collection_uuid, product_uuid))
        #
        # product_collections = list(set(product_collections))

        self._build_migration()
