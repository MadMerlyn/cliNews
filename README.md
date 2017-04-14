This python script scrapes the stories within "Top Stories" section of the google news page, and after parsing them, prints out the headlines alongwith a brief description of each headline.

If you'd like to run this script automatically whenever you open a command prompt on windows, you can do the following:
Open registry with Regedit, and create the following key:

* HKCU\SOFTWARE\Microsoft\Command Processor
* value: AutoRun
* type: REG_EXPAND_SZ
* data: python [location of .py]

I put mine in the local appdata folder %localappdata% variable in recent (>7) versions of windows, so my data looks like:
* python "%localappdata%\PyScripts\news_python3.py"
