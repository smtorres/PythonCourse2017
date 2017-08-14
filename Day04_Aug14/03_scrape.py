#Install beautiful soup
#$ easy_install beautifulsoup4
#$ easy_install pip
#$ sudo pip install beautifulsoup4

from bs4 import BeautifulSoup
import urllib2 
import random
import time
import os

# Open a web page
web_address='https://polisci.wustl.edu/faculty/specialization'
web_page = urllib2.urlopen(web_address)

# Parse it
soup = BeautifulSoup(web_page.read())
soup.prettify()

# Find all cases of a certain tag
soup.find_all('h3')
soup.find_all('a')

# Get the script of a certain tag
mytitle=soup.find_all('h3')[0]
mytitle.text

# Get the attributes
my_a_tag=soup.find_all('a')[2]
my_a_tag.attrs #Gives a dictionary with the attributes
my_a_tag.attrs.keys()
my_a_tag['alt']

# Refine search by using attributes
soup.find_all('a',{'alt':"Washington University in St. Louis" })

# There may be tags within tags
mysection=soup.find_all('div')[0]
mysection.a #Gives the 'a' tag within the 'div' tag
mysection.find_all('a') #Gives the list of all 'a' tags within the 'div' tag

# Creating a tree of objects

mysection.contents #Gives a list of all children
mysection.children #Creates an iterator for children

for child in mysection.children:
	print child

mysection.descendants #Creates an iterator for children, grandchildren, etc.

# Other methods to check family:
# parent
# parents
# next_siblings
# previous_siblings

# Beautiful Soup documentation
# http://www.crummy.com/software/BeautifulSoup/bs4/doc/

# Function to save a web page

def download_page(address,path,filename,wait=5):
	time.sleep(random.uniform(0,wait))
	page = urllib2.urlopen(address)
	page_content = page.read()
	if os.path.exists(path+filename)==False:
		with open(path+filename, 'w') as p_html:
			p_html.write(page_content)
	else:
		print "Can't overwrite file" + filename

#You can also parse a page that is saved on your computer
with open('html_test.html') as f:
  #We can read files in chunks
  myfile = f.read()
  
soup = BeautifulSoup(myfile)
soup.prettify()


