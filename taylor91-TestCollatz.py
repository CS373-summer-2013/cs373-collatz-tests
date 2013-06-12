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

from Collatz import collatz_read, collatz_eval, collatz_print, collatz_solve, cycle_length

# -----------
# TestCollatz
# -----------
class TestCollatz (unittest.TestCase) :

	# ----
	# read
	# ----

	def test_read (self) :
		r = StringIO.StringIO("1 10\n")
		a = [0, 0]
		b = collatz_read(r, a)
		self.assert_(b    == True)
		self.assert_(a[0] ==  1)
		self.assert_(a[1] == 10)

	def test_read_2 (self) :
		r = StringIO.StringIO("10 1\n")
		a = [0, 0]
		b = collatz_read(r, a)
		self.assert_(b == True)
		self.assert_(a[0] == 10)
		self.assert_(a[1] == 1)

	def test_read_3 (self) :
		r = StringIO.StringIO("5 5\n")
		a = [0, 0]
		b = collatz_read(r, a)
		self.assert_(b == True)
		self.assert_(a[0] == 5)
		self.assert_(a[1] == 5)

	def test_read_4 (self) :
		r = StringIO.StringIO("")
		a = [0, 0]
		b = collatz_read(r, a)
		self.assert_(b == False)


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
		v = collatz_eval(1, 5)
		self.assert_(v == 8)

	def test_eval_6 (self) :
		v = collatz_eval(1, 1)
		self.assert_(v == 1)

	def test_eval_7 (self) :
		v = collatz_eval(5, 5)
		self.assert_(v == 6)

	# -----
	# print
	# -----
	def test_print (self) :
		w = StringIO.StringIO()
		collatz_print(w, 1, 10, 20)
		self.assert_(w.getvalue() == "1 10 20\n")

	def test_print_2 (self) :
		w = StringIO.StringIO()
		collatz_print(w, 10, 1, 20)
		self.assert_(w.getvalue() == "10 1 20\n")

	def test_print_3 (self) :
		w = StringIO.StringIO()
		collatz_print(w, 5, 5, 0)
		self.assert_(w.getvalue() == "5 5 0\n")

	# -----
	# solve
	# -----
	def test_solve (self) :
		r = StringIO.StringIO("1 10\n100 200\n201 210\n900 1000\n")
		w = StringIO.StringIO()
		collatz_solve(r, w)
		self.assert_(w.getvalue() == "1 10 20\n100 200 125\n201 210 89\n900 1000 174\n")

	def test_solve_2 (self) :
		r = StringIO.StringIO("1 1\n")
		w = StringIO.StringIO()
		collatz_solve(r, w)
		self.assert_(w.getvalue() == "1 1 1\n")

	def test_solve_3 (self) :
		r = StringIO.StringIO("2 2\n1 1\n1 3\n")
		w = StringIO.StringIO()
		collatz_solve(r, w)
		self.assert_(w.getvalue() == "2 2 2\n1 1 1\n1 3 8\n")

	def test_solve_4 (self) :
		r = StringIO.StringIO("1 3\n3 1\n")
		w = StringIO.StringIO()
		collatz_solve(r, w)
		self.assert_(w.getvalue() == "1 3 8\n3 1 8\n")

	# ------------
	# cycle_length
	# ------------
	def test_cycle_length (self) :
		v = cycle_length(1)
		self.assert_(v == 1)

	def test_cycle_length_2 (self) :
		v = cycle_length(2)
		self.assert_(v == 2)

	def test_cycle_length_3 (self) :
		v = cycle_length(5)
		self.assert_(v == 6)

	def test_cycle_length_4 (self) :
		v = cycle_length(10)
		self.assert_(v == 7)

# ----
# main
# ----
print "TestCollatz.py"
unittest.main()
print "Done."
