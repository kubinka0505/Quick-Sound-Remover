from os import *
from shutil import *

chdir(path.abspath(path.dirname(__file__)))
chdir("../Audio")

for Folder in next(walk("."))[1]:
	rmtree(Folder)