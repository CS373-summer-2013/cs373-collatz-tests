#!/usr/bin/env python

# -------------------------------
# projects/collatz/TestCollatz.py
# Copyright (C) 2013
# Glenn P. Downing
# -------------------------------

"""
To test the program:
	% python TestCollatz.py >& TestCollatz.py.out
	% chmod ugo+x TestCollatz.py
	% TestCollatz.py >& TestCollatz.py.out
"""

# -------
# imports
# -------

import StringIO
import unittest

from Collatz import collatz_read, collatz_cycle, collatz_eval, collatz_print, collatz_solve

# -----------
# TestCollatz
# -----------

class TestCollatz (unittest.TestCase) :
	# ----
	# read
	# ----

	def test_read_1 (self) :
		r = StringIO.StringIO("1 10\n")
		a = [0, 0]
		b = collatz_read(r, a)
		self.assert_(b    == True)
		self.assert_(a[0] ==  1)
		self.assert_(a[1] == 10)

	def test_read_2 (self) :
		r = StringIO.StringIO("10 30\n")
		a = [0, 0]
		b = collatz_read(r, a)
		self.assert_(b    == True)
		self.assert_(a[0] ==  10)
		self.assert_(a[1] == 30)

	def test_read_3 (self) :
		r = StringIO.StringIO("30 90\n")
		a = [0, 0]
		b = collatz_read(r, a)
		self.assert_(b    == True)
		self.assert_(a[0] == 30)
		self.assert_(a[1] == 90)

	def test_read_4 (self) :
		r = StringIO.StringIO("90 150\n")
		a = [0, 0]
		b = collatz_read(r, a)
		self.assert_(b    == True)
		self.assert_(a[0] == 90)
		self.assert_(a[1] == 150)

	def test_read_5 (self) :
		r = StringIO.StringIO("150 450\n")
		a = [0, 0]
		b = collatz_read(r, a)
		self.assert_(b    == True)
		self.assert_(a[0] == 150)
		self.assert_(a[1] == 450)

	# ----
	# cycle
	# ----

	def test_cycle_1 (self) :
		v = collatz_cycle(1)
		self.assert_(v == 1)

	def test_cycle_2 (self) :
		v = collatz_cycle(100)
		self.assert_(v == 26)

	def test_cycle_3 (self) :
		v = collatz_cycle(250)
		self.assert_(v == 110)

	def test_cycle_4 (self) :
		v = collatz_cycle(1233)
		self.assert_(v == 133)

	def test_cycle_5 (self) :
		v = collatz_cycle(999999)
		self.assert_(v == 259)

	def test_cycle_6 (self) :
		v = collatz_cycle(935917)
		self.assert_(v == 171)

	def test_cycle_7 (self) :
		v = collatz_cycle(987342)
		self.assert_(v == 127)

	def test_cycle_8 (self) :
		v = collatz_cycle(532097)
		self.assert_(v == 196)

	# ----
	# eval
	# ----

	def test_eval_1 (self) :
		v = collatz_eval(1, 10)
		self.assert_(v == 20)

	def test_eval_2 (self) :
		v = collatz_eval(100, 200)
		self.assert_(v == 125)

	def test_eval_3 (self) :
		v = collatz_eval(201, 210)
		self.assert_(v == 89)

	def test_eval_4 (self) :
		v = collatz_eval(900, 1000)
		self.assert_(v == 174)

	def test_eval_5 (self) :
		v = collatz_eval(1, 1000000)
		self.assert_(v == 525)

	def test_eval_6 (self) :
		v = collatz_eval(398475, 3456)
		self.assert_(v == 443)

	def test_eval_7 (self) :
		v = collatz_eval(2345, 9825)
		self.assert_(v == 262)

	def test_eval_8 (self) :
		v = collatz_eval(12, 24)
		self.assert_(v == 21)

	# -----
	# print
	# -----

	def test_print_1 (self) :
		w = StringIO.StringIO()
		collatz_print(w, 1, 10, 20)
		self.assert_(w.getvalue() == "1 10 20\n")

	def test_print_2 (self) :
		w = StringIO.StringIO()
		collatz_print(w, 1233, 1233, 133)
		self.assert_(w.getvalue() == "1233 1233 133\n")

	def test_print_3 (self) :
		w = StringIO.StringIO()
		collatz_print(w, 3333, 3333, 31)
		self.assert_(w.getvalue() == "3333 3333 31\n")

	def test_print_4 (self) :
		w = StringIO.StringIO()
		collatz_print(w, 1990, 2013, 144)
		self.assert_(w.getvalue() == "1990 2013 144\n")

	def test_print_5 (self) :
		w = StringIO.StringIO()
		collatz_print(w, 12, 16, 18)
		self.assert_(w.getvalue() == "12 16 18\n")

	# -----
	# solve
	# -----

	def test_solve_1 (self) :
		r = StringIO.StringIO("1 10\n100 200\n201 210\n900 1000\n")
		w = StringIO.StringIO()
		collatz_solve(r, w)
		self.assert_(w.getvalue() == "1 10 20\n100 200 125\n201 210 89\n900 1000 174\n")

	def test_solve_2 (self) :
		r = StringIO.StringIO("1 999999\n1 1 1\n999999 999999\n510303 338642\n")
		w = StringIO.StringIO()
		collatz_solve(r, w)
		self.assert_(w.getvalue() == "1 999999 525\n1 1 1\n999999 999999 259\n510303 338642 449\n")

	def test_solve_3 (self) :
		r = StringIO.StringIO("86453 614942\n209450 773981\n315679 685926\n376602 770865\n")
		w = StringIO.StringIO()
		collatz_solve(r, w)
		self.assert_(w.getvalue() == "86453 614942 470\n209450 773981 509\n315679 685926 509\n376602 770865 509\n")

	def test_solve_4 (self) :
		r = StringIO.StringIO("818227 948722\n333295 437088\n175758 925482\n119962 333170\n")
		w = StringIO.StringIO()
		collatz_solve(r, w)
		self.assert_(w.getvalue() == "818227 948722 525\n333295 437088 449\n175758 925482 525\n119962 333170 443\n")

	def test_solve_5 (self) :
		r = StringIO.StringIO("370708 676199\n80214 187936\n648584 712970\n653634 676890\n")
		w = StringIO.StringIO()
		collatz_solve(r, w)
		self.assert_(w.getvalue() == "370708 676199 509\n80214 187936 383\n648584 712970 504\n653634 676890 442\n")

# ----
# main
# ----

print "TestCollatz.py"
unittest.main()
print "Done."