#TODO:add support for steam workshop directly
#Done. using steam workshop directly rather than smods.ru
try:
    from components.wipannounce import wipannounce_notready
    from components.mod_download import *
except:
    from wipannounce import wipannounce_notready
    from mod_download import *

from pathlib import Path
from bs4 import BeautifulSoup
import requests




def searchbyid(search_id):
    #I give up, its too hard to scrap that site
    #Using https://github.com/SegoCode/swd under Unlicense license
    #Implement "Is this the mod you want?" in the future
    moddownload_by_id(search_id)





def modsearch():
    running = True
    while running == True:
        print('Search by:')
        print('1. ID')
        print('2. Name/Tags (WIP)')
        print('3. Cancel Search')
        selection = input()
        if selection == '3':
            running = False
        elif selection == '2':
            wipannounce_notready()
        elif selection == '1':
            running_searchid = True
            while running_searchid == True:
                idtosearchfor = input('Type the ID to search for: ')
                if idtosearchfor.isdigit() == True:
                    searchbyid(idtosearchfor)
                    running_searchid = False
                else:
                    print("The input isn't a number!")
        else:
            print('Invalid Option!')
