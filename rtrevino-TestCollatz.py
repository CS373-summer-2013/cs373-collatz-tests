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

from Collatz import collatz_read, collatz_eval, collatz_print, collatz_solve

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

    # Unit Test Cases
	def test_read_1(self) :
	    r = StringIO.StringIO("1 100 \n")
	    a = [0, 0]
	    b = collatz_read(r, a)
	    self.assert_(b == True)
	    self.assert_(a[0] == 1)
	    self.assert_(b[1] == 100)

	def test_read_2(self) :
	    r = StringIO.StringIO("100 1000 \n")
	    a = [0, 0]
	    b = collatz_read(r, a)
	    self.assert_(b == True)
	    self.assert_(a[0] == 100)
	    self.assert_(b[1] == 1000)

	def test_read_3(self) :
	    r = StringIO.StringIO("1000 2000 \n")
	    a = [0, 0]
	    b = collatz_read(r, a)
	    self.assert_(b == True)
	    self.assert_(a[0] == 1000)
	    self.assert_(b[1] == 2000)
	
	   

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

    # -----
    # print
    # -----

    def test_print (self) :
        w = StringIO.StringIO()
        collatz_print(w, 1, 10, 20)
        self.assert_(w.getvalue() == "1 10 20\n")

    # Unit Test Cases for collatz_print

    def test_print_1(self) :
	w = StringIO.StringIO()
	collatz_print(w, 100, 200, 125)
	self.assert_(w.getvalue() == "100 200 125\n")

    def test_print_2(self) :
	w = StringIO.StringIO()
	collatz_print(w, 201, 210, 89)
	self.assert_(w.getvalue() == "201 210 89\n")

    def test_print_3(self) :
	w = StringIO.StringIO()
	collatz_print(w, 900, 1000, 174)
	self.assert_(w.getvalue() == "900 1000 174\n")


    # -----
    # solve
    # -----

    def test_solve (self) :
        r = StringIO.StringIO("1 10\n100 200\n201 210\n900 1000\n")
        w = StringIO.StringIO()
        collatz_solve(r, w)
        self.assert_(w.getvalue() == "1 10 20\n100 200 125\n201 210 89\n900 1000 174\n")

    # Unit Test Cases for test_solve

     def test_solve_1 (self) :
        r = StringIO.StringIO("100 100\n")
        w = StringIO.StringIO()
        collatz_solve(r, w)
        self.assert_(w.getvalue() == "100 100 26\n")

    def test_solve_2 (self) :
        r = StringIO.StringIO("1 20\n")
        w = StringIO.StringIO()
        collatz_solve(r, w)
        self.assert_(w.getvalue() == "1 20 21\n")

    def test_solve_3 (self) :
        r = StringIO.StringIO("100 225")
        w = StringIO.StringIO()
        collatz_solve(r, w)
        self.assert_(w.getvalue() == "100 225 128\n")

# ----
# main
# ----

print "TestCollatz.py"
unittest.main()
print "Done."
