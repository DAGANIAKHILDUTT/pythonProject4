class dog:
    def __int__(self):
        print("hello")
    def fun1(self):
         print("parent")

class cat(dog):
    def __int__(self):
        print("bye")
        super().__int__()


o=cat()


