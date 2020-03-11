import calendar
import pandas as pd
print("Hello there, Wellcome to my Python demo of Basic python concepts")
print("Here is a bignum")
bignun1 = 182841384165841685416854134135
bigunm2 = 135481653441354138548413384135
print(bignun1 - bigunm2)
print()
print("Next i'll show you how easy it is to convert a int to a string")
the_big_num = bignun1 - bigunm2
print(f"the_big_num var is : {the_big_num} and is a {type(the_big_num)}")
print("Now if i use the str() function")
the_big_num = str(the_big_num)
print(f"the_big_num var is : {the_big_num} and is a {type(the_big_num)}")
print()
# now if i want to import a module i can do this
print("Here is all the attributes of pandas")
print(dir(pd))
print()
print("This is a list")
demolst = 1, 2, 1, 3, 2, 4, 5, 6
print(demolst)
print()
print(f"Here is a slice of that list: {demolst[2:5]}")
print()
print("Here is a tuple")
demo_tuple = 4, 6.9, "fish"
print(demo_tuple)
print()
print("here is a lst comprehension")
x = [i for i in range(10)]
print(x)
print()
print("Here is a python dict")
demo_dict = {
    "brand": "Ford",
    "model": "Mustang",
    "year": 1964
}
print(demo_dict)
print()
print("here is a simple function")


def demo_function(number_to_increment):
    """Give Me a single number and i will increment it by 1"""
    print("number has been incremented by 1")
    result = number_to_increment + 1
    return result


def is_prime_number(x):
    if x >= 2:
        for y in range(2,x):
            if not ( x % y ):
                return False
    else:
        return False
    return True


def is_it_prime(input_number):
    result = is_prime_number(input_number)
    return print(f"prime num is: {result}")


print(help(demo_function))
print()
demo_number = 1
print(f"the demo number will first be = to {demo_number}")
demo_number = demo_function(demo_number)
print(
    f"the demo number is now {demo_number} after i have applyed it to the function")
demo_number = demo_function(demo_number)
print(f"if i apply it again it is now {demo_number}")
print()
print("Now I will give you a basic calender")
c = calendar.TextCalendar(calendar.MONDAY)
demo_calendar = c.formatmonth(2020, 3)
print(demo_calendar)