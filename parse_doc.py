"""
Creation insert into DB transaction for new products and resources
"""
import sys

import pandas

from gaming.get_rogue_cast import rogue_cast
from utils import str2bool, build_migration
from wim.get_wim import wim

if __name__ == "__main__":
    products, videos, images, product_uuids = (None, None, None, None)
    name = sys.argv[1]
    # input_catalog = sys.argv[2]
    catalog_file = pandas.read_excel(sys.argv[2])
    output_sql_file = sys.argv[3]
    check_resource_bool = str2bool(sys.argv[4])

    if name == "gaming":
        range_start = int(sys.argv[5])
        range_end = int(sys.argv[6]) + 1
        products, videos, images, product_uuids = rogue_cast(
            product_rage=list(range(range_start, range_end)),
            catalog=catalog_file,
            check_resource=check_resource_bool,
            # output_file=output_sql_file,
        )

    elif name == "wim":
        products, videos, images, product_uuids = wim(
            catalog=catalog_file,
            check_resource=check_resource_bool,
            # output_file=output_sql_file,
        )

    build_migration(
        file=output_sql_file,
        products=products,
        videos=videos,
        images=images,
        uuids=product_uuids
    )
