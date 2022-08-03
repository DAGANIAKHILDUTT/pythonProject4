class ticket:
    def __init__(self,s,n,a,f):
        sno=0
        name=n
        booked=False
        age=a
        fare=f
    def book(self):
        pass
class hyderabad(ticket):
    def __init__(self):
        print("Your destination is Hyderabad!!")
        f=1000
    def book(self):
        print("Please Enter your details name and age")
        name=input("Enter your name:")
        age=int(input("Enter your age:"))
        booked=True
        print("\n\nYour ticket is booked succesfully!!\n\n")
class ratnalcheruvu(ticket):
    def __init__(self):
        print("Your destination is Ratnalcheruvu!!")
        f = 50
    def book(self):
        print("Please Enter your details name and age")
        name = input("Enter your name:")
        age = int(input("Enter your age:"))
        booked = True
        print("\n\nYour ticket is booked succesfully!!\n\n")


list=[]
while(True):
    print("The train destinations are\n1.Hyderabad\n2.Ratnalcheruvu\n3.Exit from the window")
    n = int(input("Enter your destination 1 or 2 or 3:"))
    if (n == 1):
        obj = hyderabad()
        print("Your fare is 1000")
        obj.book()
        list.append(obj)
    elif (n == 2):
        obj = ratnalcheruvu()
        print("Your fare is 49")
        obj.book()
        list.append(obj)
    else:
        print("\n\nYou exited from the window")
        break