import unittest
import lab1_dc

class Testlab1_dcCode(unittest.TestCase):

	def setUp(self): 
		self.x2 = "10000"
		self.y2 = "10"
		self.y10 = "2"
		self.xplusy = 18
		self.xtimesy = 32

	# Correctness tests 

	# binarify
	def test_binarify_16(self):
		self.assertEqual(lab1_dc.binarify(16), "10000")

	def test_binarify_127(self):
		self.assertEqual(lab1_dc.binarify(127), "1111111")

	def test_binarify_0(self):
		self.assertEqual(lab1_dc.binarify(0), "0")

	def test_binarify_negative(self):
		self.assertEqual(lab1_dc.binarify(-16), "0")


	# int_to_base
	def test_int_to_base_2(self):
		self.assertEqual(lab1_dc.int_to_base(123, 2), lab1_dc.binarify(123))

	def test_int_to_base_3(self):
		self.assertEqual(lab1_dc.int_to_base(12, 3), "110")

	def test_int_to_base_10(self):
		self.assertEqual(lab1_dc.int_to_base(16, 10), "16")

	def test_int_to_base_0(self):
		self.assertEqual(lab1_dc.int_to_base(16, 0), "0")

	def test_int_to_base_negative(self):
		self.assertEqual(lab1_dc.int_to_base(-16, 2), "-10000")


	# base_to_int
	def test_base_to_int_16(self):
		self.assertEqual(lab1_dc.base_to_int("10000", 2), 16)

	def test_base_to_int_3(self):
		self.assertEqual(lab1_dc.base_to_int("110", 3), 12)

	def test_base_to_int_10(self):
		self.assertEqual(lab1_dc.base_to_int("16", 10), 16)

	def test_base_to_int_0(self):
		self.assertEqual(lab1_dc.base_to_int("123", 0), 0)

	def test_base_to_int_negative(self):
		self.assertEqual(lab1_dc.base_to_int("-10000", 2), -16)


	# flexibase methods
	def test_flexibase_add_base_2(self):
		self.assertEqual(lab1_dc.flexibase_add(self.x2, self.y2, 2, 2), self.xplusy)

	def test_flexibase_add_base_2_10(self):
		self.assertEqual(lab1_dc.flexibase_add(self.x2, self.y10, 2, 10), self.xplusy)

	def test_flexibase_multiply_base_2(self):
		self.assertEqual(lab1_dc.flexibase_multiply(self.x2, self.y2, 2, 2), self.xtimesy)

	def test_flexibase_multiply_base_10(self):
		self.assertEqual(lab1_dc.flexibase_multiply(self.x2, self.y10, 2, 10), self.xtimesy)


	# romanify 
	def test_romanify_3(self):
		self.assertEqual(lab1_dc.romanify(3), "III")

	def test_romanify_9(self):
		self.assertEqual(lab1_dc.romanify(9), "IX")

	def test_romanify_10(self):
		self.assertEqual(lab1_dc.romanify(10), "X")

	def test_romanify_49(self):
		self.assertEqual(lab1_dc.romanify(49), "XLIX")

	def test_romanify_99(self):
		self.assertEqual(lab1_dc.romanify(99), "XCIX")

	def test_romanify_3999(self):
		self.assertEqual(lab1_dc.romanify(3999), "MMMCMXCIX")


if __name__ == '__main__':
  unittest.main()
  
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

