Index = 0
def Previous(event = None):
	global Index
	mx.pause()
	Status_Label["fg"] = "gold"
	Path.set("Previous")
	if Index <= 0:
		Index = 0
	else:
		Index -= 1
		try:
			Text.set(Files[Index])
			print('Index: {0}\t| File Name: "{1}"'.format(Index, sep.join(path.abspath(Files[Index]).split(sep)[-2:])))
			try:
				Sound = mx.Sound(Files[Index])
				Sound.set_volume(.125)
				Sound.play()
			except FileNotFoundError:
				Status_Label["fg"] = Config["Window"]["Removed Color"]
				Path.set("Removed")
				pass
		except IndexError:
			pass