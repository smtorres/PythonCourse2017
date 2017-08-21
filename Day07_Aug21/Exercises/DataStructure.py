###				Tuple				###

#Tuples are immutable

my_tuple=(1,'b',3,'d',5,'b')

my_tuple[0] #Gives the element with index number 0
my_tuple.index('b') #Gives the index of 'b' - only the first occurence!
my_tuple.count('b') #Gives the number of times 'b' occurs
###				List				###

my_list = range(0,10)
my_square_list = [i**2 for i in range(0,10)]

my_square_list=[]
for i in range(0,10):
	my_square_list.append(i**2)

my_square_list = map((lambda x: x**2), my_list)

zip(my_list,my_square_list)

#.index and .count methods work the same as above

x = [3,6,1,2,8,3,5,7]

x.reverse() #Don't forget to add the parentheses!
x[2]
x.sort() #Don't forget to add the parentheses!
x.append(10)
x.extend(my_square_list)
x.insert(1,'+')
x.remove('+')  #Removes the first occurence '+'
x.remove(3)

print x
# enumerate function

import string

y=[3,1,2,5,2]
enumerate(y)
list(enumerate(y))

letters=list(string.lowercase)

for item in enumerate(letters):
	print item
	
for number,letter in enumerate(letters):
	print "%s is the letter with index %s" %(letter,number)
	
my_list=[1,2,1,3,1]

def all_indices(mylist,myitem):
	indices=[]
	for index, item in enumerate(mylist):
		if item==myitem:
			indices.append(index)
	return indices
	
	
###				Dictionary				###

mydict = dict(zip(letters,range(1,27)))

mydict['a']
mydict.keys() #Don't expect order!
mydict.values() 
mydict.items()

for key,value in mydict.items():
	if value==1:
		print key

for letter,number in mydict.items():
	print "%s is the letter number %s" %(letter,number)

newletter = {'A':27}
mydict.update(newletter)

new_a_value = {'a':'first'}
mydict.update(new_a_value)
mydict['z'] = 'last'

###				Stack				###

# LIFO - Last in first out		

mystack=letters
mystack.pop()

###				Queue				###

# FIFO - First in first out		

from collections import deque

letters[0:10]
myqueue=deque(letters[0:10])
myqueue.append('k')
myqueue.popleft()

###				Tree				###

#root, nodes, leaves, branching

class Node():
	def __init__(self,value=None,subnode=(None,None)):
		self.value=value
		self.subnode=subnode
		self.left=subnode[0]
		self.right=subnode[1]
		
	def __repr__(self):
		return "Node object with value %s" %(self.value)
		
	def __str__(self):
		if self.left:
			return "Node value: %s \n left child: \n %s \n right child: \n %s" %(self.value,self.left,self.right)
		else: return "Node value: %s" %self.value
# repr vs str
# x=4
# repr(x)
# '4'
# str(x)
# '4'
# y='stringy'
# repr(y)
# "'stringy'"
# str(y)
# 'stringy'
# Evaluate!
# y = 'a string'
# repr(y)
# "'a string'"
# y2=eval(repr(y))
# y==y2
# True
# y2=eval(str(y))

node2a=Node(2)
node2b=Node(3)
node1=Node(1,(node2a,node2b))


class Node():
	def __init__(self,value=None):
		self.value=value
		self.parent=None
		self.children=[None,None]			
		
	def __repr__(self):
		return "Node object with value %s" %(self.value)
		
	def __str__(self):
		if self.children !=(None,None):
			return "Node value: %s \n left child: \n %s \n right child: \n %s" %(self.value,self.children[0],self.children[1])
		else: return "Node value: %s" %self.value	
	
class Tree():
	def __init__(self,root=None):
		self.root=root
		self.branches=[[root]]
		
	def add_branch(self,node,children):
		node.children[0]=children[0]
		node.children[1]=children[1]
		for branch in self.branches:
			if branch[-1]==node:
				newbranch=branch + [children[0]]
				newbranch2=branch + [children[1]]
				self.branches.append(newbranch)
				self.branches.append(newbranch2)
				self.branches.remove(branch)

node1=Node(1)
node2=Node(2)
node3=Node(3)
node4=Node(4)
node5=Node(5)

mytree=Tree(node1)
mytree.branches
mytree.add_branch(node1,[node2,node3])
mytree.add_branch(node2,[node4,node5])




