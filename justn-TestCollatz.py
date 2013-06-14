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

    def test_read_large (self) :
        r = StringIO.StringIO("10000 9000000\n")
        a = [0, 0]
        b = collatz_read(r, a)
        self.assert_(b    == True)
        self.assert_(a[0] ==  10000)
        self.assert_(a[1] == 9000000)

    def test_read_reverse (self) :
        r = StringIO.StringIO("10 1\n")
        a = [0, 0]
        b = collatz_read(r, a)
        self.assert_(b    == True)
        self.assert_(a[0] == 10)
        self.assert_(a[1] ==  1)

    def test_read_nonint(self) :
        r = StringIO.StringIO('a 20\n')
        a = [0, 0]
        try:
            b = collatz_read(r,a)
        except Exception, e:
            self.assert_(type(e) == ValueError)
            b = False
            
        self.assert_(b == False)
        self.assert_(a[0] == 0)
        self.assert_(a[1] == 0)

    def test_read_negative(self) :
        r = StringIO.StringIO('-5 5\n')
        a = [0, 0]
        try:
            b = collatz_read(r,a)
        except Exception, e:
            self.assert_(type(e) == AssertionError)
            b = False
            
        self.assert_(b == False)

    def test_read_zero(self) :
        r = StringIO.StringIO('0 0\n')
        a = [0, 0]
        try:
            b = collatz_read(r,a)
        except Exception, e:
            self.assert_(type(e) == AssertionError)
            b = False

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

    # reverse of test_eval_1
    def test_eval_5 (self) :
        v = collatz_eval(10, 1)
        self.assert_(v == 20)

    # reverse of test_eval_2
    def test_eval_6 (self) :
        v = collatz_eval(200, 100)
        self.assert_(v == 125)

    def test_eval_7 (self) :
        v = collatz_eval(1, 1)
        self.assert_(v == 1)

    # -----
    # print
    # -----

    def test_print_1 (self) :
        w = StringIO.StringIO()
        collatz_print(w, 1, 10, 20)
        self.assert_(w.getvalue() == "1 10 20\n")

    def test_print_2 (self) :
        w = StringIO.StringIO()
        collatz_print(w, 1000, 900, 174)
        self.assert_(w.getvalue() == "1000 900 174\n")

    # -----
    # solve
    # -----

    def test_solve (self) :
        r = StringIO.StringIO("1 10\n100 200\n201 210\n900 1000\n")
        w = StringIO.StringIO()
        collatz_solve(r, w)
        self.assert_(w.getvalue() == "1 10 20\n100 200 125\n201 210 89\n900 1000 174\n")

    def test_solve_reverse (self) :
        r = StringIO.StringIO("10 1\n200 100\n210 201\n1000 900\n")
        w = StringIO.StringIO()
        collatz_solve(r, w)
        self.assert_(w.getvalue() == "10 1 20\n200 100 125\n210 201 89\n1000 900 174\n")

    def test_solve_backwards (self) :
        r = StringIO.StringIO("900 1000\n201 210\n100 200\n1 10\n")
        w = StringIO.StringIO()
        collatz_solve(r, w)
        self.assert_(w.getvalue() == "900 1000 174\n201 210 89\n100 200 125\n1 10 20\n")

    def test_solve_same (self) :
        r = StringIO.StringIO("1 1\n")
        w = StringIO.StringIO()
        collatz_solve(r, w)
        self.assert_(w.getvalue() == "1 1 1\n")

# ----
# main
# ----

print "TestCollatz.py"
unittest.main()
print "Done."
