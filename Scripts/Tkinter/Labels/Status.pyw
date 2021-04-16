Status_Label = Label(root,
	textvariable = Path,
	justify = "center",
	fg = "gold",
	bg = Config["Window"]["Background Color"],
	font = ("TkDefaultFont", 12, "bold")
	)
Status_Label.pack()
Status_Label.place(
	x = Percentage(Config["Window"]["Size"]["Width"], 50),
	y = Percentage(Config["Window"]["Size"]["Height"], 75),
	anchor = "center"
	)