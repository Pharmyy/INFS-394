#lab 7 solution Ryan Hensley 3/28/2024

import pandas as pd
import requests

endpoint = "https://data.cityofchicago.org/resource/tfm3-3j95.json"

# Add SoQL parameters to obtain
#    a list of companies with active licenses

#    and the number of active licenses each has.

#    Only have companies with at least 30 active licenses

#    and sort in descending order of the number of licenses.

rest_results = requests.get(endpoint + "?" +
            "$select=company_name,count(company_name) as Active_Vehicle_Count"+
            "&$where=status='ACTIVE'" +
            "&$group=company_name" +
            "&$having=Active_Vehicle_Count>30" +
            "&$order=Active_Vehicle_Count desc").json()


print("number of resulting records: ", len(rest_results))
results_df = pd.DataFrame.from_records(rest_results)

print("The results of the rest query:")
print(results_df)


