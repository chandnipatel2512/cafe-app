# Load txt file
def load_txt_data(filename):
    try:
        file = open(filename)
    except:
        print("This file does not exist, please enter a valid file name.")
    global list1
    list1 = file.readlines()
    file.close()
    list1 = list(map(str.strip, list1))
    return list1


# Save updated txt files
def save_txt_data(filename, list=[]):
    updated_items = "\n".join(str(x) for x in list)
    file = open(filename, "w+")
    file.write(updated_items)
    file.close()


# Open csv file
import csv


def load_csv_data(filename: str):
    with open(filename, mode="r") as csv_file:
        csv_read = csv.DictReader(csv_file)
        data = []
        for line in csv_read:
            data.append(line)
    return data
