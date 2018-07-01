def menu():
    print('Electronic Phone Book')
    print('=====================')
    print('1. Look up an entry')
    print('2. Set an entry')
    print('3. Delete an entry')
    print('4. List all entries')
    print('5. Quit')

numbers = {}
menuchoice = 0
menu()
while menuchoice != 5:
    menuchoice = int(input("What do you want to do (1-5)? "))
    if menuchoice == 1:
        name = input("Name: ")
        if name in numbers:
            print("Number: ", numbers[name])
        else:
            print(name, "not found")
        menu()
    elif menuchoice == 2:
        name = input("Name: ")
        phone = input("Number: ")
        numbers[name] = phone
        print("Entry stored for {}.\n".format(name))
        menu()
    elif menuchoice == 3:
        name = input("Name: ")
        if name in numbers:
            del numbers[name]
            print("Entry deleted for {}.\n".format(name))
        else:
            print(name, "was not found")
        menu()
    elif menuchoice == 4:
        name = input("Name: ")
        if name in numbers:
            print("Number: ", numbers[name])
        else:
            print(name, "not found")
        menu()
    elif menuchoice != 5:
        menu()
        break