# Number items in list:
def number_items(list):
    index = 1
    for item in list:
        print(index, item)
        index += 1
    return ""


# Create new item in list
def create(item="", list=[]):
    print(
        f"\nPlease provide the name of the {item} you would like to add to the menu, alternatively, please enter 0 to cancel."
    )
    new_item = input()
    return "" if new_item == "0" else list.append(new_item)


# Update item in list
def update(item="", list=[]):
    print(
        f"\nPlease provide the number of the {item} you would like to update, alternatively, please enter 0 to cancel."
    )
    z = int(input())
    if z == 0:
        return ""
    else:
        print(f"\nPlease provide the updated {item} name ")
        updated_item = input()
        list[z - 1] = updated_item


# Delete item in list
def delete(item="", list=[]):
    print(
        f"\nPlease provide the number of the {item} you would like to delete, alternatively, please enter 0 to cancel."
    )
    z = int(input())
    return "" if z == 0 else list.remove(list[z - 1])