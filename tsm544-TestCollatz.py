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
        self.assert_(b == True)
        self.assert_(a[0] == 1)
        self.assert_(a[1] == 10)

    def test_read_01 (self) :
        r = StringIO.StringIO("10 1\n")
        a = [0, 0]
        b = collatz_read(r, a)
        self.assert_(b == True)
        self.assert_(a[0] == 10)
        self.assert_(a[1] == 1)

    def test_read_02 (self) :
        r = StringIO.StringIO("1 2\n3 4\n5 6\n")
        a1 = [0, 0]
        a2 = [0, 0]
        a3 = [0, 0]
        b1 = collatz_read(r, a1)
        b2 = collatz_read(r, a2)
        b3 = collatz_read(r, a3)
        self.assert_(b1 == True)
        self.assert_(b2 == True)
        self.assert_(b3 == True)
        self.assert_(a1[0] == 1)
        self.assert_(a1[1] == 2)
        self.assert_(a2[0] == 3)
        self.assert_(a2[1] == 4)
        self.assert_(a3[0] == 5)
        self.assert_(a3[1] == 6)

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
        # Check for large number first
        v = collatz_eval(10, 1)
        self.assert_(v == 20)

    def test_eval_6 (self) :
        v = collatz_eval(1, 1)
        self.assert_(v == 1)

    def test_eval_7 (self) :
        v = collatz_eval(10, 10)
        self.assert_(v == 7)

    # -----
    # print
    # -----

    def test_print (self) :
        w = StringIO.StringIO()
        collatz_print(w, 1, 10, 20)
        self.assert_(w.getvalue() == "1 10 20\n")

    def test_print_1 (self) :
        w = StringIO.StringIO()
        collatz_print(w, 1, 10, 20)
        collatz_print(w, 2, 3, 4)
        self.assert_(w.getvalue() == "1 10 20\n2 3 4\n")

    def test_print_2 (self) :
        w = StringIO.StringIO()
        collatz_print(w, 10, 1, 20)
        self.assert_(w.getvalue() == "10 1 20\n")

    # -----
    # solve
    # -----

    def test_solve (self) :
        r = StringIO.StringIO("1 10\n100 200\n201 210\n900 1000\n")
        w = StringIO.StringIO()
        collatz_solve(r, w)
        self.assert_(w.getvalue() == "1 10 20\n100 200 125\n201 210 89\n900 1000 174\n")

    def test_solve_1 (self) :
        r = StringIO.StringIO("1 1\n")
        w = StringIO.StringIO()
        collatz_solve(r, w)
        self.assert_(w.getvalue() == "1 1 1\n")

    def test_solve_2 (self) :
        r = StringIO.StringIO("1 10\n10 1\n")
        w = StringIO.StringIO()
        collatz_solve(r, w)
        self.assert_(w.getvalue() == "1 10 20\n10 1 20\n")

    def test_solve_3 (self) :
        # Check for answer caching
        r = StringIO.StringIO("1 10\n1 10\n")
        w = StringIO.StringIO()
        collatz_solve(r, w)
        self.assert_(w.getvalue() == "1 10 20\n1 10 20\n")

# ----
# main
# ----

print "TestCollatz.py"
unittest.main()
print "Done."