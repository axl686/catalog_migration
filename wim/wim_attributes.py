# Мержим json файлы с каталогом вим, сохраняем недостающие варианты продукта

import csv
import uuid

import ijson
import pandas as pd

products = []


def parse_product(file_name, brand_name):
    f = open(file_name, 'r')
    objects = ijson.items(f, 'item')

    for o in objects:
        prices = []
        parameters = []

        for v in o["variants"]:
            prices.append(float(v["price"].replace(" USD", "")))

            if v["size"] == "" or v["color"] == "":
                continue

            sku = None
            if 'sku' in v:
                sku = v['sku']

            parameters.append({
                "color": v["color"], "size": v["size"], "link": v["link"],
                "brand": brand_name, "price": float(v["price"].replace(" USD", "")), "sku": sku,
                "variantId": str(uuid.uuid4())
            })
        prices = list(set(prices))

        products.append({
            "id": o['id'],
            "spu": o['spu'],
            "title": o['title'],
            "price": prices[0],
            "parameters": parameters
        })


parse_product('./wim/koandaily.json', "Koandaily")
parse_product('./wim/koandaily_02.json', "Koandaily")
parse_product('./wim/lilicloth.com.json', "Lilicloth")
parse_product('./wim/anniecloth_02.json', "Anniecloth")

with open('./wim/attributes.csv', 'w', newline='') as csvfile:
    writer = csv.writer(csvfile)
    writer.writerow(['id', 'spu', 'title', 'price', 'parameters'])
    for p in products:
        writer.writerow([p["id"], p["spu"], p["title"], p["price"], p["parameters"]])

catalog = pd.read_excel("./wim/products-wim-3.xlsx")
attributes = pd.read_csv("./wim/attributes.csv")

for idx, cols in catalog.iterrows():
    items = attributes[attributes["spu"] == cols["SPU"]]
    if len(items) > 0:
        catalog.loc[idx, "Price"] = str(items.iloc[0]["price"]).replace("USD", "").strip()
        catalog.loc[idx, "Variants"] = str(items.iloc[0]["parameters"])

catalog.to_excel("./wim/output-4.xlsx")
