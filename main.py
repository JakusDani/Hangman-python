def menu():
    print("1. játék kezdése")
    print("2. beállítások")
    print("3. kilépés")
    menu = input("Kérem válasszon a menüből: ")
    print(menu)
    if menu == "2":
        topic = difficulty()
        print(topic[1])
    # return menu


def difficulty():
    topic = ""
    level = ""
    print("1. Téma: {}".format(topic))
    print("2. nehézség: {}".format(level))
    level = input("")
    return topic, level

def words(level, topic):
    pass


def gameLogic():
    pass


def end(bool):
    pass


def main():
    menu()


main()