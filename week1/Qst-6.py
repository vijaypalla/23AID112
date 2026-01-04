Age = int(input("Enter your age : " ))
if Age<13 :
    print("You are a child")
else :
    if 13<= Age <=17 :
        print("You are a teenager")
    else:
        if 18<= Age <=64 :
            print("You are an adult")
        else:
            print("You are a senior")
