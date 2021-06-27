class NewAge:

    def __init__(self,age):
        self.age = age

    def __int__(self,age):
        return age

    def age_foo(self,age):
        new_age = int(age) + 5
        return new_age
