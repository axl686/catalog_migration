import pandas
import requests

from sql import DELETE_ALL, PIG_INSERT_ITEMS


class Application:

    def __init__(self, products: list, videos: list, images: list, product_uuids: list, name: str, catalog: str):
        self.name = name
        self.catalog = catalog
        self.uuids = product_uuids
        self.products = products
        self.images = images
        self.videos = videos

    def build_migration(self, output_file) -> None:
        """Write SQL migration to file"""
        delete_all = DELETE_ALL % (self.uuids, self.uuids, self.uuids)
        with open(output_file, 'w') as file_handle:
            file_handle.write(PIG_INSERT_ITEMS)
            for list_item in self.products:
                file_handle.write('%s\n' % list_item)
            file_handle.write('\n')
            for list_item in self.videos:
                file_handle.write('%s\n' % list_item)
            file_handle.write('\n')
            for list_item in self.images:
                file_handle.write('%s\n' % list_item)
            file_handle.write('\n\n-- +pig Down\n')
            file_handle.write(
                '%s\n' % delete_all.replace("[", "").replace("]", ""))

    def catalog(self, input_file) -> None:
        """Excel file to pandas"""
        self.catalog = pandas.read_excel(input_file)


class RogueCast(Application):

    catalog = r'/Users/AlekseiMalinovsky/Downloads/RogueCast\ Catalogue.xlsx'

    def __init__(self):
        super().__init__(self.products, self.videos, self.images, self.uuids, self.name, self.catalog)









RC_CATALOG_URL = 'https://perfectartco-my.sharepoint.com/:x:/g/personal/sergey_bakulin_perfectart_com/EYlnqr9boyBLn7KNK5SBdM0Br7srtA-vkUAdUhkQt3cOhA'
headers = {'Accept': 'application/json;odata=verbose'}
guid = 'EYlnqr9boyBLn7KNK5SBdM0Br7srtA-vkUAdUhkQt3cOhA'
r = requests.get(RC_CATALOG_URL, headers=headers)

rc = "https://perfectartco-my.sharepoint.com/_api/web/lists/GetByTitle('RogueCast Catalogue')/Items(4)"

r = requests.post(
"https://intranet-uat-gb.mysp2016.com/clients/_api/Web/Lists/GetByTitle('RogueCast Catalogue')/Items(4)",
verify=False,
auth=auth,
data={
'__metadata': {
'type': 'SP.Data.TestlistListItem'
},
"Title": "Something better",
}),
headers={
'X-RequestDigest': form_digest,
'content-type': "application/json;odata=verbose",
'Accept': "application/json",
"X-HTTP-Method": "MERGE",
"IF-MATCH": etag,
},

