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
        r = StringIO.StringIO("21 210\n")
        a = [0, 0]
        b = collatz_read(r, a)
        self.assert_(b    == True)
        self.assert_(a[0] ==  21)
        self.assert_(a[1] == 210)
    def test_read2 (self) :
        r = StringIO.StringIO("11 13\n")
        a = [0, 0]
        b = collatz_read(r, a)
        self.assert_(b    == True)
        self.assert_(a[0] ==  11)
        self.assert_(a[1] == 13)
    def test_read3 (self) :
        r = StringIO.StringIO("100 1000\n")
        a = [0, 0]
        b = collatz_read(r, a)
        self.assert_(b    == True)
        self.assert_(a[0] ==  100)
        self.assert_(a[1] == 1000)


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
        v = collatz_eval(190, 300)
        self.assert_(v == 128)

    def test_eval_6 (self) :
        v = collatz_eval(1000, 10000)
        self.assert_(v == 262)

    def test_eval_7 (self) :
        v = collatz_eval(501, 800)
        self.assert_(v == 171)

    # -----
    # print
    # -----

    def test_print (self) :
        w = StringIO.StringIO()
        collatz_print(w, 1, 10, 20)
        self.assert_(w.getvalue() == "1 10 20\n")

    def test_print1 (self) :
        w = StringIO.StringIO()
        collatz_print(w, 300, 900, 179)
        self.assert_(w.getvalue() == "300 900 179\n")
    def test_print2 (self) :
        w = StringIO.StringIO()
        collatz_print(w, 1000, 10000, 262)
        self.assert_(w.getvalue() == "1000 10000 262\n")
    def test_print3 (self) :
        w = StringIO.StringIO()
        collatz_print(w, 501, 800, 171)
        self.assert_(w.getvalue() == "501 800 171\n")

    # -----
    # solve
    # -----

    def test_solve (self) :
        r = StringIO.StringIO("1 10\n100 200\n201 210\n900 1000\n")
        w = StringIO.StringIO()
        collatz_solve(r, w)
        self.assert_(w.getvalue() == "1 10 20\n100 200 125\n201 210 89\n900 1000 174\n")

    def test_solve1 (self) :
        r = StringIO.StringIO("300 900\n1000 10000\n501 800\n9000 90000\n")
        w = StringIO.StringIO()
        collatz_solve(r, w)
        self.assert_(w.getvalue() == "300 900 179\n1000 10000 262\n501 800 171\n9000 90000 351\n")
    def test_solve2 (self) :
        r = StringIO.StringIO("11 110\n1100 1200\n1201 1210\n1900 10000\n")
        w = StringIO.StringIO()
        collatz_solve(r, w)
        self.assert_(w.getvalue() == "11 110 119\n1100 1200 182\n1201 1210 71\n1900 10000 262\n")
    def test_solve3 (self) :
        r = StringIO.StringIO("21 210\n2100 2200\n2201 2210\n2900 21000\n")
        w = StringIO.StringIO()
        collatz_solve(r, w)
        self.assert_(w.getvalue() == "21 210 125\n2100 2200 170\n2201 2210 170\n2900 21000 279\n")

# ----
# main
# ----

print "TestCollatz.py"
unittest.main()
print "Done."
