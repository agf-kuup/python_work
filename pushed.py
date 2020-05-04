import subprocess               # Open subprocesses in computer.
import requests                 # Ask for webpages.
import os                       # Create things in the computer.
import sys                      # Permit close if main wasn't run.
import simplejson as json       # To edit content in file data.
from datetime import date       # Get the date of today.

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
    print('''In order to ask you, it's needed your profile's name.
Enter to "Your Profile" and copy the part next to the last "/".
For example, in\n
         https://github.com/repositorio-generico
\nthe name is repositorio-generico\n''')

    username=input("""Paste the name of your repository.\nThis will be asked once if the username is saved in data.\n""")
    d['github']=username
    data_file.seek(0)
    print("Your name was saved.")
    data_file.write(json.dumps(d))
data_file.close()


flag=False
r=requests.get("https://github.com/"+username)
path = os.getcwd()
if r.status_code!=200:
    print("""Something is failing with your connection.
This code will run but probably will fail if isn't in a folder with
github repositories.
If you have a folder where your repositories are saved,
put this folder inside in order to find the last log you did""")
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
            print("\nYou have done something today! :-)")
            flag=True
            break
    print("\nYou haven't done anything today! :-(")

else:
    if 'fill="#ebedf0" data-count="0" data-date="{}"'.format(today) in r.content.decode("UTF-8"):
        print("\nYou haven't done anything today! :-(")
    else:
        flag=True
        print("\nYou have done something today! :-)")

# if flag==False:
#     while True:
#         X=input("Do you want me to remind you to push in your repos? Yes (y)/ No (n)")
