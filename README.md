# python_work
 Python script to run programs and open tabs in the moment is ran.

# How it works

The code is very primitive. You must run `main.py` if you want to run all 
the programs. It generates a folder called `data`, that will contain a json 
file with two parts, the `webs` (the links that will be opened by the 
program) and the `programs` that are the ubications of the programs that 
will be opened by the script.

The idea is to make this a script that runs when you start your computer so
you can just wait everything opens and you can start working. Yeah, you could
do this in windows, or whatever you use, but I'm just trying to see how far I
can go with Python.

Also I want to be constantly working in my github account, so I will create an
alert to remind me to work until push something useful in my repositories. This
part is started in `pushed.py`, but it's far from being complete.

The actual `pushed.py` file asks for the username of the owner, pastes it the
entry github in `data.json` and never ask again the username. After that you
will be notified in that moment if you have already pushed something that day.
The idea is to generate a notification until push something.

The good thing is that you can run `pushed.py` without running main, and it will
still work asking your username if you haven't added yet, and also when this 
script becomes a reminder, it will be able to be run by itself instead of depending
on `main.py`.

# Structure of data/data.json

Just in case you need understanding of how it works, `data.json` has the next 
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

to add any other link or program, for the moment just add it manually by pasting 
what you want in were it must be. For example, if you want to add notepad in 
Windows, you look for the program, open the ubication of the exe file, copy it,
write the name of the exe file in the end, and paste it in programs. In the case
of webpages you just copy the link and paste it. **Don't forget to add the commas!**


# What's next

 * ~~I just want to make a reminder alert that appear each certain time. The alert will
appear periodically until you update your github. The idea is to use tkinter for now
until get better ways to give the notification in Windows.~~ The idea of the reminder was
done with the marvelous library [`win10toast`](https://github.com/jithurjacob/Windows-10-Toast-Notifications).

 * Make it an executable script to run when the computer starts.
 
 * If I finish, I want to know how to edit everything to do it in Linux. I don't have
 a Mac so I can't work in that for now.

# A bit more

I'm not saying this will be useful, but it's a nice idea I came when learning how to 
open things with python. If you have a better idea to improve this project, please
tell me. Now I'm enjoying my learning and having new ideas is the best way to learn 
more.