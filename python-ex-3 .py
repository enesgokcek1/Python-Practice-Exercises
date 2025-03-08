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
# lambda yapısı yazdığımız yapı içinde tek kullanımlık bir değer ataması. Eğer dışına yazarsak side effect yaratabilir.

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

del(k[1])
print(k)



























