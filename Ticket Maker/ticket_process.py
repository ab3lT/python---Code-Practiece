class client():
    def __init__(self, first_name, last_name, dest, age):
        self.first_name = first_name
        self.last_name = last_name
        self.dest = dest
        self.age = age

    def get_first_name(self):
        input("Please input your first name here: ")

    def get_last_name(self):
        input("Please input your last name here: ")

    def get_age(self):
        int(input("Please input your age here: "))

    def get_dest(self):
        input("Please input your destination here: ")
