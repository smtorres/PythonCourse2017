import csv

#Open a file stream and create a CSV writer object
f = open('test.csv', 'wb')
my_writer = csv.writer(f)

for i in range(1, 100):
  my_writer.writerow([i, i-1])
   
f.flush()
f.close()

#The correct way!
with open('test1.csv', 'wb') as f:
  my_writer = csv.writer(f)
  for i in range(1, 100):
    my_writer.writerow([i, i-1])
    
#How about with field names
with open('test_with_fields.csv', 'wb') as f:
  my_writer = csv.DictWriter(f, fieldnames=("A", "B"))
  my_writer.writeheader()
  for i in range(1, 100):
    my_writer.writerow({"B":i, "A":i-1})
    
    

#Now lets read some things
with open('test.csv', 'rb') as f:
  print "Reading test1.csv"
  my_reader = csv.reader(f)
  for row in my_reader:
    print row

#Now lets read some things with field names
with open('test_with_fields.csv', 'rb') as f:
  print "\nReading test_with_fields.csv"
  my_reader = csv.DictReader(f)
  for row in my_reader:
    print row

##### You can also use w+, r+

# Copyright (c) 2014 Matt Dickenson
# 
# Permission is hereby granted, free of charge, to any person obtaining a copy
# of this software and associated documentation files (the "Software"), to deal
# in the Software without restriction, including without limitation the rights
# to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
# copies of the Software, and to permit persons to whom the Software is
# furnished to do so, subject to the following conditions:
# 
# The above copyright notice and this permission notice shall be included in all
# copies or substantial portions of the Software.
# 
# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
# IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
# FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
# AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
# LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
# OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
# SOFTWARE.