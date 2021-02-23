"""
Creation insert into DB transaction for new products and resources
"""
import sys

from gaming import RogueCast
from utils import str2bool
from wim import Wim

if __name__ == "__main__":
    products, videos, images, product_uuids = (None, None, None, None)
    name = sys.argv[1]
    catalog_file = sys.argv[2]
    output_sql_file = sys.argv[3]
    check_resource_bool = str2bool(sys.argv[4])

    if name == "gaming":
        range_start = int(sys.argv[5])
        range_end = int(sys.argv[6]) + 1
        rogue_vast = RogueCast(
            input_file=catalog_file,
            out_file_path=output_sql_file
        )
        rogue_vast.parse_excel(
            product_rage=list(range(range_start, range_end)),
            check_resource=check_resource_bool
        )

    elif name == "wim":
        wim = Wim(input_file=catalog_file, out_file_path=output_sql_file)
        wim.parse_excel(check_resource=check_resource_bool)
