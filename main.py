from os import system, name
from time import sleep
import random


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
            gameLogic('Easy', 'heroes')
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


def gameLogic(level, topic):
    arr = words(topic)
    result = random.choice(arr) # randomszó
    resultlst = [char for char in result]
    question = [] # _ _ _
    choice = '' # A már választott betűk
    choicelst = [' ', '-']
    life = 7
    for i in resultlst:
        if i == ' ':
            question.append(i)
        elif i == '-':
            question.append(i)
        else:
            question.append('_')
    while life != 0 or result != choice: #Ez csak azt veszi figyelembe, hogy ha elfogy a hp, vagy direktbe kitalálják a szót.
        for x in range(len(resultlst)):
            # print(x)
            if choice.lower() == resultlst[x].lower():
                # print(x)
                question[x] = resultlst[x]
            else:
                pass
                # question += ''.join('_ ')
        print(result)
        print(question)
        choice = input("\nKérem tippeljen: ")
        choicelst.append(choice)


def end(bool):
    pass


def main():
    # menu()
    gameLogic('Easy', 'heroes')


main()
