from src.db.core import connection, get_data, update
from src.functions.list_functions import *
from src.functions.operational_functions import *
from src.functions.sql_functions import *
from src.menu_functions import *
import uuid

# Load data
product = sql_get("product")
courier = sql_get("courier")
order = sql_get("transaction")
basket = sql_get("basket")

# Run app
main_menu()
