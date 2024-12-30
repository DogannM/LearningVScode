#Exercise 9: String Manipulation
#Write a Python program that:
#Takes a string input from the user.
#Prints the string in reverse order.
#Prints the number of characters in the string.
#Converts the string to uppercase and prints it.

#Prints the string in reverse order.
string = str(input("Write Something in your mind: "))[::-1]
print(string)
#Prints the number of characters in the string.
print(len(string))
#Converts the string to uppercase and prints it.
print(string.upper())