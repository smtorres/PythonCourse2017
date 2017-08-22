import re

mytext = r'Hello! Nice to meet you. I am a 5th year student at WashU, in St. Louis.Yes, 5.\n How\'re you doing today?'
#re.findall and re.split
mytext2 = 'Hello world, Bonjour world!'

re.split(r'\d',mytext)
re.split(r'\d\.',mytext)

re.findall(r'[a-z]',mytext)
re.findall(r'[a-z]+',mytext) #space!

#re.compile

pattern = re.compile(r'[a-z]+') #Create a regex object

pattern.findall(mytext2)
pattern.split(mytext2)


#re.MULTILINE

mytext='bin\nban\ncan'

pattern = re.compile(r'^b\w*')
pattern.findall(mytext)

pattern = re.compile(r'^b\w*',re.MULTILINE)
pattern.findall(mytext)

pattern = re.compile(r'[^b]\w*')
pattern.findall(mytext)

re.findall(r'^b\w*',mytext,re.MULTILINE)

#re.match and re.search

mytext = 'a1b2c3D'

x = re.match(r'\d',mytext) #matches the pattern at the beginning of the string
y = re.search(r'\d',mytext) #looks for the pattern anywhere in the string
x.group(0)
y.group(0)


#math and search

pattern = re.compile(r'\d')

pattern.match(mytext) #similar to above
pattern.match(mytext,1) #matches the pattern in the position 1

pattern.search(mytext) #similar to above
pattern.search(mytext, 1) #looks for the pattern in the position 1

pattern = re.compile('r[A-Z]')
pattern.search(mytext,1,6) #looks for the pattern between positions 1 and 5

#create groups

mytext = '12 twelve'

pattern = re.compile(r'(\d*)\s(\w*)')
mysearch=pattern.search(mytext)
mysearch.groups() #list of all groups
mysearch.group(0) #the complete match
mysearch.group(1) #the first group
mysearch.group(2) #the second group

pattern = re.compile(r'(?P<number>\d*)\s(?P<name>\w*)') #similar to regular parentheses
mysearch=pattern.search(mytext)
mysearch.groups()
mysearch.groupdict()

mytext = '12 24'
pattern = re.compile(r'(\d*)')
pattern.search(mytext).groups()
pattern.search(mytext).group(0)
pattern.search(mytext).group(1)


