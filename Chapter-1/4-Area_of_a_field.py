#!/usr/bin/python3

from turtle import width

#Calculate area of field

#ask for user input
length = float(input("Enter length of field in feet: "))
width = float(input("Enter width of field in feet: "))

#Calculate area in square feet
area = length * width

#covert area from feet to acres
acres = area / 43560
print("The acre of the field is", acres, "acres")
