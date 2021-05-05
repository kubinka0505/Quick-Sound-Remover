Index = 0
def Next(event = None):
	global Index
	mx.pause()
	Status_Label["fg"] = "gold"
	Path.set("Next")
	if Index > len(Files):
		Index = len(Files)
	else:
		Index += 1
		try:
			Text.set(Files[Index])
			print('Index: {0}/{1}\t\t| File Name: "{2}"'.format(Index, len(Files), sep.join(path.abspath(Files[Index]).split(sep)[-2:])))
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
			Index = len(Files) - 1