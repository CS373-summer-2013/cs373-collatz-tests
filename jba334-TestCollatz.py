#!/usr/bin/env python

# -------------------------------
# projects/collatz/TestCollatz.py
# Copyright (C) 2013
# Glenn P. Downing
# -------------------------------

# James Aydemir
# EID: jba334
# CS 373
# Due: 13 June 2013

"""
To test the program:
    % python TestCollatz.py >& TestCollatz.py.out
    % chmod ugo+x TestCollatz.py
    % TestCollatz.py >& TestCollatz.out
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
        
    def test_read_1 (self) :
    	r = StringIO.StringIO("100 200\n")
        a = [0, 0]
        b = collatz_read(r, a)
        self.assert_(b    == True)
        self.assert_(a[0] == 100)
        self.assert_(a[1] == 200)
        
    def test_read_2 (self) :
    	r = StringIO.StringIO("1 1\n")
        a = [0, 0]
        b = collatz_read(r, a)
        self.assert_(b    == True)
        self.assert_(a[0] == 1)
        self.assert_(a[1] == 1)
        
    def test_read_3 (self) :
    	r = StringIO.StringIO("100 1\n")
        a = [0, 0]
        b = collatz_read(r, a)
        self.assert_(b    == True)
        self.assert_(a[0] == 100)
        self.assert_(a[1] == 1)
        

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
        v = collatz_eval(10, 1)
        self.assert_(v == 20)

    def test_eval_6 (self) :
        v = collatz_eval(200, 100)
        self.assert_(v == 125)

    def test_eval_7 (self) :
        v = collatz_eval(210, 201)
        self.assert_(v == 89)

    def test_eval_8 (self) :
        v = collatz_eval(1000, 900)
        self.assert_(v == 174)
        
    def test_eval_9 (self) :
        v = collatz_eval(1, 1)
        self.assert_(v == 1)

    def test_eval_10 (self) :
        v = collatz_eval(5, 10)
        self.assert_(v == 20)

    def test_eval_11 (self) :
        v = collatz_eval(7, 9)
        self.assert_(v == 20)

    def test_eval_12 (self) :
        v = collatz_eval(1000, 1001)
        self.assert_(v == 143)

    # -----
    # print
    # -----

    def test_print (self) :
        w = StringIO.StringIO()
        collatz_print(w, 1, 10, 20)
        self.assert_(w.getvalue() == "1 10 20\n")
        
    def test_print_1 (self) :
        w = StringIO.StringIO()
        collatz_print(w, 1, 1, 1)
        self.assert_(w.getvalue() == "1 1 1\n")
        
    def test_print_2 (self) :
        w = StringIO.StringIO()
        collatz_print(w, 7, 9, 20)
        self.assert_(w.getvalue() == "7 9 20\n")
        
    def test_print_3 (self) :
        w = StringIO.StringIO()
        collatz_print(w, 10, 1, 20)
        self.assert_(w.getvalue() == "10 1 20\n")
        
    # ------------
    # cycle_length
    # ------------

    # -----
    # solve
    # -----

    def test_solve (self) :
        r = StringIO.StringIO("1 10\n100 200\n201 210\n900 1000\n")
        w = StringIO.StringIO()
        collatz_solve(r, w)
        self.assert_(w.getvalue() == "1 10 20\n100 200 125\n201 210 89\n900 1000 174\n")

    def test_solve_1 (self) :
        r = StringIO.StringIO("100 100\n")
        w = StringIO.StringIO()
        collatz_solve(r, w)
        self.assert_(w.getvalue() == "100 100 26\n")
        
    def test_solve_2 (self) :
        r = StringIO.StringIO("1 5\n5 1\n")
        w = StringIO.StringIO()
        collatz_solve(r, w)
        self.assert_(w.getvalue() == "1 5 8\n5 1 8\n")
        
    def test_solve_3 (self) :
        r = StringIO.StringIO("1 5\n5 1\n")
        w = StringIO.StringIO()
        collatz_solve(r, w)
        self.assert_(w.getvalue() == "1 5 8\n5 1 8\n")

# ----
# main
# ----

print "TestCollatz.py"
unittest.main()
print "Done."
