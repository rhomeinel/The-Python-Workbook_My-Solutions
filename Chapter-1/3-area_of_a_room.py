#!/usr/bin/python3

# This program calculates the area of a room.

#from turtle import width


width = float(input("Enter the width of the room in meters: ")) 
length = float(input("Enter the length of the room in meters: "))
area = width * length
print(f"The area of the room is: {area} square meters")


#Other way to print the area:
#2print("The area of the room is: {area} square meters".format(area=area))
#print("The area of the room is: {0:.2f} square meters".format(area))
#print("The area of the room is: {} square meters".format(area))
#print("The area of the room is:",area,"square meters") 
