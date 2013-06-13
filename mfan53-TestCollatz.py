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

    def test_read2 (self) :
        r = StringIO.StringIO("53 216\n")
        a = [0, 0]
        b = collatz_read(r, a)
        self.assert_(b    == True)
        self.assert_(a[0] ==  53)
        self.assert_(a[1] == 216)

    def test_read3 (self) :
        r = StringIO.StringIO("15 25\n")
        a = [0, 0]
        b = collatz_read(r, a)
        self.assert_(b    == True)
        self.assert_(a[0] ==  15)
        self.assert_(a[1] == 25)

    def test_read4 (self) :
        r = StringIO.StringIO("300 900\n")
        a = [0, 0]
        b = collatz_read(r, a)
        self.assert_(b    == True)
        self.assert_(a[0] ==  300)
        self.assert_(a[1] == 900)

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
        v = collatz_eval(53, 216)
        self.assert_(v == 125)

    def test_eval_6 (self) :
        v = collatz_eval(15, 25)
        self.assert_(v == 24)

    def test_eval_7 (self) :
        v = collatz_eval(300, 900)
        self.assert_(v == 179)

    # -----
    # print
    # -----

    def test_print (self) :
        w = StringIO.StringIO()
        collatz_print(w, 1, 10, 20)
        self.assert_(w.getvalue() == "1 10 20\n")

    def test_print2 (self) :
        w = StringIO.StringIO()
        collatz_print(w, 53, 216, 125)
        self.assert_(w.getvalue() == "53 216 125\n")

    def test_print3 (self) :
        w = StringIO.StringIO()
        collatz_print(w, 15, 25, 24)
        self.assert_(w.getvalue() == "15 25 24\n")

    def test_print4 (self) :
        w = StringIO.StringIO()
        collatz_print(w, 300, 900, 179)
        self.assert_(w.getvalue() == "300 900 179\n")

    # -----
    # solve
    # -----

    def test_solve (self) :
        r = StringIO.StringIO("1 10\n100 200\n201 210\n900 1000\n")
        w = StringIO.StringIO()
        collatz_solve(r, w)
        self.assert_(w.getvalue() == "1 10 20\n100 200 125\n201 210 89\n900 1000 174\n")

    def test_solve2 (self) :
        r = StringIO.StringIO("1 10\n100 200\n300 900\n")
        w = StringIO.StringIO()
        collatz_solve(r, w)
        self.assert_(w.getvalue() == "1 10 20\n100 200 125\n300 900 179\n")

    def test_solve3 (self) :
        r = StringIO.StringIO("1 10\n1 1\n15 25\n")
        w = StringIO.StringIO()
        collatz_solve(r, w)
        self.assert_(w.getvalue() == "1 10 20\n1 1 1\n15 25 24\n")

    def test_solve4 (self) :
        r = StringIO.StringIO("53 216\n300 900\n900 1000\n")
        w = StringIO.StringIO()
        collatz_solve(r, w)
        self.assert_(w.getvalue() == "53 216 125\n300 900 179\n900 1000 174\n")

# ----
# main
# ----

print "TestCollatz.py"
unittest.main()
print "Done."
