"""QSR - Quick Sound Remover

Simple, fast and very versatile
GUI sound removal tool."""

__STA_TIME = __import__("time").time()
from os import *
from time import time
from tkinter import *
from json import loads
from random import randint
from tkinter.messagebox import *
environ["PYGAME_HIDE_SUPPORT_PROMPT"] = "hide"
from pygame import mixer as mx
del open

__author__		= "kubinka0505"
__copyright__	= __author__
__credits__		= __author__
__version__		= "1.0"
__date__		= "15.04.2021"
__status__		= "Mature"
__license__		= "GPL V3"

BaseDir = path.abspath(path.dirname(__file__))
chdir(BaseDir)

#-------------------------#

Config = loads(open("Config.json", encoding = "utf-8").read())
mx.init(frequency = Config["Audio"]["Samplerate"], buffer = Config["Audio"]["Buffer Size"])

FolderName = "Session_" + str(time()).split(".")[0]
chdir(Config["Working Directory"])
Files = next(walk("."))[2]

_Err = "There is only one audio file in the target folder."
_Title = "{0} v{1} by {2}".format(BaseDir.split(sep)[-1].replace("-", " "), __version__, __author__)

#------------#

print('Current working directory is "' + getcwd() + '"')
print('Saving Directory is "' + path.abspath(FolderName) + '"\n')

#-------------------------#

# Opening Scripts/Utils.pyw
exec(open(BaseDir + "/Scripts/Utils.pyw", encoding = "utf-8").read())
exec(open(BaseDir + "/Scripts/Tkinter/Functions/Setup.pyw", encoding = "utf-8").read())

#------------#

if len(Files) == 1:
	root.withdraw()
	print(_Err, "")
	showerror(title = _Title, message = _Err)
	exit()
else:
	try:
		chdir(FolderName)
	except FileNotFoundError:
		mkdir(FolderName)

#------------#

# Opening Functions/*.pyw
Functions = ["Next", "Previous", "Remove", "Exit"]
chdir(BaseDir + "/Scripts/Tkinter/Functions")

for Funcion in Functions:
	exec(open(path.abspath(Funcion + ".pyw"), encoding = "utf-8").read())

#------------------------#

# Opening Labels/*.pyw
Labels = ["File_Name", "Status"]
chdir(BaseDir + "/Scripts/Tkinter/Labels")

for Label_ in Labels:
	exec(open(path.abspath(Label_ + ".pyw"), encoding = "utf-8").read())

#-------------------------#

exec(open(BaseDir + "/Scripts/Tkinter/Labels.pyw", encoding = "utf-8").read())

chdir(BaseDir)
chdir(Config["Working Directory"])

#-------------------------#

root.protocol("WM_DELETE_WINDOW", Exit)
root.mainloop()