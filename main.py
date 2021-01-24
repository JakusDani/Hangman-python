from os import system, name
from time import sleep


def clear():
    _ = system('clear')


def menu():
    menu = ""
    level = "Easy"
    topic = "Heroes"
    while menu != "3":
        print("1. Játék kezdése\n2. Beállítások\n3. Kilépés")
        print("\n\nlevel: {}\ntopic: {}".format(level, topic))
        menu = input("\nKérem válasszon a menüből: ")
        clear()
        if menu == "1":
            gameLogic('Easy')
        if menu == "2":
            settings = difficulty(level, topic)
            level = settings[0]
            topic = settings[1]
        # return menu
    print("Köszi a játékot")


def difficulty(level, topic):
    menu = ""
    while menu != "3":
        print("1. Nehézség\n2. Téma\n3. Vissza")
        menu = input("Kérem válasszon nehézséget, vagy témát: ")
        clear()
        if menu == "1":
            dicLevel = {1: "Easy", 2: "Medium", 3: "Hard"}
            lenght = len(dicLevel)
            for  i in range(lenght):
                print("{}. {}".format(i + 1, dicLevel[i + 1]))
            level = int(input("Válasszon nehézséget: "))
            level = dicLevel[level]
        clear()
        if menu == "2":
            dicTopic = {1: "Heroes", 2: "Macskák", 3: "Országok"}
            lenght = len(dicTopic)
            for i in range(lenght):
                print("{}. {}".format(i + 1, dicTopic[i + 1]))
            topic = int(input("Kérem válasszon témát: "))
            topic = dicTopic[topic]
        clear()
    # clear()
    return level, topic


def words(topic):
    if topic == "heroes":
        arr = []
        f = open("{}.txt".format(topic), "r")
        for x in f:
            if '(' in x:
                test = x.split('(')
                arr.append(test[0])
            else:
                arr.append(x.replace("\n", ""))
        f.close()
        return arr
    else:
        pass


def gameLogic(level):
    pass


def end(bool):
    pass


def main():
    # menu()
    words('heroes')


main()
