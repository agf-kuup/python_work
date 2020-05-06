import os                       # Create things in the computer.
import simplejson as json       # Edit content in file data.
import subprocess               # Open subprocesses in computer.
import PySimpleGUI as sg        # 
import time                     # To avoid running everything at the same time.
import webbrowser               # To open the webbrowser.
sg.theme('LightGray1')	# Add a touch of color

# Code to create data where any information involved to this project will be saved.
user_folder=os.environ['USERPROFILE'].replace('\\','/')+'/' # Gets the user path where the info folder will be saved.
name_new_dir= "py_set"                                      # Name of folder
new_dir_path = user_folder + name_new_dir                   # New folder, in case this program grows, I will have this folder instead of a file.
name_new_file="startup"                                     # Name of the file. If you change the name, change data_file in the file "pushed.py".

#Creating files for next processes. Needs update.
try:
    os.mkdir(new_dir_path)                                  # Creating the folder for working without disturbing.
except OSError:
    message="Creation of the directory \"{}\" failed.\nThe directory already exists".format(new_dir_path) # If fails, is because it already exists.
else:                                                       # Else, creates it.
    message="Successfully created the directory {} ".format(new_dir_path)
window = sg.PopupAutoClose(message,title="Creating data",auto_close_duration=3)

data_file_path=user_folder+"{}/{}.json".format(name_new_dir,name_new_file)  # Path to the file.
if os.path.isfile(data_file_path) and os.stat(data_file_path).st_size!=0:   # If the file isn't empty, we already have information inside it
    data_file=open(data_file_path,'r+')                                     # So we read it
    d=json.loads(data_file.read())                                          # Charge it and show it in a message.
    msg='Reading file...\nActual content of file has:\n'+\
        ''.join(c for c in json.dumps(d, sort_keys=True, indent=4 * ' ') if not c in ['[',']','{','}',',','"'])+\
        "This content can be edited in {}/{}.json reading the readme.  ".format(name_new_dir,name_new_file)
    data_file.close()                                                       # Never leave open the file!
else:    
    data_file=open(data_file_path,'w+')             # We open the file again, 
    data_file.seek(0)                               # point to the first line
    d={'webs':[ 'https://github.com/',              # and write over it all the content.
                'https://www.youtube.com/',         # Obviously those links are my preferences, and you can edit them
                'https://mail.google.com/',         # throught this file or entering the data_file_path file just adding or deleting the 
                'https://web.whatsapp.com/'],       # lines you dis/like
        'programs':[
                user_folder+'AppData/Roaming/Telegram Desktop/Telegram.exe',   # Again, my programs, and you can edit them in the same way
                user_folder+'AppData/Local/Programs/Microsoft VS Code/Code.exe'# like the links
                ]}
    data_file.write(json.dumps(d))                  # writing over the file and sending a message with the updated content.
    msg="Creating new data file...\nThe content of data file will be:"+\
        ''.join(c for c in json.dumps(d, sort_keys=True, indent=4 * ' ') if not c in ['[',']','{','}',',','"'])+\
        "\nThis content can be edited in {}/{}.json reading the readme.  ".format(name_new_dir,name_new_file)
    data_file.close()                               # Again, closing!
window = sg.PopupAutoClose(msg[:-2],title="Reading data",auto_close_duration=5) # Tiny advisement of what's inside 

#######################################
#Opening and running programs for starting day.
# chrome.exe folder dir
chromedir= 'C:/Program Files (x86)/Google/Chrome/Application/chrome.exe %s'
for i in d['webs']:                 # For the links, we just call them this way
    webbrowser.get(chromedir).open(i)
for i in d['programs']:             # And for the progrms we make subprocesses but they're not dependent of this script.
    subprocess.Popen([i, '-new-tab'], stderr=subprocess.DEVNULL)
    time.sleep(1)                   # To avoid stumblings between processes, just made wait 1 second each process.

gitmsg="Do you want to check your github?"
popup=sg.popup_yes_no(gitmsg,title="Github")        # Pop up to let the user decide if s/he wants to be advised when he haven't done pushes to github.
while True:
    if popup in (None,'No'):                        # if user closed the window using X or clicked Quit button
        last_msg="Closing...\nIf you change your mind, you can run just pushed.py." # The script will end without more.
        window = sg.PopupAutoClose(last_msg,title="Closing",auto_close_duration=4)
        break
    else: 
        import pushed    # Else you will start pushed process to check your github processes.
        break            # Importing the file is absolutely better than making it a process. Best idea ever.
exit()                   # And after all, this finishes.