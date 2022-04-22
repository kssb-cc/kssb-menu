import kssbmenu

menu = kssbmenu.kssb_menu()

result = menu.download()
for k, v in result.items():
	print(f'Menu for {k}:\n{v}\n')
