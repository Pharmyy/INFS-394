# Lab 2 solution Ryan Hensley 2/8/2024

from Largest_USA_Cities import cities_dict

#Add code in print statement to print out number of entries in dictionary
print("The number of entries in the Cities dictionary is: ", len(cities_dict)  )

city = input("please enter a city name and state code (e.g. Chicago, IL): ")

#Add code to see if city entered is one of the largest cities
if city in cities_dict:

    print("That city is one of the largest cities in the United States!")
    response = input("Do you want to know that cities' population (Yes/No)? ")

    #Add code to check if "Yes" was entered
    if response.capitalize() == "Yes":
        #Add code in print statement to print out population of city
        print("The population of ",city, " in 2020 was: ", cities_dict[city] )

    #Add code to create if "No" was entered
    elif response.capitalize() == "No":
        print("You replied 'No' - you can always check back later")


    else:
        print("You did not enter yes or no!")
   #Add code to print message if city entered is not one of largest cities
else:
        print(city,"is not one of the largest in the US")




print("\nHave a great day!") 


