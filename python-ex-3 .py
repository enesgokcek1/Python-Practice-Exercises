# MORE ON LISTS
l=[1,2,3,4,111]
print(l)

# Add an item to the end of the list.
l.append(55)
print(l)

# Insert an item at a given position.
l.insert(2,111) 
print(l)

# Remove the first item from the list whose value is equal to x.
l.remove(111)
print(l)

# Remove the item at the given position in the list, and return it
print(l.pop())
print(l)

# Returns the rank of the entered value
print(l.index(2))

# Return the number of times x appears in the list.
print(l.count(1))

# Sort the items of the list in place
l.append(44)
print(l)
l.sort()
print(l)

# Extend the list by appending all the items from the iterable. 
l2=[2,4,5]
l.extend(l2)
print(l)

# Remove all items from the list. Similar
# l.clear()
# print(l)

# Return a shallow copy of the list.
l=l2
l.append(600)
print(l)
print(l2)
# but..
l=l2.copy()
l.append(700)
print(l)
print(l2)


# STACK AND QUEUE

l2=[44,55,66]
l2.append(88)
print(l2.pop(0))
print(l2)

#  popleft: the first to arrive now leaves. 
# if you write popleft second time so the second to arrive will leaves
from collections import deque

l3 = deque([11,23,45])
print(l3)
l3.append(67)
print(l3.popleft())
print(l3)


# List Comprehensions :List comprehensions provide a concise way to create lists
# lambda yapısı yazdığımız yapı içinde tek kullanımlık bir değer atamasıdır. Eğer dışına yazarsak side effect yaratabilir.

l=[]

for x in range(1,11):
    l.append(x**2)

print(l)
print(x)

squares = list(map(lambda y: y**2, range(1,11)))
print(squares)
print(range(1,11))

def f(x):
    return x+5
l2=[2,8,3]
print(list(map(lambda x:x+5,l2)))

l3 = [x**2 for x in range(10)]
print(l3)

l4 = [(x,y,z) for x in [1,2,3] for y,z in [(1,2),(2,3),(3,4)] if x!=y ]
print(l4)

# (1,2,3,4) 
l5 = [(a,b,c,d) for a in [1] for b in [2] for c in [3] for d in [4]]
print(l5)

# (3,4,5,6) 
# (2,4,3,4) 
# (2,5,3,7) 


# LIST OF LIST

l=[1,2,3]
m = [[1,2,3],[3,4,5],l]
print(m)
l[1]=100
print(m)

k = [[[1,2,3],[2,3,4]],[1,2,3],[1,1,1]],[[1,1]]
print(k)

mt = [[row[i] for row in m] for i in range(3)]
print(mt)

# del(k[1])
# print(k)


# TUPLE AND IMMUTABLE

# l = [1,2,3]
# # This structure cannot be changed = immutable
# t = (1,2,3) 
# print(l,t)
# # t[2]=10
# print(t)

# x,y,z =t
# print(x,z)
# z=10
# print(t)
# t=(x,y,z)
# print(t)


# burada yapılan değişiklik tuple'a yapılmıyor. Tuple içindeki listeye yapılıyor!
v=([1,2,3],[3,2,1])
v[0][1]=100
print(v)

#  bu yapıda tuple dır ancak bu şekilde zorluk cıkarma paranteze al!
t2 =1,2,3
print(t2)


# KÜMELER(SET) CURLY BRACKET
# KÜMELERDE 1 ELEMAN 1 KEZ OLUR. BELİRLİ BİR SIRALAMASI YOKTUR
# SET BİR LİSTEYİ ALIP KÜMEYE ÇEVİRİR
k = {1,2,3,3,1,3,4,1,2,3} 
l=[1,2,3,3,4,1,1,2,2,4,1]
print(k)
print(l)
l1= set(l)
print(l1)

k4= set("enessalihgokcek")
k5= set("bilgisayarkavramlari")
print(k4)
print(k5)

# KÜMELER BİRLEŞİMİ = SET UNION
print(k4|k5)
# SET DIFFERENCE
print(k4-k5)
# KUME KESİŞİM
print(k4&k5)
# SYMMETRİC DIFFERENCE, iki yönlü küme farkı birleşimi 
print(k4^k5)


# Creating a dictionary
person = {
    "name": "John",
    "age": 29,
    "city": "New York"
}

# Accessing dictionary values by key
print(person["name"])  # Output: John
print(person["age"])   # Output: 30 

# Adding a new key-value pair
person["job"] = "Engineer"

# Modifying an existing value
person["age"] = 31

# Removing a key-value pair
del person["city"]

print(person)



# DICTIONARY EXAMPLE 2
employee = {
    "name": "usman",
    "age": 34,    
    "department": "data analyst"
    }
print(employee["name"])
print(employee["age"])
print(employee["department"])

employee["jobs"] = "software"
employee["gender"] = "men"
employee["age"] = 45
print(employee)
del employee["gender"]
print(employee)


# LOOPING TECHNİQUES
campingmaterial = {"tent": "decathlon", "axe": "fiskars"}
for t,a in campingmaterial.items():
    print(t,a)


# LOOPING TECHNIQUES EXAMPLE FOR DATA ANALYSIS*****

product_prices = {"apple": 3, "banana": 5, "orange": 4}
for product, price in product_prices.items():
    product_prices[product]=price*1.5
print(product_prices)


# Comparing Sequences and Other Types 
(1, 2, 3)              < (1, 2, 4)
[1, 2, 3]              < [1, 2, 4]
'ABC' < 'C' < 'Pascal' < 'Python'
(1, 2, 3, 4)           < (1, 2, 4)
(1, 2)                 < (1, 2, -1)
(1, 2, 3)             == (1.0, 2.0, 3.0)
(1, 2, ('aa', 'ab'))   < (1, 2, ('abc', 'a'), 4)


# DOSYALARI BİRLEŞTİRME KÜTÜPHANE YAPMA. import işlemi ile birden fazla kodu 
# tek çatı altında kütüphane formatı ile bir araya getirebiliriz

# Fibonacci numbers module

def fib(n):    # write Fibonacci series up to n
    a, b = 0, 1
    while a < n:
        print(a, end=' ')
        a, b = b, a+b
    print()

def fib2(n):   # return Fibonacci series up to n
    result = []
    a, b = 0, 1
    while a < n:
        result.append(a)
        a, b = b, a+b
    return result


# DOSYALAR

file = open ('bilgisayar.txt', 'w') # bilgisayar adlı dosyaya write et yaz
file.write('bilgisayar kavramlari\n')
file.close()

file= open("bilgisayar.txt", "r") #okumayı ifade eder
print(file.read())
file.close()


# Değişkenlerin geçerlilik alanı

def scope_test():
    def do_local():
        spam = "local spam"#local spam bu bloğun içinde geçerli

    def do_nonlocal():
        nonlocal spam
        spam = "nonlocal spam"#nonlocal bu genel fonks içinde geçerli

    def do_global():
        global spam
        spam = "global spam"#global ise tüm kodda tanımlı

    spam = "test spam"
    do_local()
    print("After local assignment:", spam)
    do_nonlocal()
    print("After nonlocal assignment:", spam)
    do_global()
    print("After global assignment:", spam)

scope_test()
print("In global scope:", spam)

# CLASS AND OBJECT

class car:
    speed= 0
    color="green"
    def speedUp(self):
        self.speed = self.speed + 1
x = car() 
x.speed = 100;
x.speedUp()
print("car speed", x.speed)
    
    


class car:
    speed= 0
    color="green"
    def speedUp(self):
        self.speed = self.speed + 1
x = car() 
x.speed = 100;
x.speedUp()
print("car speed", x.speed)
    
    




class car:
    speed= 0
    color="green"
    def speedUp(self):
        self.speed = self.speed + 1
x = car() 
x.speed = 100;
x.speedUp()
print("car speed", x.speed)
    
    














































