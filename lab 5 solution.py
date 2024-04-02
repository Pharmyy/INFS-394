# Ryan Hensley  03/14/24
import pandas as pd
trip_df = pd.read_json("trip_data.json")
trip_df = trip_df[['pickup_community_area', 'dropoff_community_area',
                   'fare', 'tips', 'tolls', 'extras', 'trip_total',
                   'payment_type']]
print("Before renaming columns, column names:\n ", trip_df.columns)
trip_df.rename(columns = {"pickup_community_area": "pickup_area",
          "dropoff_community_area": "dropoff_area"}, inplace = True)
print("After renaming columns, column names:\n ", trip_df.columns)
print("frequency of top 4 pickup areas: ")
print(trip_df.pickup_area.value_counts().head(4))

#Create a new column named ‘to_or_from_area_8’ with value 1 in rows 
# that have either pickup or dropoff area 8, and 0 otherwise.

trip_df["to_or_from_area_8"] = 0
trip_df.loc[(trip_df.pickup_area==8)|(trip_df.dropoff_area==8),"to_or_from_area_8"] = 1


print("frequency of to_or_from_area_8: ")
print(trip_df.to_or_from_area_8.value_counts())
#create dummy variables for payment_type in a new DataFrame.

payment_dummies = pd.get_dummies(trip_df.payment_type)

print(payment_dummies.head())
#Add Cash and Credit_Card dummy variables to trip_df DataFrame

trip_df["Cash"] = payment_dummies["Cash"]
trip_df["Credit_Card"] = payment_dummies["Credit Card"]

print(trip_df.head())
#reduce the DataFrame to include only cash or credit card payments.
trip_df = trip_df.query("Cash == 1 | Credit_Card == 1")


trip_df.to_json("Area8CashorCredit.json", orient = "records")

