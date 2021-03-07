import json
import math

from settings import BLACK_PARAMS, DISPLAY_NAMES
from utils import pg, sql


class Hierarchy(object):
    def __init__(
            self,
            cat_id: str = None,
            name: str = None,
            description: str = None,
            image_uri: str = None
    ):
        self.id = cat_id
        self.name = name
        self.description = description
        self.filter = {}
        self.children = []
        self.imageUri = image_uri

    def to_json(self):
        return json.dumps(
            self,
            default=lambda o: o.__dict__,
            sort_keys=False,
            indent=4,
        )

    def get_params(self):
        records = pg.pg_execute(sql.PRODUCTS_PROPERTIES, (self.id,))

        categories = {}
        if len(records) == 0:
            return categories

        for row in records:
            params = {}
            properties = row[0]
            category_id = row[1]
            # product_id = row[2]
            # print('product_id: ', product_id, categories)  # FIXME check which product_id is incorrect
            if category_id in categories:
                params = categories[category_id]["params"]

            for param in properties:
                for _, j in enumerate(param):
                    if j in BLACK_PARAMS:
                        continue

                    if j in params:
                        if isinstance(param[j], list):
                            params[j] + param[j]
                        else:
                            params[j].append(param[j])
                        continue

                    if isinstance(param[j], list):
                        params[j] = param[j]
                    else:
                        params[j] = [param[j]]

            for _, j in enumerate(params):
                params[j] = list(set(params[j]))

            if category_id not in categories:
                categories[category_id] = {"params": {}}

            categories[category_id]["params"] = params

            # пробуем привести все к флоат чтобы далее вычислить range
        for _, j in enumerate(categories[self.id]["params"]):
            is_string = False
            for i, p in enumerate(categories[self.id]["params"][j]):
                if isinstance(categories[self.id]["params"][j][i], str):
                    categories[self.id]["params"][j][i] = (
                        categories[self.id]["params"][j][i].encode('ascii', 'ignore')).decode("utf-8")
                if not is_string:
                    is_string = isinstance(categories[self.id]["params"][j][i], str)

                try:
                    float(categories[self.id]["params"][j][i])
                except ValueError:
                    continue
                categories[self.id]["params"][j][i] = float(categories[self.id]["params"][j][i])

            # если есть хотя бы одна строка, значит все будут строками
            if is_string:
                for i, p in enumerate(categories[self.id]["params"][j]):
                    categories[self.id]["params"][j][i] = str(categories[self.id]["params"][j][i]).replace(".0", "")

        for i, j in enumerate(categories[self.id]["params"]):
            is_int = all(isinstance(x, int) for x in categories[self.id]["params"][j])
            is_float = all(isinstance(x, float) for x in categories[self.id]["params"][j])

            if is_int or is_float:
                min_v = math.floor(min(categories[self.id]["params"][j]))
                max_v = math.ceil(max(categories[self.id]["params"][j]))

                min_v = min_v - int(min_v / 10)
                max_v = max_v + int(max_v / 10)

                categories[self.id]["params"][j] = {
                    "max": max_v,
                    "min": min_v,
                    "type": "RANGE",
                    "displayName": DISPLAY_NAMES[j]
                }
            else:
                categories[self.id]["params"][j] = {
                    "values": categories[self.id]["params"][j],
                    "type": "CHECKBOX",
                    "displayName": DISPLAY_NAMES[j]
                }

        order = []
        for i, j in enumerate(categories[self.id]["params"]):
            if j != 'price':
                order.append(j)

        order.sort()
        order = ["price"] + order

        for k in order:
            self.filter[k] = categories[self.id]["params"][k]

    # def get_hierarchy(self, next_id: str or None, parent_id=None):
    #     if parent_id:
    #         cursor.execute(sql.CATEGORY_BY_PARENT_ID, (parent_id,))
    #     else:
    #         cursor.execute(sql.CATEGORY_BY_ID, (next_id,))
    #
    #     records = cursor.fetchall()
    #
    #     for row in records:
    #         item = Hierarchy(app_id=row[0], name=row[1], description=row[2], image_uri=row[4])
    #         print('category: ', item.name)  # category check
    #         if not item.children:
    #             item.get_hierarchy(next_id=None, parent_id=item.id)
    #             if len(item.children) == 0:
    #                 item.children = None
    #
    #         self.children.append(item)
