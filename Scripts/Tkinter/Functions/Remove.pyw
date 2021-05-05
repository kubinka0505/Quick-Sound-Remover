def Remove(event = None):
	global Index
	Status_Label["fg"] = "Coral1"
	Path.set("Removed")
	try:
		if not Config["Remove Permamently"]:
			rename(path.abspath(Files[Index]), path.abspath(FolderName + sep + Files[Index].split(sep)[-1]))
		else: 
			remove(path.abspath(Files[Index]))
			print('Removed "{0}" permamently'.format(sep.join(path.abspath(Files[Index]).split(sep)[-2:])))
	except FileNotFoundError as Error:
		print('File "' + path.abspath(Files[Index]) + '" cannot be removed (Errno {0})'.format(Error.errno))
		Status_Label["fg"] = Config["Window"]["Removed Color"]
		Path.set("File not found!")	