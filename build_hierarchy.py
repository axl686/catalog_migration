"""Строим иерархию каталога из фильтров по существующим продуктам"""

import sys

from db.pg import pg_cursor
from hierarchy.get_params import get_params
from hierarchy.hierarchy import Hierarchy
from settings import GAMING_ID, WIM_ID
from sql import CATEGORY_BY_PARENT_ID, CATEGORY_BY_ID, PIG_UPDATE_HIERARCHY

cursor = pg_cursor()


def get_hierarchy(next_id: str or None, parent_id=None) -> list:
    if parent_id:
        cursor.execute(CATEGORY_BY_PARENT_ID, (parent_id,))
    else:
        cursor.execute(CATEGORY_BY_ID, (next_id,))

    records = cursor.fetchall()

    children = []
    for row in records:
        print('category: ', row[1])  # category check
        item = Hierarchy(app_id=row[0], name=row[1], description=row[2], image_uri=row[4])
        item.filter = get_params(category_id=row[0])

        if not item.children:
            item.children = get_hierarchy(next_id=None, parent_id=row[0])
            if len(item.children) == 0:
                item.children = None

        children.append(item),

    return children


if __name__ == "__main__":
    app_name = sys.argv[1]
    output_file = sys.argv[2]

    app_id = ''
    if app_name == 'gaming':
        app_id = GAMING_ID
    if app_name == 'wim':
        app_id = WIM_ID

    h = get_hierarchy(app_id)
    hierarchy = h[0].to_json()

    with open(output_file, 'w') as file_handle:
        file_handle.write(PIG_UPDATE_HIERARCHY % (hierarchy, app_id))
