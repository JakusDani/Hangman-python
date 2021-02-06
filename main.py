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
        clear()
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
    resultlst = list(result)
    question = [] # _ _ _
    choice = '' # A már választott betűk
    choicelst = []
    life = 2
    answer = ''
    for i in resultlst:
        if i == ' ':
            question.append(i)
        elif i == '-':
            question.append(i)
        else:
            question.append('_')
    while not (life == 0):
        clear()
        print(result, life)
        answer = ' '.join(question)
        print(answer)
        choice = input("\nKérem tippeljen: ")
        counter = 0
        for x in range(len(resultlst)):
            if choice.lower() == resultlst[x].lower():
                question[x] = resultlst[x]
                counter += 1
        if counter == 0:
            life -= 1  
        choicelst.append(choice)
        if resultlst == question:
            clear()
            print(f"You WIN!!, the correct answer is: {result}")
            sleep(2)
            return True
    print(f"You LOSE!!, the correct answer is: {result}")
    sleep(2)
    return False

def end(bool):
    pass


def main():
    menu()


main()
