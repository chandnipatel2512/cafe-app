# Load txt file
def load_data(filename):
    try:
        file = open(filename)
    except:
        print("This file does not exist, please enter a valid file name.")
    global list1
    list1 = file.readlines()
    file.close()
    list1 = list(map(str.strip,list1))