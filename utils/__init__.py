import logging
import sys

import requests
from numpy import nan

from utils.pg import pg_execute
from utils.sql import DB_DICTIONARY, DELETE_ALL, PIG_INSERT_ITEMS


def represents_int(s) -> bool:
    try:
        int(s)
        return True
    except ValueError:
        return False


def str2bool(s):
    return s.lower() in ("True", "true", "t", "1", "yes")


def check_remote_resource(url: str, item_id: str = None) -> None:
    response = requests.head(url)
    if not response.ok:
        print(f"Bad url for {item_id}:", url)


def is_none(_key):
    return (
            _key is nan
            or _key is None
            or str(_key) == "nan"
            or str(_key).replace('\\xa0', '').strip() == ''
    )


def get_category(tbl: str, value: str) -> str:
    _uuid = None
    rows = pg_execute(DB_DICTIONARY % tbl)

    for row_in_db in rows:
        if row_in_db[0].lower() in value.strip().lower():
            _uuid = row_in_db[1]
            break
    if not _uuid:
        logging.warning(f"{value} not found in {tbl}")
        return sys.exit(100)
    else:
        return _uuid


def str_replace(some_string: str) -> str:
    """ replacement for specific products. naming left somewhere"""
    some_string = some_string.replace("CG03_Vision_", "CG03_Vision")
    some_string = some_string.replace("GM-4.5.6.12_In_N_Out", "GM-4_5_6_12_In_N_Out")
    some_string = some_string.replace("GM-1.2.3_Gonna_Celebrate", "GM-1")
    some_string = some_string.replace("GM-3.9_Unconditional_Future", "GM-3")
    some_string = some_string.replace("AM01_CaliforniaTropic.", "AM01_CaliforniaTropic")
    some_string = some_string.replace("GM-6.7_California_Tropics", "GM-6")
    some_string = some_string.replace("HG05_", "HG05")
    some_string = some_string.replace("MCB-NR200-WNNN-S00", "CM_NR200")
    some_string = some_string.replace("110-BQ-0700-V1", "EVGA_700_BQ")
    some_string = some_string.replace("100-100000031BOX", "08736fda-f96e-4452-bdbb-238665129a23")
    some_string = some_string.replace("BX8070110850K", "Intel_I9_10850K")
    some_string = some_string.replace("CA-H510B-B1", "NZXT_H510")
    some_string = some_string.replace("08736fda-f96e-4452-bdbb-238665129a23", "98e417c6-ec68-4c77-9e05-1c9e0a6e3443")
    return some_string


def build_migration(
        file,
        products: list,
        videos: list,
        images: list,
        uuids: list
) -> None:
    delete_all = DELETE_ALL % (uuids, uuids, uuids)

    with open(file, 'w') as file_handle:
        file_handle.write(PIG_INSERT_ITEMS)
        for list_item in products:
            file_handle.write('%s\n' % list_item)
        file_handle.write('\n')
        for list_item in videos:
            file_handle.write('%s\n' % list_item)
        file_handle.write('\n')
        for list_item in images:
            file_handle.write('%s\n' % list_item)
        file_handle.write('\n\n')
        file_handle.write('-- +pig Down\n')
        file_handle.write('%s\n' % delete_all.replace("[", "").replace("]", ""))


def to_link_str(s: str) -> str:
    return (
        str(s)
        .strip()
        .replace(' ', '_')
        .replace("'", r"\'")
        .replace('/', '_')
    )
