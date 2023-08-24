import kssb_menu

menu = kssb_menu.KssbMenu()

result = menu.download()
for k, v in result.items():
    print(f'Menu for {k}:\n{v}\n')
