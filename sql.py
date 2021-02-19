from settings import (
    OWNER_USER_ID,
    GAMING_SHOP_ID,
    GAMING_STORE_ID,
    WIM_STORE_ID,
)

INSERT_COLLECTIONS = "INSERT INTO product_collections (collection_id, product_id) VALUES ('%s', '%s');"
INSERT_IMAGES = "INSERT INTO product_images (product_id, position, image_uri) VALUES ('%s', 1, E'%s');"
INSERT_VIDEOS = "INSERT INTO product_videos (product_id, video_id, position, video_uri, cover_image_uri, start_time, video_title) VALUES ('%s', '%s', %i, '%s', E'%s', '00:00:00', 'Product Video');"
DELETE_ALL = """
DELETE FROM product_images WHERE product_id IN (%s);
DELETE FROM product_videos WHERE product_id IN (%s);
DELETE FROM products WHERE id IN (%s);"""
DELETE_COLLECTIONS = "DELETE FROM product_collections WHERE id IN (%s);"

# HIERARCHY
CATEGORY_BY_PARENT_ID = """
    SELECT id, name, description, parent_id, image_uri 
    FROM categories 
    WHERE parent_id = %s
      AND deleted_at IS NULL
    ORDER BY position
"""
DB_DICTIONARY = """
SELECT name, id 
FROM %s
"""
CATEGORY_BY_ID = """
    SELECT id, name, description, parent_id, image_uri 
    FROM categories 
    WHERE id = %s
      AND deleted_at IS NULL 
    ORDER BY position
"""
# + bugfix for item number 10 ( ID='f48bc9da-1370-4540-a0ff-75b1969881b4' )
PRODUCTS_PROPERTIES = """
    SELECT properties, category_id, id
    FROM products 
    WHERE deleted_at IS NULL
      AND properties IS NOT NULL 
      AND properties != '[{}]'
      AND category_id = %s
      AND id != 'f48bc9da-1370-4540-a0ff-75b1969881b4'
"""
PRODUCT_AVAILABILITY = """
SELECT property ->> 'availability' AS availability
FROM products CROSS JOIN jsonb_array_elements(properties) AS property
WHERE id = '%s'
"""
PIG_UPDATE_HIERARCHY = """
-- +pig Name: 005_new_hierarchy
-- +pig Requirements: 
-- +pig Up

UPDATE categories SET hierarchy = '%s' WHERE id = '%s';

-- +pig Down
"""
PIG_INSERT_ITEMS = """
-- +pig Name: 00__items
-- +pig Requirements:
-- +pig Up\n
"""

# GAMING
GAMING_UPDATE_DELETED_AT = f"UPDATE products SET deleted_at=now() WHERE id='%s' AND store_id='{GAMING_STORE_ID}';"
GAMING_UPDATE_PRODUCTS = f"UPDATE products SET properties='%s', updated_at=now() WHERE id='%s' AND store_id='{GAMING_STORE_ID}';"
GAMING_INSERT_PRODUCTS = f"INSERT INTO products (title, description, category_id, id, store_id, owner_user_id, shop_id, url, product_id, properties) VALUES (E'%s', E'%s', '%s', '%s', '{GAMING_STORE_ID}', '{OWNER_USER_ID}', '{GAMING_SHOP_ID}', E'%s', '%s', '%s');"

# WIM
WIM_INSERT_PRODUCTS = f"INSERT INTO products (title, description, category_id, id, store_id, owner_user_id, shop_id, brand_id, product_id, properties) VALUES (E'%s', E'%s', E'%s', E'%s', '{WIM_STORE_ID}', '{OWNER_USER_ID}', E'%s', E'%s', E'%s', E'%s');"
