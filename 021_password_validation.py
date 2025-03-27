password = "python123"
while True:
    user = input("Enter password: ")
    if user == password:
        print("Access Granted")
        break

    else:
        print("Wrong Password, try again!")
