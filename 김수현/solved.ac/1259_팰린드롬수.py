while True:
    user_input = input()

    if user_input == '0':
        break

    if user_input == user_input[::-1]:
        print("yes")
    else:
        print("no")