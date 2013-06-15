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

    def test_print2 (self) :
        w = StringIO.StringIO()
        collatz_print(w, 2, 4, 8)
        self.assert_(w.getvalue() == "2 4 8\n")

    def test_print3 (self) :
        w = StringIO.StringIO()
        collatz_print(w, 0, 0, 0)
        self.assert_(w.getvalue() == "0 0 0\n")

    # ------------
    # cycle_length
    # ------------

    def test_cycle_length (self) :
        n = 400
        self.assert_(cycle_length(n) == 28)


    def test_cycle_length2 (self) :
        n = 1010101
        self.assert_(cycle_length(n) == 153)

    def test_cycle_length3 (self) :
        n = 78222
        self.assert_(cycle_length(n) == 77)
    # -----
    # solve
    # -----

    def test_solve (self) :
        r = StringIO.StringIO("1 10\n100 200\n201 210\n900 1000\n")
        w = StringIO.StringIO()
        collatz_solve(r, w)
        self.assert_(w.getvalue() == "1 10 20\n100 200 125\n201 210 89\n900 1000 174\n")

    def test_solve_Duplicates (self) :
        r = StringIO.StringIO("10 10\n200 200\n")
        w = StringIO.StringIO()
        collatz_solve(r, w)
        self.assert_(w.getvalue() == "10 10 7\n200 200 27\n")

    def test_solve_ExtremeBound (self) :
        r = StringIO.StringIO("999999 1000000 259\n1 1 1\n")
        w = StringIO.StringIO()
        collatz_solve(r, w)
        self.assert_(w.getvalue() == "999999 1000000 259\n1 1 1\n")

    def test_solve_Reversed_IJ (self) :
        r = StringIO.StringIO("6887 6000\n4 3\n")
        w = StringIO.StringIO()
        collatz_solve(r, w)
        self.assert_(w.getvalue() == "6887 6000 262\n4 3 8\n")

    def test_solve_BIG_Numbers (self) :
        r = StringIO.StringIO("885267 564488\n269064 936951\n928757 679478\n479412 775208\n")
        w = StringIO.StringIO()
        collatz_solve(r, w)
        self.assert_(w.getvalue() == "885267 564488 525\n269064 936951 525\n928757 679478 525\n479412 775208 509\n")    
# ----
# main
# ----

print "TestCollatz.py"
unittest.main()
print "Done."
