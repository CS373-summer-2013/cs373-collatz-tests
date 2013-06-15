#!/usr/bin/env python

# -------------------------------
# projects/collatz/TestCollatz.py
# Copyright (C) 2013
# Glenn P. Downing
# -------------------------------

"""
To test the program:
    % python TestCollatz.py >& TestCollatz.out
    % chmod ugo+x TestCollatz.py
    % TestCollatz.py >& TestCollatz.py.out
"""

# -------
# imports
# -------

import StringIO
import unittest

from Collatz import collatz_read, collatz_eval, collatz_print, collatz_solve, fill_cache

# -----------
# TestCollatz
# -----------

class TestCollatz (unittest.TestCase) :

    fill_cache()
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

    def test_read_swap (self) :
        """
        first number larger than second
        """
        r = StringIO.StringIO("200 100\n")
        a = [0, 0]
        b = collatz_read(r, a)
        self.assert_(b    == True)
        self.assert_(a[0] == 200)
        self.assert_(a[1] == 100)

    def test_read_same (self) :
        """
        same numbers
        """
        r = StringIO.StringIO("1 1\n")
        a = [0, 0]
        b = collatz_read(r, a)
        self.assert_(b    == True)
        self.assert_(a[0] == 1)
        self.assert_(a[1] == 1)

    def test_read_range (self) :
        """
        big range
        """
        r = StringIO.StringIO("1 10000\n")
        a = [0, 0]
        b = collatz_read(r, a)
        self.assert_(b    == True)
        self.assert_(a[0] ==     1)
        self.assert_(a[1] == 10000)

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
        v = collatz_eval(200, 100)
        self.assert_(v == 125)

    def test_eval_6 (self) :
        v = collatz_eval(1, 1)
        self.assert_(v == 1)

    def test_eval_7 (self) :
        v = collatz_eval(1, 10000)
        self.assert_(v == 262)

    # -----
    # print
    # -----

    def test_print (self) :
        w = StringIO.StringIO()
        collatz_print(w, 1, 10, 20)
        self.assert_(w.getvalue() == "1 10 20\n")

    def test_print_swap (self) :
        w = StringIO.StringIO()
        collatz_print(w, 200, 100, 125)
        self.assert_(w.getvalue() == "200 100 125\n")

    def test_print_same (self) :
        w = StringIO.StringIO()
        collatz_print(w, 1, 1, 1)
        self.assert_(w.getvalue() == "1 1 1\n")

    def test_print_range (self) :
        w = StringIO.StringIO()
        collatz_print(w, 1, 10000, 262)
        self.assert_(w.getvalue() == "1 10000 262\n")

    # -----
    # solve
    # -----

    def test_solve (self) :
        r = StringIO.StringIO("1 10\n100 200\n201 210\n900 1000\n")
        w = StringIO.StringIO()
        collatz_solve(r, w)
        self.assert_(w.getvalue() == "1 10 20\n100 200 125\n201 210 89\n900 1000 174\n")

    def test_solve_swap (self) :
        r = StringIO.StringIO("10 1\n200 100\n210 201\n1000 900\n")
        w = StringIO.StringIO()
        collatz_solve(r, w)
        self.assert_(w.getvalue() == "10 1 20\n200 100 125\n210 201 89\n1000 900 174\n")

    def test_solve_same (self) :
        r = StringIO.StringIO("10 10\n100 100\n201 201\n900 900\n")
        w = StringIO.StringIO()
        collatz_solve(r, w)
        self.assert_(w.getvalue() == "10 10 7\n100 100 26\n201 201 19\n900 900 55\n")

    def test_solve_range (self) :
        r = StringIO.StringIO("1 10000\n100 20000\n201 2100\n6 101\n")
        w = StringIO.StringIO()
        collatz_solve(r, w)
        self.assert_(w.getvalue() == "1 10000 262\n100 20000 279\n201 2100 182\n6 101 119\n")
# ----
# main
# ----

print "TestCollatz.py"
unittest.main()
print "Done."
