from selenium import webdriver
import json
import os
from ast import literal_eval as make_tuple

# Functions to implement
# 1. Adding a team member on the ppia website
# 2. Parse filename to tuple (Name, Position)
# 3. Load admin.json into tuple (username, password, link)

""" 
Process:
1. Iterate through team photo directory
2. Open a headless chrome browser, login to admin panel, open add teams
3. Add each image file as a team member (Name & position on filename, division from directory)
"""

# Iterator for img files in directory
def file_reader(root):
    for division in os.listdir(root):
        for img in os.listdir(root + '/' + division):
            print(img.split(','))

# Loads admin.json into tuple (username, password, link)
def read_admin_info():
    with open('admin.json') as json_file:
        data = json.load(json_file)
        return (data['username'], data['password'], data['link'])


file_reader('Photoshoot')
