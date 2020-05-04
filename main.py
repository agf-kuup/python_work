# Script to set up everything in the computer when it starts.
# First the program will open the chrome browser to open all 
# the tabs that are used frequently by me.
# 
# 
# After that it opens the programs I usually open first.
#  
import os                       # To create things in the computer.
import simplejson as json       # To edit content in file data.
import subprocess               # To open subprocesses in computer.
import sys
import time                     # To avoid running everything at the same time.
import webbrowser               # To open the webbrowser.

# Code to create data where any information involved to this project will be saved.
path = os.getcwd()
new_dir = os.getcwd()+"\data"
name_new_dir=new_dir.split('\\')[-1]

#Creating files for next processes. Needs update.
try:
    os.mkdir(new_dir)
except OSError:
    print ("Creation of the directory \"{}\" failed. The directory already exists".format(name_new_dir))
else:
    print ("Successfully created the directory {} ".format(name_new_dir))

if os.path.isfile("./data/data.json") and os.stat('./data/data.json').st_size!=0:
    print("Reading file...")
    data_file=open('./data/data.json','r+')
    d=json.loads(data_file.read())
    data_file.close()
else:
    print("Creating new data file...")
    data_file=open('./data/data.json','w+')
    data_file.seek(0)
    d={'webs':[ 'https://github.com/',
                'https://www.youtube.com/',
                'https://mail.google.com/',
                'https://web.whatsapp.com/'],
        'programs':[
                'C:/Users/anton/AppData/Roaming/Telegram Desktop/Telegram.exe',
                'C:/Users/anton/AppData/Local/Programs/Microsoft VS Code/Code.exe'
                ]}
    data_file.write(json.dumps(d))
    print("Updating data...\n")
    data_file.close()
#######################################
#Opening and running programs for starting day.
# chrome.exe folder
chromedir= 'C:/Program Files (x86)/Google/Chrome/Application/chrome.exe %s'
print("\nActual webpages added are:")
for i in d['webs']:
    #webbrowser.get(chromedir).open(i)
    print("    {}".format(i))
print("\nActual programs added are:")
for i in d['programs']:
    #subprocess.Popen([i, '-new-tab'], stderr=subprocess.DEVNULL)
    time.sleep(1)
    print("    {}".format(i))

githubcheck=input("Do you want to check your github? Yes(y) / No(n)\n")
if githubcheck=='y':
    subprocess.call(["python", "pushed.py"])
else:
    print("""Closing...
If you change your mind, you can run just pushed.py.""")
    exit()
