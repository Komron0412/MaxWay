from django.db import connection
from contextlib import closing


def dictfetchall(cursor):
    columns = [col[0] for col in cursor.description]
    return [
        dict(zip(columns, row)) for row in cursor.fetchall()
    ]


def dictfetchone(cursor):
    row = cursor.fetchone()
    if row is None:
        return False
    columns = [col[0] for col in cursor.description]
    return dict(zip(columns, row))


def get_categories():
    with closing(connection.cursor()) as cursor:
        cursor.execute("""SELECT id,title from food_menu_categories""")
        categories = dictfetchall(cursor)
        return categories


def get_orders():
    with closing(connection.cursor()) as cursor:
        cursor.execute("""Select * from food_menu_orders""")
        orders = dictfetchall(cursor)
        return orders


def get_products():
    with closing(connection.cursor()) as cursor:
        cursor.execute("""SELECT food_menu_products.id,food_menu_products.name,food_menu_products.description,food_menu_products.price,
                                 food_menu_products.image as image,food_menu_products.created ,food_menu_categories.title as category_title from food_menu_products
                       left join food_menu_categories on food_menu_products.category_id = food_menu_categories.id""")
        products = dictfetchall(cursor)
        return products


def get_users():
    with closing(connection.cursor()) as cursor:
        cursor.execute("""SELECT * from food_menu_users""")
        users = dictfetchall(cursor)
        return users

