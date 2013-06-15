#
#  mgt91-TestCollatz.py.py
#  
#
#  Created by Matt Thurner on 6/12/13.
#  Copyright (c) 2013 University of Texas at Austin. All rights reserved.
#


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
		
	# both values are 1
	def test_read_1 (self) :	
        r = StringIO.StringIO("1 1\n")
        a = [0, 0]
        b = collatz_read(r, a)
        self.assert_(b    == True)
        self.assert_(a[0] ==  1)
        self.assert_(a[1] ==  1)
		
	# values are presented in inverse fashion	
	def test_read_inverse (self) :	
		r = StringIO.StringIO("20 10\n")
        a = [0, 0]
        b = collatz_read(r, a)
        self.assert_(b    == True)
        self.assert_(a[0] == 20)
        self.assert_(a[1] == 10)

	# second value is large
	def test_read_large (self) :	
        r = StringIO.StringIO("1 5000\n")
        a = [0, 0]
        b = collatz_read(r, a)
        self.assert_(b    == True)
        self.assert_(a[0] ==  1)
        self.assert_(a[1] == 5000)

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

	# values are both 1
	def test_eval_5 (self) :
		v = collatz_eval(1, 1)
		self.assert_(v == 1)

	# reversed values
	def test_eval_6 (self) :
		v = collatz_eval(10, 5)
		self.assert_(v == 20)
	
	# same value
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

	# values are both 1
    def test_print_one (self) :
        w = StringIO.StringIO()
        collatz_print(w, 1, 1, 1)
        self.assert_(w.getvalue() == "1 1 1\n")

	# same value
    def test_print_same (self) :
        w = StringIO.StringIO()
        collatz_print(w, 5, 5, 6)
        self.assert_(w.getvalue() == "5 5 6\n")
		
	# reversed values
    def test_print_reverse (self) :
        w = StringIO.StringIO()
        collatz_print(w, 10, 5, 20)
        self.assert_(w.getvalue() == "10 5 20\n")

    # -----
    # solve
    # -----

    def test_solve (self) :
        r = StringIO.StringIO("1 10\n100 200\n201 210\n900 1000\n")
        w = StringIO.StringIO()
        collatz_solve(r, w)
        self.assert_(w.getvalue() == "1 10 20\n100 200 125\n201 210 89\n900 1000 174\n")
	
	# one line		
    def test_solve_one (self) :
        r = StringIO.StringIO("1 5\n")
        w = StringIO.StringIO()
        collatz_solve(r, w)
        self.assert_(w.getvalue() == "1 5 8\n")
		
	# two lines	
    def test_solve_two (self) :
        r = StringIO.StringIO("5 5\n5 10\n")
        w = StringIO.StringIO()
        collatz_solve(r, w)
        self.assert_(w.getvalue() == "5 5 6\n5 10 20\n")
		
	# reversed values	
    def test_solve_reverse (self) :
        r = StringIO.StringIO("1 1\n1 5\n5 10\n10 5\n")
        w = StringIO.StringIO()
        collatz_solve(r, w)
        self.assert_(w.getvalue() == "1 1 1\n1 5 8\n5 10 20\n10 5 20\n")

# ----
# main
# ----

print "TestCollatz.py"
unittest.main()
print "Done."