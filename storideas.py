from en import menuEn, clearEn, contEn
from es import menuEs

#MAIN MENU
def mainmenu():
    op = 0
    while (op < 1) or (op > 3):
        clearEn()
        print("-----MLT STORIDEAS-----")
        print("1) English")
        print("2) Español")
        print("3) Exit")
        try:
            op = int(input("Select a language/option (1-3): "))
        except ValueError:
            None
        else:
            if(op == 1):
                menuEn()
            if(op == 2):
                menuEs()
            if(op == 3):
                print("Saliendo del programa...")

mainmenu()