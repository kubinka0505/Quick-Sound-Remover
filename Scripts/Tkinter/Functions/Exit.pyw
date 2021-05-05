def Exit():
	try:
		if len(listdir(FolderName)) == 0:
			print("Saving Directory was removed permamently ({0} files inside)".format(len(listdir(FolderName))))
			rmdir(path.abspath(FolderName))
	except:
		pass
	exit()