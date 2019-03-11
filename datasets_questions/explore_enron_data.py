#!/usr/bin/python

""" 
    Starter code for exploring the Enron dataset (emails + finances);
    loads up the dataset (pickled dict of dicts).

    The dataset has the form:
    enron_data["LASTNAME FIRSTNAME MIDDLEINITIAL"] = { features_dict }

    {features_dict} is a dictionary of features associated with that person.
    You should explore features_dict as part of the mini-project,
    but here's an example to get you started:

    enron_data["SKILLING JEFFREY K"]["bonus"] = 5600000
    
"""

import sys
import pickle
import pandas as pd
import numpy
sys.path.append("../final_project/")
from poi_email_addresses import poiEmails


enron_data = pickle.load(open("../final_project/final_project_dataset.pkl", "rb"))

x = enron_data["ALLEN PHILLIP K"]
y = poiEmails()

jp = enron_data["PRENTICE JAMES"]["total_stock_value"]

wc = enron_data["COLWELL WESLEY"]["from_this_person_to_poi"]

jks = enron_data["SKILLING JEFFREY K"]["exercised_stock_options"]

names = ["SKILLING JEFFREY K", "LAY KENNETH L", "FASTOW ANDREW S"]
for n in names:
    earnings = enron_data[n]["total_payments"]
    print(earnings)
    
enron_pd = pd.DataFrame.from_dict(enron_data)
enron_pd = enron_pd.T

salary = pd.DataFrame(enron_pd.loc[:,'salary'])
count = salary['salary'].value_counts()
salary['salary'] = pd.to_numeric(salary['salary'], errors='coerce')
salary.dropna(inplace=True)
#salary['salary'].contains('NaN')

emails = pd.DataFrame(enron_pd.loc[:,'email_address'])
counte = emails['email_address'].value_counts()

total_payment = pd.DataFrame(enron_pd.loc[:,'total_payments'])
counte = total_payment['total_payments'].value_counts()