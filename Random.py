import random
n=random.randbytes(3)
print(n)
print(random.randrange(1,8))
print(random.randint(100,211))
mylist = ["Jadeja", "Ashwin", "Rahane","Shami","dhoni","virat"]
mylist1 = {"Jadeja", "Ashwin", "Rahane","Shami","dhoni","virat"}
print(random.choice(mylist))
#print(random.choice(mylist1))#Will Not Work with SET
random.shuffle(mylist)
print(mylist)