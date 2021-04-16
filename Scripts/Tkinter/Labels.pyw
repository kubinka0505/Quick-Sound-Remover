Next_Button = Button(root, text = Next.__name__)
Next_Button.bind_all(Config["Controls"]["Next"], Next)

Previous_Button = Button(root, text = Previous.__name__)
Previous_Button.bind_all(Config["Controls"]["Previous"], Previous)

Remove_Button = Button(root, text = Remove.__name__)
Remove_Button.bind_all(Config["Controls"]["Remove"], Remove)