# Program Description: This program manages a inventory list for a robotics team.
#It allows the user to add items to the list, remove items from the list, and check if a specific item is on the list.
#In theory this would allow for connection to an inventory database

# Author: Ryan Hesnley
# Date: February 15, 2024

'''
Requirements

    Comments with a detailed description of what the program is designed to do in a comment at the beginning of your program. 
    Comments to explain what is happening at each step as well as one in the beginning of your code that has your name and the date the code was created and/or last modified.
    The use of at least one compound data type (a list, a tuple, or a dictionary) that has at least 10 elements.
    Use of at least one method with your compound data type.
    Use of at least one Python built-in function with your compound data type.
    An if statement with at least two elif statements and an else statement.
    A nested if statement.
    At least one value input by the user during the program execution.
    At least one result reported to the user, that varies based on the value(s) that they input and values in your compound data type(s).

'''

# Define a robotics list using a dictionary with items as keys and their quantities as values
robotics_list = {"10/24 bolts": 5, "75t Belts": 3, "Omni Wheels": 2, "775 motors": 1, "10/20 Metal": 6, "Stealth Wheels": 1, \
                 "Kraken Motors": 2, "Falcon Motors": 4, "Squish Wheels": 3, "Colson Wheels": 2}

# Main program
##Title
print("Robotics Inventory list manager")

#While the following is true run loop and give options to end-user
while True:
    print("Options:")
    print("1. Add item to the list")
    print("2. Remove item from the list")
    print("3. Check if item is on the list")
    print("4. View all items")
    print("5. Exit")
    option = input("Choose an option: ")

#if end-user enters 1 then ask for item to add and then quantity of that item
    if option == '1':
        item = input("Enter the item to add: ")
        #try the code if the string input can be converted to an integer 
        try:
            quantity = int(input("Enter the quantity: "))
        #if the item is already in the list then add quantity
            if item in robotics_list:
                robotics_list[item] += quantity
        #else the item equals quantity input
            else:
                robotics_list[item] = quantity
            print(item+" added to the list.")
        #if a ValueError is thrown as a result of the quantity input string being unable to be converted to an intger then have user select another option 
        except ValueError:
            print("Invalid quantity input. Enter a valid integer.")
        
#if end-user enters 2 then ask for item to remove and then quantity of that item
    elif option == '2':
        item = input("Enter the item to remove: ")
        quantity = int(input("Enter the quantity to remove: "))
    #if the item is in the list and if the item is less or equal than the quantity than delete the item from the list
        if item in robotics_list:
            if robotics_list[item] <= quantity:
                del robotics_list[item]
    #else remove the quantity entered
            else:
                robotics_list[item] -= quantity
            print(item+ " removed from the list.")
    #else if the item is not in the list print out that the item is not found in the robotics list
        else:
            print(item+ " not found in the robotics list.")

#if end-user enters 3 then ask for item to check
    elif option == '3':
        item = input("Enter the item to check: ")
    #if the end user inputs an item and it is on the list then return the item name is on the list
        if item in robotics_list:
            print(item + " is on the robotics list.")
    #if the end user inputs an item not on the list then return the item name is on the list
        else:
            print(item + " is not on the robotics list.")
            
#if end-user enters 4 and the dictonary has 0 items in it then report back the robotics list is empty        
    elif option == '4':
        if len(robotics_list) == 0:
            print("The robotics list is empty.")
        #else print out the Robotics list, attaching the quantity to each of the items, and then printing out the item + the quantity
        else:
            print("Robotics List:")
            for item, quantity in robotics_list.items():
                print(item + ": " + str(quantity))
                
#If the end-user enters 5 then print out Robotics List Exited
    elif option == '5':
        print("Robotics List Exited")
        break

#Else print out Invalid option. Please Choose an option again.
    else:
        print("Invalid option. Please choose an option again.")

