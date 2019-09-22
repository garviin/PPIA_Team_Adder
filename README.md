# PPIA_Team_Adder

A script made for the Indonesian Student's Association in Melbourne University to update their website with new committee members. 

## Dependencies
- Firefox ver. 46 and newer
- Selenium
- Geckodriver v0.25.0


## Usage
1. Clone this repo.
2. Create an 'admin.json' file in the root directory, fill out this json object with the relevant details:
'''
{
    "username":"username",
    "password":"password",
    "link": "link_to_add_team_members"
}
'''
3. Name the jpg files as "<name>,<position>". Arrange them in folders named by their division. Store all      the divison folders in one folder, store that in the root directory of the repo.
4. Run:
''' 
python3 adder.py
'''

## Current Status: 
Script works semi-manually, it can fill out the forms, but uploading images only works 5/10 times as the wordpress CMS times out half the time, and that has to be handled manually.

Possible solution: Compress the images to <300kb, could lessen the chance of the cms timing out.