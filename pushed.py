import subprocess                       # Open subprocesses in computer.
import requests                         # Ask for webpages.
import os                               # Create things in the computer.
import sys                              # Permit close if main wasn't run.
import time                             # Sleep program until 15 minutes later.
import simplejson as json               # To edit content in file data.
import PySimpleGUI as sg      
from win10toast import ToastNotifier    # Windows Notification
from datetime import date               # Get the date of today.
from extra import getDate

today=date.today()
######################################
# Running a script to know if today I have updated my github.
# If you don't have internet, you must call all the git repos in your laptop in order
# to know if you have already pushed something today. 
# I pray to any god you don't have like a million or this will take a life.

data_file=open('./data/data.json','r+')
d=json.loads(data_file.read())
if 'github' in d.keys():
    username=d['github']
else:
    msg='''In order to ask you, it's needed your profile's name.
Enter to "Your Profile" and copy the part next to the last "/".
For example, in\n
         https://github.com/repositorio-generico
\nthe name is repositorio-generico\n
Paste the name of your repository.\nThis will be asked once if the username is saved in data.\n'''
    layout = [ [sg.Txt(msg,key='msg')],      
            [sg.In(key='username')],      
            [sg.Button('Add', bind_return_key=True)]]

    window = sg.Window('Username input', layout)      

    while True:      
        event, values = window.read()      

        if event is not None:      
            username = str(values['username'])      
            window.close()
            break
        else:
            break
    d['github']=username
    data_file.seek(0)
    data_file.write(json.dumps(d))
data_file.close()


flag=False
r=requests.get("https://github.com/"+username)
path = os.getcwd()
if r.status_code!=200:
    status_fail_msg="""Something is failing with your connection.
This code will run but probably will fail if isn't in a folder with
github repositories.
If you have a folder where your repositories are saved,
put this folder inside in order to find the last log you did"""
    sg.popup(status_fail_msg,title="Status")
    path=path.split(":")[1].replace('\\','/')[1:]
    output = subprocess.check_output(['bash.exe','-c', "cd ..; find . -name .git -type d -prune".format(path)])
    for i in output.decode("utf-8").split('\n')[:-1]:
        h=subprocess.check_output(['bash.exe',
                                    '-c', 
                                    "cd ..;\
                                    cd {};\
                                    git log -1;".format(i[2:-4])])
        day=getDate(h)
        if today==day:
            update="\nYou have done something today! :-)"
            flag=True
            break
    if flag==False:
        update="\nYou haven't done anything today! :-("

else:
    if 'fill="#ebedf0" data-count="0" data-date="{}"'.format(today) in r.content.decode("UTF-8"):
        update="\nYou haven't done anything today! :-("
    else:
        flag=True
        update="\nYou have done something today! :-)"
sg.PopupAutoClose(update,title="Status",auto_close_duration=5)

if ":-)" in update:
    sys.exit()

if flag==False:
    while True:
        alert_msg="Do you want me to remind you to push in your repos?\n"
        popup=sg.popup_yes_no(alert_msg,title="Alerts")
        if popup=='No':
            sys.exit()
        else:
            while True:
                r=requests.get("https://github.com/"+username)
                if 'fill="#ebedf0" data-count="0" data-date="{}"'.format(today) in r.content.decode("UTF-8"):
                    toaster = ToastNotifier()
                    toaster.show_toast("Hey! You haven't pushed yet!!",
                                        "Continue working to avoid that empty square!!",
                                        icon_path="icon.ico",
                                        duration=10)
                else:
                    toaster = ToastNotifier()
                    toaster.show_toast("Nice! You were productive today :-)!!",
                                        "See you tomorrow!!",
                                        icon_path="icon.ico",
                                        duration=10)
                    sys.exit()
                time.sleep(60*10)