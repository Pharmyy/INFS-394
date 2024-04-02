#Ryan Hensley 3/21/24

import pandas as pd
import ssl
ssl._create_default_https_context = ssl._create_unverified_context
pd.set_option('display.max_columns', 7)
pd.set_option('display.width', 200)

tables = pd.read_html("https://en.wikipedia.org/wiki/Chicago" )

print("The number of tables: ", len(tables))

teams_df = tables[7]
print("The columns of the DataFrame are:", teams_df.columns)
print("The sports of the DataFrame are:", teams_df.Sport)

sport = input("please enter a Sport (e.g. Baseball, Football, " +
               "Basketball, Ice hockey, or Soccer) or 'end' ")

while   sport != "end":
    
    if sport.capitalize() in ["Baseball", "Football", "Basketball",
                  "Ice hockey", "Soccer"]:

        query_string =  "Sport == '" + sport + "'"
        print("The value of the query string  is: ",query_string)
        teams = teams_df.query(query_string)
        
        
        print(f"The Chicago teams in the {sport} are:")
        print(teams)
        
    else:
        print(f"There are no Chicago teams in the {sport} Sport:")
        
    sport = input("please enter a Sport (e.g. Baseball, Football, " +
               "Basketball, Ice hockey, or Soccer) or 'end' ")


