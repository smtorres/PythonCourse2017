def print_int(int):
	print 'Here is an integer: %s' %int

print_int(1)
print_int('b')


####################################
def random_product(lower, upper):
	random1
	random2
	return random1 * random2

print random_product(0,1)

####################################
import random
def random_product(lower, upper):
	random1=uniform(lower, upper)
	random2=uniform(lower, upper)
	return random1 * random2

print random_product(0,1)

####################################
import random
def random_product(lower, upper):
	random1=random.uniform(lower, upper)
	random2=random.uniform(lower, upper)
	return random1 * random2

print random_product(0,1)

####################################
class human(object):
	latin_name = 'homo sapien'

me = human()

####################################
class human(object):
	latin_name = 'homo sapien'
	def __init__(self, age, sex, name):
		self.age = age
		self.sex = sex
		self.name = name

me = human()
####
me = human(29, 'Female', "Michelle")
me.name
me.age

####################################
class human(object):
	latin_name = 'homo sapien'
	def __init__(self, age, sex, name=None):
		self.age = age
		self.sex = sex
		self.name = name

	def speak(self, words):
		return words

	def introduce(self):
		if self.sex=='Female': return self.speak("Hello. I'm Ms. %s" % self.name)
		elif self.sex=='Male': return self.speak("Hello. I'm Mr. %s" % self.name)
		else: return self.speak("Hello. I'm %s" % self.name)

dir(human)
me = human(29, 'Female', "Michelle")
me.speak('Hola')
me.introduce()

class human(object):
	latin_name = 'homo sapien'
	def __init__(self, age, sex, name=None):
		self.age = age
		self.sex = sex
		self.name = name

	def speak(self, words):
		return words

	def introduce(self):
		if self.sex=='Female': return self.speak("Hello. I'm Ms. %s" % self.name)
		elif self.sex=='Male': return self.speak("Hello. I'm Mr. %s" % self.name)
		else: return self.speak("Hello. I'm %s" % self.name)

	def __str__(self):
		return 'Human: %d year-old %s.' % (self.age, self.sex)


me = human(29, 'Female', "Michelle")
print me



############ A MORE COMPLICATED EXAMPLE

# - Add a student's name to the roster for a grade
# - Get a list of all students enrolled in a grade
# - Get a sorted list of all students in all grades.
# 
# Note that all our students only have one name.
# (It's a small town, what do you want?)

class school():
    def __init__(self, school_name): #initialize instance of class School with parameter name
        self.school_name = school_name #user must put name, no default
        self.db = {} #initialize empty dictionary to store kids and grades
        
    def add(self, name, student_grade): #add a kid to a grade in instance of School
        if student_grade in self.db: #need to check if the key for the grade already exists, otherwise assigning it will return error
            self.db[student_grade].add(name) #add kid to the set of kids within the dictionary
        else: self.db[student_grade] = {name} #if the key doesn't exist, create it and put kid in

    def sort(self): #sorts kids alphabetically and returns them in tuples (because they are immutable)
        sorted_students={} #sets up empty dictionary to store sorted tuples
        for key in self.db.keys(): #loop through each key
            sorted_students[key] = tuple(sorted(self.db[key])) #add dictionary entry with key being the grade and the entry the tuple of kids
        return sorted_students

    def grade(self, check_grade):
        if check_grade not in self.db: return None #if the key doesn't exist, there are no kids in that grade: return None
        return self.db[check_grade] #if None wasn't returned above, return elements within dictionary, or kids in grade

    def __str__(self): #print function will display the school name on one line, and sorted kids on other line
        return "%s\n%s" %(self.school_name, self.sort())

    def __setitem__(self, grade, name):
      return self.add(name, grade)


#################### INHERITANCES

class Parent():
  def __init__(self, sex, firstname, lastname):
    self.sex = sex
    self.firstname = firstname
    self.lastname = lastname
    self.kids = []

  def role(self):
    if self.sex == "Male":
      return "Father"
    else:
      return "Mother"

  def have_child(self, name):
    child = Child(name, self)
    print self.firstname + " is having a child named " + child.name()
    print "They will make a very good " + self.role()
    self.kids.append(child)
    return child

  def list_children(self):
    for kid in self.kids:
      print "I am the " + self.role() + " of " + kid.name()

class Child():
  def __init__(self, firstname, parent):
    self.parent = parent 
    self.lastname = parent.lastname
    self.firstname = firstname

  def set_name(self, new_first_name, new_last_name):
    self.firstname = new_first_name
    self.lastname = new_last_name

  def name(self):
    return "%s %s" % (self.firstname, self.lastname)

  def introduce(self):
    return "Hi I'm " + self.name()

  def siblings(self):
    for kid in self.parent.kids:
      if kid != self:
        print "I have a sibling named " + kid.name()
        


mom = Parent("Female", "Jane", "Smith")
mom.list_children()
jill = mom.have_child("Jill")
jill.set_name("Jillian", "Jones")
print jill.introduce()
print jill == mom.kids[0]
jack = mom.have_child("Jack")
print jack.introduce()
jack.parent.kids[0].parent.list_children()
jack.siblings()


############## POLYMORPHISM

class Animal(object):
  living="Yes!"
  def __init__(self, name):    # Constructor of the class
      self.name = name
      
  def talk(self):              # Abstract method, defined by convention only
  	raise NotImplementedError("Subclass must implement abstract method")
  	 
class Cat(Animal):
  def talk(self):
    return self.meow()
    
  def meow(self):
    return 'Meow!'
 
class Dog(Animal):
  def talk(self):
    return self.bark()
  
  def bark(self):
    return 'Woof! Woof!'
      
class Fish(Animal):
  
  def swim(self):
    pass
  
  def __str__(self):
    return "I am a fish!"
      
animals = [Cat('Foo'),Dog('Bar'),Fish('nemo')]
 
for animal in animals:
    print animal.name + ': ' + animal.talk()
  
 f = Fish("foo")
 print "Hi, " + str(f)

