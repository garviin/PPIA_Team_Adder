# Status: Script works semi-manually, it can fill out the forms,
#         but uploading images only works 5/10 times as the wordpress
#         CMS times out half the time, and that has to be handled manually.

from selenium.webdriver import Firefox
from selenium.webdriver.firefox.options import Options
from selenium.common.exceptions import NoSuchElementException 
import json
import os
from ast import literal_eval as make_tuple
import time 


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
            info = [division]
            person = img.split(',')
            print(person)
            if (len(person) == 2 and input("proceed y/n?") == 'y'):
                info = info + person
                info[2] = clean_string(info[2])
                info.append(os.path.abspath(root + '/' + division + '/' + img))
                add_new_person(info)
                if(input("proceed y/n?") != 'y'):
                    browser.close()
                    quit()
                browser.get(LINK)

# Loads admin.json into tuple (username, password, link)
def read_admin_info():
    with open('admin.json') as json_file:
        return json.load(json_file)

def clean_string(string):
    return string.replace('.jpg','')

#def add_new_person(name,title):
    
# def check_exists_by_xpath(xpath):
#     try:
#         browser.find_element_by_xpath(xpath)
#     except NoSuchElementException:
#         return False
#     return True

info = read_admin_info()

LINK = info['link']
USERNAME = info['username']
PASSWORD = info['password']
DIVISON_ID = {
    'Executive': 'in-group-81',
    'Artifact': 'in-group-125',
    'Corporate Relation': 'in-group-85',
    'External': 'in-group-80',
    'Indonesian Film Festival': 'in-group-102',
    'Internal': 'in-group-79',
    'Media & Marketing': 'in-group-82',
    'Perspektif': 'in-group-101',
    'Social Welfare':'in-group-84',
    'Sports': 'in-group-83'
}

TRIAL_PATH = os.path.abspath("Photoshoot/Artifact/Alexander Jason Anggara,Treasurer.jpg")

opts = Options()
opts.headless = False
browser = Firefox(options=opts)
browser.get(LINK)

username = browser.find_element_by_id("user_login")
password = browser.find_element_by_id("user_pass")
submit   = browser.find_element_by_id("wp-submit")

username.send_keys(USERNAME)
password.send_keys(PASSWORD)

submit.click()

def add_new_person(info):
    time.sleep(1)
    
    browser.find_element_by_id("title").send_keys(info[1])
    browser.find_element_by_id("_cherry_team-position").send_keys(info[2])
    browser.find_element_by_id(DIVISON_ID[info[0]]).click()

    add_image = browser.find_element_by_id("set-post-thumbnail")
    add_image.click()
    # image upload
    # input_file = "//input[starts-with(@id, 'html5_')]"
    # browser.find_element_by_xpath(input_file).send_keys(info[3])

#file_reader('Photoshoot')

browser.close()
quit()