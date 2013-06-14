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
    def test_read1 (self) :
        r = StringIO.StringIO("1 20\n")
        a = [0, 0]
        b = collatz_read(r, a)
        self.assert_(b    == True)
        self.assert_(a[0] ==  1)
        self.assert_(a[1] == 20)
    def test_read2 (self) :
        r = StringIO.StringIO("20 10\n")
        a = [0, 0]
        b = collatz_read(r, a)
        self.assert_(b    == True)
        self.assert_(a[0] == 20)
        self.assert_(a[1] == 10)
    def test_read3 (self) :
        r = StringIO.StringIO("100000 102\n")
        a = [0, 0]
        b = collatz_read(r, a)
        self.assert_(b    ==   True)
        self.assert_(a[0] == 100000)
        self.assert_(a[1] ==    102)

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
        v = collatz_eval(1, 2)
        self.assert_(v == 2)

    def test_eval_6 (self) :
        v = collatz_eval(2, 1)
        self.assert_(v == 2)
		
    def test_eval_7 (self) :
        v = collatz_eval(5, 3)
        self.assert_(v == 8)

    # -----
    # print
    # -----

    def test_print (self) :
        w = StringIO.StringIO()
        collatz_print(w, 1, 10, 20)
        self.assert_(w.getvalue() == "1 10 20\n")
		
    def test_print1 (self) :
        w = StringIO.StringIO()
        collatz_print(w, 100, 200, 125)
        self.assert_(w.getvalue() == "100 200 125\n")
		
    def test_print2 (self) :
        w = StringIO.StringIO()
        collatz_print(w, 5, 4, 230)
        self.assert_(w.getvalue() == "5 4 230\n")

    def test_print3 (self) :
        w = StringIO.StringIO()
        collatz_print(w, 23, 21, 12)
        self.assert_(w.getvalue() == "23 21 12\n")

    # -----
    # solve
    # -----

    def test_solve (self) :
        r = StringIO.StringIO("1 10\n100 200\n201 210\n900 1000\n")
        w = StringIO.StringIO()
        collatz_solve(r, w)
        self.assert_(w.getvalue() == "1 10 20\n100 200 125\n201 210 89\n900 1000 174\n")

    def test_solve1 (self) :
        r = StringIO.StringIO("1 10\n")
        w = StringIO.StringIO()
        collatz_solve(r, w)
        self.assert_(w.getvalue() == "1 10 20\n")
		
    def test_solve2 (self) :
        r = StringIO.StringIO("10 1\n")
        w = StringIO.StringIO()
        collatz_solve(r, w)
        self.assert_(w.getvalue() == "10 1 20\n")
		
    def test_solve3 (self) :
        r = StringIO.StringIO("5 3\n")
        w = StringIO.StringIO()
        collatz_solve(r, w)
        self.assert_(w.getvalue() == "5 3 8\n")

# ----
# main
# ----

print "TestCollatz.py"
unittest.main()
print "Done."
