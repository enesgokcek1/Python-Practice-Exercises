words = ["cat","dog","windwow"]
for kelime in words:
    print(kelime, len(kelime))
    

users = {"hans":"active", "elenore":"inactive", "sports": "active"}
for user, status in users.copy().items():
    if status == "inactive":
        del users[user]

active_users={}
for user, status in users.items():
    if status == "avctive":
        active_users[user] = status
    


# FOR 

l1 = [1,2,34,5,66]
toplam = 0
for listone in l1:
    toplam = toplam + listone
    print(listone)
print(toplam)


for x in range(7):
    print(x)
l2 = range(15,2,-2)
print(list(l2))

for x in range(1,20):
    if(x%3==0):
      continue
    print(x)
    
for y in range(1,10):
    if(y%2==0):
        break
    print(y)

# PASS İŞLEMİ : HERHANGİ BİR İŞLEM YAPILMAYACAK

for i in range(10):
    if i == 9:
        pass
    else:
        print(i)
        
try:
    x = 32/0
except ZeroDivisionError:
    pass
print("program devam ediyor...")

# TARİH YAZDIRMA

import datetime
a=datetime.datetime.now()
print(a)

# EKRANDAN SAYI OKUMAK

a = input("please enter the number: ")
a = int(a)
print(a)

# YAŞ HESAPLAMA

today = int(input("what is datetime: "))
birthday = int(input("what is your birthday"))
age= today-birthday
print("your age is :",age)

# İŞÇİ PROBLEMİ

employee = int(input("are there how many employee :"))
power = int(input("what is employee power 1-10 :"))
reelpower = (power*0.5)*employee
workdays = int(input("how many days will workers work:"))
worktime = int(workdays*8)
finishtime = int(worktime//reelpower)
print("The job will finish" ,finishtime, "after days")


# ASAL SAYI BULMA
result=[]
for i in range(1,100):
    for b in range(2,i):
         if(i%b==0):
             break
    else:
        result.append(i)
print(result)

# DEFINING FUNCTIONS
number = int(input("please enter the any number"))
def f(number):
    return number+10

name = input("please enter your name ")
def hello(name):
    print("hello " + str(name))
hello(name)

# FİBONACCİ 

def fib(n):
    a,b = 0,1
    while a<n:
        print(a)
        a,b=b,a+b    

# FACTORIAL

def facto(n):
    if(n==0):
        return 1
    return n-facto(n-1)

print(facto(5))


# DEFAULT PARAMETR

def g(x,y=3):
    return x % 5*y
print(g(2,5))
    
    
# ARGUMENT LIST

def topla(a,b):
    return a+b
result = topla(3,4)
print(result)


# DYNAMIC ARGUMENT LIST

def toplam(*args):
    return sum(args)
result= toplam(1,2,3,4,5)
print(result)

    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
