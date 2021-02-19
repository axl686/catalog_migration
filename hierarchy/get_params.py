import math

from db.pg import pg_cursor
from settings import BLACK_PARAMS, DISPLAY_NAMES
from db.sql import PRODUCTS_PROPERTIES

cursor = pg_cursor()


def get_params(category_id: str) -> dict:
    cursor.execute(PRODUCTS_PROPERTIES, (category_id, ))
    records = cursor.fetchall()

    categories = {}
    if len(records) == 0:
        return categories

    for row in records:
        # print(row)  # FIXME
        params = {}
        properties = row[0]
        category_id = row[1]
        product_id = row[2]
        # print('product_id: ', product_id, categories)  # FIXME
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
    for _, j in enumerate(categories[category_id]["params"]):
        is_string = False
        for i, p in enumerate(categories[category_id]["params"][j]):
            if isinstance(categories[category_id]["params"][j][i], str):
                categories[category_id]["params"][j][i] = (
                    categories[category_id]["params"][j][i].encode('ascii', 'ignore')).decode("utf-8")
            if not is_string:
                is_string = isinstance(categories[category_id]["params"][j][i], str)

            try:
                float(categories[category_id]["params"][j][i])
            except ValueError:
                continue
            categories[category_id]["params"][j][i] = float(categories[category_id]["params"][j][i])

        # если есть хотя бы одна строка, значит все будут строками
        if is_string:
            for i, p in enumerate(categories[category_id]["params"][j]):
                categories[category_id]["params"][j][i] = str(categories[category_id]["params"][j][i]).replace(".0", "")

    for i, j in enumerate(categories[category_id]["params"]):
        is_int = all(isinstance(x, int) for x in categories[category_id]["params"][j])
        is_float = all(isinstance(x, float) for x in categories[category_id]["params"][j])

        if is_int or is_float:
            min_v = math.floor(min(categories[category_id]["params"][j]))
            max_v = math.ceil(max(categories[category_id]["params"][j]))

            min_v = min_v - int(min_v / 10)
            max_v = max_v + int(max_v / 10)

            categories[category_id]["params"][j] = {
                "max": max_v,
                "min": min_v,
                "type": "RANGE",
                "displayName": DISPLAY_NAMES[j]
            }
        else:
            categories[category_id]["params"][j] = {
                "values": categories[category_id]["params"][j],
                "type": "CHECKBOX",
                "displayName": DISPLAY_NAMES[j]
            }

    order = []
    for i, j in enumerate(categories[category_id]["params"]):
        if j != 'price':
            order.append(j)

    order.sort()
    order = ["price"] + order

    ordered = {}
    for k in order:
        ordered[k] = categories[category_id]["params"][k]

    return ordered
