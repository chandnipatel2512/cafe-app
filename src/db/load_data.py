from src.db.core import connection, get_data, update
from src.functions.sql_functions import *


# Load data
product = sql_get("product")
courier = sql_get("courier")
order = sql_get("transaction")
basket = sql_get("basket")