#!/usr/bin/env python

import requests
import sys

# check if the user passed an ID as an argument
if len(sys.argv) < 2:
    sys.exit("Please pass your ID as an argument")

STUDENT_ID = sys.argv[1]
API_ENDPOINT = 'https://mplan.ashesi.edu.gh/API/api/getCurrentBalance/'
FAIL = "fail"

# make request to the API; convert result to JSON
response = requests.get(API_ENDPOINT + STUDENT_ID)
data = response.json()

# check if the request was successful
if data['status'] == FAIL:
    sys.exit("Invalid ID")

print('Your meal plan balance is', data['current_balance'])
