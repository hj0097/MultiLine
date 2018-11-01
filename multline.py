x=0
line=str(input("the line u want to print  :"))
while True:
    try:
        no=int(input("number of time u wanna print this :"))
        break
    except Exception:
        print("enter a valid option")
if no == 0:
    print("u wanna print it right?")
else:
    while(no>x):
        print(line)
        x=x+1
    else:
        print("welll, goodbye")
