import kssbmenu

menu = kssbmenu.KssbMenu()

result = menu.download()
for k, v in result.items():
	print(f'Menu for {k}:\n{v}\n')
