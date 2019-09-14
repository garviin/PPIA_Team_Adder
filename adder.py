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