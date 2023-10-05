name = "Dave"
count = 1


def another():
    color = "blue"
    global count  # global keyword allows access to global variable
    count += 1
    print(count)

    def greeting(name):
        nonlocal color  # nonlocal keyword allows access to outer scope variable 
        color = "red"
        print(color)
        print(name)

    greeting("Dave")


another()
