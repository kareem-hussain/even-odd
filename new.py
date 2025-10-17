a1=int(input("enter the 1 number"))
a2=int(input("enter the 2 number"))
a3=int(input("enter the  3 number"))
a4=int(input("enter the 4 number"))
if (a1>a2 and a1>a3 and a1>4):
    print("a1 is highest number")
elif (a2>a1 and a2>a3 and a2>a4):
    print("a2 is highest")
elif (a3>a1 and a3>a2 and a3>a4):
    print("a3 is highest")
elif (a4>a1 and a4>a2 and a4>a3):
    print("a4 is highest")
else:
    print("nothing")    
