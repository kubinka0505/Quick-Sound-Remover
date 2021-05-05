File_Name_Label = Label(root,
	textvariable = Text,
	justify = "center",
	fg = "white",
	bg = Config["Window"]["Background Color"],
	font = ("TkDefaultFont", 12, "bold")
	)
File_Name_Label.pack()
File_Name_Label.place(
	x = Percentage(Config["Window"]["Size"]["Width"], 50),
	y = Percentage(Config["Window"]["Size"]["Height"], 25),
	anchor = "center"
	)