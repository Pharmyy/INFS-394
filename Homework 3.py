#Ryan Hensley 4/1/2023

<<<<<<< HEAD
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
=======
'''
Create a REST query that uses SoQL parameters to accomplish the following:

    return three specific columns
    limit the rows returned by applying criteria to two different columns (using the $where parameter). 

Print out some information from the data obtained
Save the data that results from your query in a JSON file.
'''

#imports
    import pandas as pd
    import requests as rest

#set endpoint
    endpoint = "https://data.lacity.org/resource/r4uk-afju.json?$query=SELECT%0A%20%20%60location_account%60%2C%0A%20%20%60business_name%60%2C%0A%20%20%60dba_name%60%2C%0A%20%20%60street_address%60%2C%0A%20%20%60city%60%2C%0A%20%20%60zip_code%60%2C%0A%20%20%60location_description%60%2C%0A%20%20%60mailing_address%60%2C%0A%20%20%60mailing_city%60%2C%0A%20%20%60mailing_zip_code%60%2C%0A%20%20%60naics%60%2C%0A%20%20%60primary_naics_description%60%2C%0A%20%20%60council_district%60%2C%0A%20%20%60location_start_date%60%2C%0A%20%20%60location_end_date%60%2C%0A%20%20%60location%60%2C%0A%20%20%60%3A%40computed_region_2dna_qi2s%60%2C%0A%20%20%60%3A%40computed_region_ur2y_g4cx%60%2C%0A%20%20%60%3A%40computed_region_tatf_ua23%60%2C%0A%20%20%60%3A%40computed_region_kqwf_mjcx%60%2C%0A%20%20%60%3A%40computed_region_k96s_3jcv%60%2C%0A%20%20%60%3A%40computed_region_qz3q_ghft%60"

#SoQL params
    
>>>>>>> 39e9008c3284cb3d7de1891150dbf0a1233fb4da
