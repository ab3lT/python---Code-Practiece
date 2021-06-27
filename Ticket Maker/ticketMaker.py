
first_name = ""
last_name = ""
age = ""
dest = ""


def data_retrieve():
    global first_name
    first_name = input("Enter first name here: ")
    global last_name
    last_name = input("Enter your last name here: ")
    global age
    age = input("Enter your last age here: ")
    global dest
    dest = input("Enter your destination here: ")


def data_process():
    print("Name: "+first_name[0] + '. ' + last_name+"," + age)
    print("Destination: ", dest)


def ticket_print():
    data_retrieve()
    data_process()


ticket_print()
