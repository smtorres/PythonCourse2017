# setup
items = range(1, 5)

def sqr(x): return x**2

def cub(x): return x**3

# mapping
mylist=[]
for x in items: 
	mylist.append(sqr(x))
	
mylist=map(sqr, items)
mylist=map((lambda x: x **2), items)

funcs = [sqr, cub]
for i in items:
    value = map(lambda x: x(i), funcs)
    print value

# reducing and filtering
range(-5, 5)
filter((lambda x: x < 0), range(-5,5))

from functools import reduce
reduce( (lambda x, y: x * y), items )

L = ['Testing ', 'shows ', 'the ', 'presence', ', ','not ', 'the ', 'absence ', 'of ', 'bugs']
reduce( (lambda x,y:x+y), L)

reduce( (lambda x,y:x+y), map(len, L))

reduce( (lambda x,y:x+y), map(sqr, items))