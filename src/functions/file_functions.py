# Open csv file
import csv


def load_csv_data(filename):
    with open(filename, mode="r") as csv_file:
        csv_read = csv.DictReader(csv_file)
        data = []
        for line in csv_read:
            data.append(line)
    return data  #


def load_data():
    products = load_csv_data("./data/products.csv")
    couriers = load_csv_data("./data/couriers.csv")
    orders = load_csv_data("./data/orders.csv")
    return products, couriers, orders


# Save updated orders list to csv file
def save_csv_data(filename, orders=[]):
    with open(filename, "w", newline="") as output_file:
        fc = csv.DictWriter(
            output_file,
            fieldnames=orders[0].keys(),
        )
        fc.writeheader()
        fc.writerows(orders)


def save_data(products=[], couriers=[], orders=[]):
    save_csv_data("./data/products.csv", products),
    save_csv_data("./data/couriers.csv", couriers),
    save_csv_data("./data/orders.csv", orders)