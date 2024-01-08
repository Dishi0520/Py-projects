# adding str to int variable in print will convert int values to str. Ex. age = 21 then print("My age is" +str(age))  a.k.a type casting
# instead of age = 21 then age = age + 1, writ age = 21, age += 1 
# int data type cannot store dec. #'s, float data type can
# To find out data type of variable, write print(type(var name))
# boolean data type store only true or false. Used in if statements. 
# multiple assignment = allows us to assignmen multiple varibale at the same time in  one line of code. Ex. name, age, attractive = "Bro", "21". "True" 
# If multiple variable are same, ex. purple = 0 and red = 0, then write purple = red = 0
# string methods: name = "dishita"
#     print(len(name)): will print out lenght of the name ex. 7
#     print(name.find("d")): will print out which value contains that letter ex. 0 *First letter is 0. 
#     print(name.capitalize()): capitalize only first letter in name
#     print(name.upper()): capitalize all letters in string
#     print(name.lower()): lowercase all letters in string
#     print(name.isdigit()): Will tell if name is a digit or not. Returns a true or false statement. Doesn't mean if data type is int or str. Tells if str has numbers.
#     print(name.isalpha()): Returns true or false statement wheter or not string is only alphbetical letters. Spaces and other character will cause a false statement. 
#     print(name.count("i")): Tells how many times the letter in the parantheses is present in the string. ex. 2
#     print(name.replace("i", "y")): Replaces all letters in first quotation with the letter in the second quotes. Ex. dyshyta
#     print(name*3): Will print name 3 times. 

# type casting: conver the data type of a value to another data type
# Used when you need to print things. ex. print("X is" + x) wudn't work if x was a int, so you wud convert it to a str. by print("x is" + str(x))

# MATH FUNCTIONS

#import math for some reason
# round function, rounds arguement to the nearest whole number. Ex. pi = 3.14 print(round(pi)) = 3
# math.ceil function will round arguement up to the nearest whole number. Ex. pi=3.14 print(math.ceil(pi)) = 4
# math.floor will round round arguement down to the nearest whole number.
# print(abs(pi)) = absolute value of number
# print(pow(pi,2)) = raises argument to a power. In this ex. it raises pi (3.14) to the 2nd power. 1st comma = base, 2nd comma = power
# math.sqrt = gives square root of number
"""
EX.....
x = 1
y = 2
z = 3
print(max(x,y,z)) = gives max number out of all the variables given
print(min(x,y,z)) = gives min number out of all the variables given
"""
#hh
""""
STRING SLICING

"""