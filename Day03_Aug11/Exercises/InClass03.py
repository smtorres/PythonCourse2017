raise Exception
print "I raised an exception!"

####################################
try:
	print b
except NameError:
	print "oops name error"	
except:
	pass
finally:
	print "Yes! I did it!"

b='Can I do it?'

try:
    print b
except NameError:
    print "oops name error" 
except:
    pass
finally:
    print "Yes! I did it!"

####################################
	
for i in range(1,10):
	if i==5:
		print "I found five!"
		continue
		print "Here is five!"
	else:
		print i
else:
	print "I went through all iterations!"

# Now comment out the continue

####################################
def Rename(entry):
    try:
     	if entry%1==0:
    		entry = str(entry)
    		if entry[-2] == '1':
    			return "%sth" %(entry)
     		elif entry[-1] == '1':
    			return "%sst" %(entry)
    		elif entry[-1] == '2':
    			return "%snd" %(entry)
    		elif entry[-1] == '3':
    			return "%srd" %(entry)  
    		else:
    			return  "%sth" %(entry)	
    	else:
    		return "Please do not enter decimal places." 	
    except:
    	return "Please enter an integer."
    finally: 
    	print "This is a function."

entry = 1
entry%1==0 # True
entry = str(entry)
if entry[-2] == '1':
    print "%sth" %(entry)
elif entry[-1] == '1':
    print "%sst" %(entry)
elif entry[-1] == '2':
    print "%snd" %(entry)
elif entry[-1] == '3':
    print "%srd" %(entry)  
else:
    print  "%sth" %(entry)

#IndexError: string index out of range

####################################
def print_integer(integer):
    return "Here is my integer: " + str(integer)

print_integer(2)
print_integer('22')
print_integer('banana')

def print_integer(integer):
    try:
        int(integer)
    except ValueError:
        print "Put in a number."
    else:
        print "Here is my integer: " + str(integer)

print_integer(2)
print_integer('22')
print_integer('banana')


def print_integer(integer):
    if type(integer)==int:
        print "Here is my integer: " + str(integer)
    else:
        raise Exception, "This is not an integer"
print_integer('22')

def print_integer(integer):
    if type(integer)==int: 
        return "Here is my integer: " + str(integer)
    else:
        raise TypeError, "Enter an integer!"
print_integer('22')
                
def print_integer(integer):
    try:
        if integer %1==0:
            return "Here is my integer: " + str(integer)
        else:
            return "This has decimals!"
    except:
        raise TypeError, "Enter a number!"
print_integer('22')
        
def print_integer(integer):
    try:
        if integer%1==0:
            print "Congratulations! You entered an integer!"
        else:
            raise
    except:
        raise TypeError, "This is not an integer!"
    else:
        return "Here is my integer: " + str(integer)
print_integer('22')
print_integer(22)



def print_integer(integer):
    try:
        if integer%1==0:
            print "Here is my integer: " + str(integer)
        else:
            raise Exception
    except TypeError:
        print "Enter a number!"
    except:
        print "Integers can't have decimals!"

                
def print_integer(integer):
    try:
        if integer %1==0:
            print "Congratulations! You entered an integer!"
        else:
            raise Exception
    except TypeError:
        raise TypeError, "Enter a number!"
    except:
        raise TypeError, "Integers can't have decimals!"    
    else:
        return "Here is my integer: " + str(integer)

        
#Create your own exception      
class CustomException(Exception): 
  def __init__(self, value):
    self.value = value
  def __str__(self):
    return self.value
    
    
def print_integer(integer):
    try:
        if integer %1==0:
            print "Congratulations! You entered an integer!"
        else:
            raise CustomException(integer%1)
    except CustomException as e:
        raise TypeError, "Your number has a decimal: %.2f" %e.value
    except TypeError:
#        pass
        raise TypeError, "Enter a number!"
    else:
        return "Here is my integer: " + str(integer)
    finally:
        print "I'm done!"


################################
import unittest

class TestStringMethods(unittest.TestCase):

    def test_upper(self):
        self.assertEqual('foo'.upper(), 'FOO')

    def test_isupper(self):
        self.assertTrue('FOO'.isupper())
        self.assertFalse('Foo'.isupper())

    def test_split(self):
        s = 'hello world'
        self.assertEqual(s.split(), ['hello', 'world'])
        # check that s.split fails when the separator is not a string
        with self.assertRaises(TypeError):
            s.split(2)

if __name__ == '__main__':
    unittest.main()
###############
for n in range(2, 10):
    for x in range(2, n):
        if n % x == 0:
            print(n, 'equals', x, '*', n//x)
            break
        else:
            print(n, 'is a prime number')

