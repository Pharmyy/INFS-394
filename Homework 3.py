#Ryan Hensley 4/1/2023

#imports
import pandas as pd
import requests

# Set pandas display options to widen the display
pd.set_option('display.max_columns', None)
pd.set_option('display.expand_frame_repr', False)

# Set endpoint
endpoint = "https://data.lacity.org/resource/r4uk-afju.json"

# SOQL params
# %25 is a wildcard matches any string containing 'Hardware', allowing non-direct matches
# Ensure future entries are covered by filtering out rows with blank NAICS numbers
# The IS NOT NULL condition guarantees that only records with non-null NAICS numbers are returned
params = {
    "$select": "business_name as BusinessName, zip_code as Zip, street_address as Address, primary_naics_description as TypeOfStore, naics as NAICS, city as City",
    "$where": "city='LOS ANGELES' AND naics IS NOT NULL AND primary_naics_description LIKE 'Hardware%'"
}

rest_results = requests.get(endpoint, params=params).json()

print("number of resulting records: ", len(rest_results))
results_df = pd.DataFrame.from_records(rest_results)

print("The results of the rest query:")
print(results_df)

# Save the data to a JSON file
results_df.to_json("hardware_stores_LA.json", orient="records")
