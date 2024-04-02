#Lab 1 solution Ryan Hensley 2/1/2024
new_list = [180, "Hello", True, 125.5, [180, False]]

print("The original list is: ", new_list)
print("Enter value to add to list within the list: ")
new_value = input()
#Add line of code to insert new_value as 2nd value in list within list
#new_list = [180,"Hello",True,125.5,[180,new_value,False]]
new_list[4].insert(1,new_value)
print("After adding new value, the list is now: ", new_list)

#Add code in print statement to print out slice of list
print("The 2nd-4th items in the list are: ",  new_list[1:4])


text_entered = input("Please enter some text: ")
#Add code to create list of words in text_entered 
word_list = text_entered.split()
#Add code in print statement to print out number of words in list
print("There are ",   len(word_list)         ," words in the text")

print("The words in the text you entered are: ", word_list)


