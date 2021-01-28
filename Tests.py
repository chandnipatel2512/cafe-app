from File_Functions import load_txt_data, save_txt_data, load_csv_data
from List_Functions import number_items, create, update, delete, new_order

# Load products and couriers data
products = load_txt_data("Products.txt")
couriers = load_txt_data("Couriers.txt")
orders = load_csv_data("Orders.csv")
print(orders, type(orders))

new_order(couriers)
print(orders)