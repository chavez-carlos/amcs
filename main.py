from components.wipannounce import wipannounce_notready
from components.modsearch import modsearch


print('version: amcs 0.0.1')
running = True
while running == True:
    print('What do you want to do?')
    print('1. Manage Mods (WIP)')
    print('2. Search for new mods')
    print('3. Exit')
    mainscreen_selection = input('selection: ')

    if mainscreen_selection == '1':
        wipannounce_notready()
    elif mainscreen_selection == '2':
        modsearch()
    elif mainscreen_selection == '3':
        running = False
    else:
        print('Invalid option!')
        






