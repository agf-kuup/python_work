import requests                         # Ask for webpages.
import os                               # Create things in the computer.
import sys                              # Permit close if main wasn't run.
import time                             # Sleep program until 15 minutes later.
import simplejson as json               # To edit content in file data.
import PySimpleGUI as sg                # This is to ask for github checking. (pushed.py)
from win10toast import ToastNotifier    # Windows Notification.
from datetime import date               # Get the date of today.
from extra import getDate               # Just to edit the way a date is given.
sg.theme('LightGray1')	                # Color of all the next windows.


user_folder=os.environ['USERPROFILE']                   # Gets the user path where the info folder is saved to ask for your github account
data_file=open(user_folder+'/py_set/startup.json','r+')   # After that the file is opened. EDIT THIS NAME IF YOU CHANGE THE FILE NAME
d=json.loads(data_file.read().replace('\\','/'))                          # Reading content of file
if 'github' in d.keys():
    username=d['github']                                # Getting the github profile name
else:                                                   # If data isn't registered yet
    msg='''In order to ask you, it's needed your profile's name.\nEnter to "Your Profile" and copy the part next to the last "/".\nFor example, in\n\n         https://github.com/repositorio-generico\nthe name is repositorio-generico\nPaste the name of your repository.\nThis will be asked once if the username is saved in data.\n'''
    layout = [ [sg.Txt(msg,key='msg')],      
            [sg.In(key='username')],      
            [sg.Button('Add', bind_return_key=True)]]
    window = sg.Window('Username input', layout)        # Window asking for your profile name
    while True:                                         # Process to receive answer in the window.
        event, values = window.read()                   # Waiting for the profile name.
        if event is not None:      
            username = str(values['username'])      # Updating the variable username with your input.
            window.close()                          # Closing the window.
            break
        else:
            break
    d['github']=username                            # Setting the profile name in the file for next time.                             
    data_file.seek(0)                               # Preparing to write in the first line.
    data_file.write(json.dumps(d))                  # Writing....
data_file.close()                                   # Don't forget to close the file.


today=date.today()                                  # Info for checking the day and verify if the have been pushes or not.
def Have_you_finished_those_errands(squidward):     # Asking info in github.
    try:
        r=requests.get("https://github.com/"+squidward) # Requests asking for the content in that page.
        if r.status_code==200:
            if 'fill="#ebedf0" data-count="0" data-date="{}"'.format(today) in r.content.decode("UTF-8"): # We find the color of the square of today
                return False
            else:
                return True
    except requests.ConnectionError:
        alert="You don't have internet connection.\nI can't check if you updated something :("
        sg.PopupAutoClose(alert,title="No connection :(",auto_close_duration=10) # A popup opens and says if you did something today.
        sys.exit()

if Have_you_finished_those_errands(username):       # If you have done a push, let me tell you.
    update="\nYou have done something today! :-)"
else:                                               # If not, you don't deserve a happy face.
    update="\nYou haven't done anything today! :-("
sg.PopupAutoClose(update,title="Status",auto_close_duration=10) # A popup opens and says if you did something today.
if ":-)" in update:                                 # I just need to check if :-) is in the update to know if something has been pushed.
    sys.exit()                                      # Here is important. If there has been an update, I will finish the process. If not, this continues to the next lines. 

alert_msg="Do you want me to remind you to push in your repos?\n"
popup=sg.popup_yes_no(alert_msg,title="Alerts")     # Popup to ask if you want to get an advise in your desktop each 7 minutes.
if popup=='No':                                     # If not, see you next time.
    sys.exit()
else:                                               # Else the process will continue
    while True:                                     # And it will continue each 7 minutes until you push something... or turn down the program.
        if Have_you_finished_those_errands(username):
            toaster = ToastNotifier()               # This is the last notifier for today, promise.
            toaster.show_toast("Nice! You were productive today :-)!!",
                                "See you tomorrow!!",
                                duration=10)
            sys.exit()
        else:
            toaster = ToastNotifier()               # Windows notifier created.
            toaster.show_toast("Hey! You haven't pushed yet!!",     # And its content.
                                "Continue working to avoid that empty square!!",
                                duration=10)        # It will last for 10 seconds.
        time.sleep(60*7)                            # If you want to edit the time the notifier appears, edit this.