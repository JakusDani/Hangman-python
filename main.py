from os import system, name
from time import sleep
def clear():
    _ = system('clear')

def menu():
    menu = ""
    level = "1"
    topic = "sup"
    while menu != "3":
        print("1. Játék kezdése\n2. Beállítások\n3. Kilépés")
        print("\n\nlevel: {}\ntopic: {}".format(level, topic))
        menu = input("Kérem válasszon a menüből: ")
        clear()
        if menu == "2":
            settings = difficulty(level, topic)
            level = settings[0]
            topic = settings[1]
        # return menu
    print("Köszi a játékot")


def difficulty(level, topic):
    menu = ""
    while menu != "3":
        print("1. nehézség\n2. Téma\n3. Vissza")
        menu = input("Válasszon nehézséget, vagy témát: ")
        if menu == "1":
            print("1. Easy\n2. Medium\n3. Hard")
            level = input("Válasszon nehézséget: ")
    clear()
    return level, topic

def words(level, topic):
    pass


def gameLogic():
    pass


def end(bool):
    pass


def main():
    menu()


main()