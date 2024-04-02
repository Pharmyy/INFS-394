#Ryan Hensley 4/1/2023

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
    
