root = Tk()
root.title(_Title)
root.resizable(False, False)
root.iconbitmap(BaseDir + "/Documents/Pictures/QSR.ico")
root.configure(background = Config["Window"]["Background Color"])
root.geometry("{0}x{1}+{2}+{3}".format(
	Config["Window"]["Size"]["Width"],
	Config["Window"]["Size"]["Height"],
	root.winfo_screenwidth() // 2 - Config["Window"]["Size"]["Width"] // 2,
	root.winfo_screenheight() // 2 - Config["Window"]["Size"]["Height"] // 2
	))

Text = StringVar()
Text.set("Press {0} to start!".format(Config["Controls"]["Next"]))
Path = StringVar()
Path.set("Idle")