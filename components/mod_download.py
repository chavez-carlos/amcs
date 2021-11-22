try:
    from components.swdtools import *
except:
    from swdtools import *
import subprocess

def moddownload_by_id(mod_id) :
    url = 'https://steamcommunity.com/sharedfiles/filedetails/?id=' + mod_id
    command = swd_command()
    subprocess.run([command, url])
    print('Download Succesful')



