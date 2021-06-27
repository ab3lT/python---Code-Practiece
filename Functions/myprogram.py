def age_foo(input_age):
    new_age = int(input_age) + 50
    return new_age


age = input("Enter your age : ")
new_age = age_foo(age)
AGE = str(new_age)
print("You will be " + AGE + " years old in 2068G.C.")
