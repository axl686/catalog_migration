"""Строим иерархию каталога из фильтров по существующим продуктам"""

import sys

from gaming.hierarchy import Hierarchy
from settings import GAMING_ID, WIM_ID
from utils.pg import pg_execute
from utils.sql import CATEGORY_BY_PARENT_ID, CATEGORY_BY_ID, PIG_UPDATE_HIERARCHY


def get_hierarchy(next_id: str or None, parent_id=None) -> list:
    if parent_id:
        categories = pg_execute(CATEGORY_BY_PARENT_ID, (parent_id,))
    else:
        categories = pg_execute(CATEGORY_BY_ID, (next_id,))

    children = []

    for row in categories:
        item = Hierarchy(cat_id=row[0], name=row[1], description=row[2], image_uri=row[4])
        item.get_params()

        if not item.children:
            item.children = get_hierarchy(next_id=None, parent_id=item.id)
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
    elif app_name == 'wim':
        app_id = WIM_ID

    h = get_hierarchy(app_id)
    hierarchy = h[0].to_json()

    with open(output_file, 'w') as file_handle:
        file_handle.write(PIG_UPDATE_HIERARCHY % (hierarchy, app_id))
