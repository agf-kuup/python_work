# python_work ![license](https://img.shields.io/badge/license-MIT-green)
 Python script to run programs and open tabs in the moment the script is executed.
 Also advices if you haven't updated anything new in your github (this last 
 idea is to give personal motivation).

Actually only works on Windows.

# How it works

You must run `main.py` before running `pushed.py` or this second won't 
work (this last one needs the file that will by running the first one). 
It generates a folder called `py_set`, that will contain only one 
json file with two parts: the `webs` (the links that will be opened by the
 program) and the `programs` (the paths of the programs that will be opened 
 by the script).

The idea is to make this a script that runs when you start your computer so
you can just wait everything opens before you start working. Yeah, you could
do this in Windows with something else, or whatever you use, but I'm just 
trying to see how far I can go with Python.

I want to be constantly working in my github account, so I created an
alert to remind me to work until push something useful in my repositories. This
part is started in `pushed.py`.

The actual `pushed.py` file asks for the username of the owner, pastes in the
entry `github` in `startup.json` and never asks again the username. After that you
will be notified in that moment if you have already pushed something that day.
The idea is to generate a notification until you push something.

You can run `pushed.py` without running `main.py`, but I insist: this is possible 
just if you have run `main.py` at least once.

# Structure of py_set/startup.json

Just in case you need understanding of how it works, `startup.json` has the next 
structure:

    {
    "webs": [
        "https://github.com/",
        "https://www.youtube.com/",
        "https://mail.google.com/",
        "https://web.whatsapp.com/"
    ],
    "programs": [
        "path_to_exe_file_1/Telegram.exe",
        "path_to_exe_file_2/Code.exe"
    ],
    "github": your_username
    }

to add any other link or program, add it manually by pasting what you want in were it must 
be. For example, if you want to add notepad in Windows, you look for the program,
 open the ubication of the exe file, copy it, write the name of the exe file in 
 the end, and paste it in programs. In the case of webpages you just copy the 
 link and paste it. **Don't forget to add the commas!**


# ~~What's next~~ What was done (or how was replaced to make it easier)

 * ~~I just want to make a reminder alert that appear each certain time. The alert will
appear periodically until you update your github. The idea is to use tkinter for now
until get better ways to give the notification in Windows.~~ The idea of the reminder was
done with the marvelous library [`win10toast`](https://github.com/jithurjacob/Windows-10-Toast-Notifications).

 * ~~Avoid only using the terminal to show text.~~ To avoid this, I added popup windows with 
 [`PySimpleGui`](https://pysimplegui.readthedocs.io/en/latest/). 
 It's a delightful library! Thanks, [@PySimpleGui](https://github.com/PySimpleGUI/PySimpleGUI)!

 * ~~Make it an executable script to run when the computer starts. (Library expected to use: pyinstaller)~~ 
 It's better to just do a batch file for this case. Easier and in just two lines.


# A bit more

I'm not saying this will be useful, but it's a nice idea I came when learning how to 
open things with python. If you have a better idea to improve this project, please
tell me. Now I'm enjoying my learning and having new ideas is the best way to learn 
more.

# If you want to do it "executable"

This idea came from a recommendation of @Dr_donut in a reddit post. 

* Open notepad
* Write a file of the form:

        "path to your python console" "path to the file main.py"
        pause
    
* Save it with the `.bat` extension.
* Double click it and will run :-) 