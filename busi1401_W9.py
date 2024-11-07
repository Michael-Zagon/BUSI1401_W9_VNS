#!/usr/bin/env python3

# Created by: Michael Zagon
# Created on: Nov 2024
# This file goes over Variables, Numbers and Strings for BUSI1401


'''
courseNum = 1401
CourseNum = 1402
print(courseNum)
print(CourseNum)
print(courseNum, CourseNum)
'''

'''
favouriteColor="blue"
age=19

print(favouriteColor)
print(age)
'''

# This program states the users name and age

# Input
user_name=input("What is your name?")
user_age=input("How old are you?")

# Output
print("Hello,", user_name,"! You are", user_age, "years old." )

'''
num=10
type(num)
num=10.0
int(6.3)
float(7)
'''

print("")

a=10
b=20
print("10 plus 20 is: ",a+b)
print("10 minus 20 is: ",a-b)
print("10 times 20 is: ",a*b)
print("10 to the power of 20 is: ",a**b)
print("10 divided by 20 is: ",a/b)

print("")


print("Hello, \nWorld!")
print("Hello, \tWorld!")
print("Hello, \\World!")
print("Hello, \'World!")
print("Hello, \"World!")


print("")

myName="michael zagon"
modified_name=myName.capitalize()
print(modified_name)
modified_name2=myName.upper()
print(modified_name2)

print("")

fname="john"
lname="smith"
fullNameex=fname+" "+lname
print(fullNameex)

print("")

# This program states the length of the users string

# Input
user_string=input("This program states the length of your sentence. Please enter your sentence: ")

# Process
strLength=len(user_string)

# Output
print("Amount of characters in your sentence:" ,strLength)


# Input
firstName=input("Input your first name:")
lastName=input("Input your last name:")
# Process
initials = (firstName[0] +"&"+ lastName[0])
# Output
print("Your initials are:" ,initials)

print("\nDone")