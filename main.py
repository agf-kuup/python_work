import os                       # To create things in the computer.
import simplejson as json       # To edit content in file data.
import subprocess               # To open subprocesses in computer.
import sys
import time                     # To avoid running everything at the same time.
import webbrowser               # To open the webbrowser.
import PySimpleGUI as sg

# Script to set up everything in the computer when it starts.
# First the program will open the chrome browser to open all 
# the tabs that are used frequently by me.
# 
# 
# After that it opens the programs I usually open first.
#  

sg.theme('LightGray1')	# Add a touch of color

# Code to create data where any information involved to this project will be saved.
path = os.getcwd()
new_dir = os.getcwd()+"\data"
name_new_dir=new_dir.split('\\')[-1]

#Creating files for next processes. Needs update.
try:
    os.mkdir(new_dir)
except OSError:
    message="Creation of the directory \"{}\" failed.\nThe directory already exists".format(name_new_dir)
else:
    message="Successfully created the directory {} ".format(name_new_dir)
window = sg.PopupAutoClose(message,title="Creating data",auto_close_duration=3)


if os.path.isfile("./data/data.json") and os.stat('./data/data.json').st_size!=0:
    msg="Reading file...\n"
    data_file=open('./data/data.json','r+')
    d=json.loads(data_file.read())
    msg+='Actual content of file is:\n'
    msg+=''.join(c for c in json.dumps(d, sort_keys=True, indent=4 * ' ') if not c in ['[',']','{','}',',','"'])
    data_file.close()
else:
    msg="Creating new data file...\n"
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
    msg+="The content of data file will be:\n"
    msg+=''.join(c for c in json.dumps(d, sort_keys=True, indent=4 * ' ') if not c in ['[',']','{','}',',','"'])
    data_file.write(json.dumps(d))
    msg+="This content can be edited in data/data.json reading the readme\nfile."
    data_file.close()
window = sg.PopupAutoClose(msg[:-2],title="Reading data",auto_close_duration=3)


#######################################
#Opening and running programs for starting day.
# chrome.exe folder
chromedir= 'C:/Program Files (x86)/Google/Chrome/Application/chrome.exe %s'
for i in d['webs']:
    webbrowser.get(chromedir).open(i)
for i in d['programs']:
    subprocess.Popen([i, '-new-tab'], stderr=subprocess.DEVNULL)
    time.sleep(1)

gitmsg="Do you want to check your github?"

popup=sg.popup_yes_no(gitmsg,title="Github")  # Shows Yes and No buttons
while True:
    if popup in (None,'No'):        # if user closed the window using X or clicked Quit button
        last_msg="""Closing...\nIf you change your mind, you can run just pushed.py."""
        window = sg.PopupAutoClose(last_msg,title="Closing",auto_close_duration=4)
        break
    else: 
        subprocess.call(["python", "pushed.py"])
        break
exit()
