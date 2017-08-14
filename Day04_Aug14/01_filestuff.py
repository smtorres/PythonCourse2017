import sys

#The cleanest way to handle files (gracefully handles exceptions)
with open('readfile.txt') as f:
  #We can read files in chunks
  the_whole_thing = f.read()
  print "The Whole Thing\n***\n{0}".format(the_whole_thing)

  #We can read files line by line
  print "\nLooping over lines\n****\n"
  f.seek(0)
  lines = f.readlines()
  for l in lines:
    print "{0}".format(l)
    
  #More efficiently we can loop over the file object (i.e. we don't need the variable lines)
  print "\nLooping over the file object\n***\n"
  f.seek(0)
  for l in f:
    print "{0}".format(l)
    
  #You can also go byte by byte (don't do this)
  print "\nByte by Byte\n********************\n"
  f.seek(0)
  next_byte = f.read(1)
  while next_byte != "":
    sys.stdout.write(next_byte)
    next_byte = f.read(1)
    
# We can also manually open and close files, now we need to handle exceptions and closing files
f =  open('readfile.txt')
print "\nManually Opened File\n********************\n"
print f.read()
f.close()

#Writing files is easy, open command takes r, w, a, plus some others
with open('writefile.txt', 'w') as f:
  #wipes the file clean and opens it
  f.write("Hi guys.")
  f.write("Does this go on the second line?")
  f.writelines(['a\n', 'b\n', 'c\n'])
  # f.flush() # If using the file object interactively you may need to flush the buffer

with open('writefile.txt', 'a') as f:
  #just tacks some things on the end
  f.write("\nI got appended!")
  f.flush()

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
