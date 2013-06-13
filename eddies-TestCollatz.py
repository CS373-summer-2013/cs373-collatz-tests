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

    def test_read_tab (self) :
        r = StringIO.StringIO("1 \t 10\n")
        a = [0, 0]
        b = collatz_read(r, a)
        self.assert_(b == True)
        self.assert_(a[0] == 1)
        self.assert_(a[1] == 10)

    def test_read_whitespace (self) :
        r = StringIO.StringIO(" 1     5    \n")
        a = [0, 0]
        b = collatz_read(r, a)
        self.assert_(b == True)
        self.assert_(a[0] == 1)
        self.assert_(a[1] == 5)

    def test_read_empty (self) :
        r = StringIO.StringIO("")
        a = [0, 0]
        b = collatz_read(r, a)
        self.assert_(b == False)
        self.assert_(a[0] == 0)
        self.assert_(a[1] == 0)

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

    # My tests for eval start below

    def test_eval_5 (self) :
        v = collatz_eval(1, 2)
        self.assert_(v == 2)

    def test_eval_6 (self) :
        v = collatz_eval(4, 5)
        self.assert_(v == 6)

    def test_eval_7 (self) :
        v = collatz_eval(5, 10)
        self.assert_(v == 20)

    def test_eval_8 (self) :
        v = collatz_eval(1, 1)
        self.assert_(v == 1)

    # -----
    # print
    # -----

    def test_print (self) :
        w = StringIO.StringIO()
        collatz_print(w, 1, 10, 20)
        self.assert_(w.getvalue() == "1 10 20\n")

    def test_print_1 (self) :
        w = StringIO.StringIO()
        collatz_print(w, 1, 2, 2)
        self.assert_(w.getvalue() == "1 2 2\n")

    def test_print_diff_types (self) :
        w = StringIO.StringIO()
        collatz_print(w, 1, "2", 3)
        self.assert_(w.getvalue() == "1 2 3\n")

    def test_print_garbage (self) :
        w = StringIO.StringIO()
        collatz_print(w, "str1", "42 5", True)
        self.assert_(w.getvalue() == "str1 42 5 True\n")

    # -----
    # solve
    # -----

    def test_solve (self) :
        r = StringIO.StringIO("1 10\n100 200\n201 210\n900 1000\n")
        w = StringIO.StringIO()
        collatz_solve(r, w)
        self.assert_(w.getvalue() == "1 10 20\n100 200 125\n201 210 89\n900 1000 174\n")

    def test_solve_1 (self) :
        r = StringIO.StringIO("1 2\n 4 5\n 5 10\n")
        w = StringIO.StringIO()
        collatz_solve(r, w)
        self.assert_(w.getvalue() == "1 2 2\n4 5 6\n5 10 20\n")

    def test_solve_tab (self) :
        r = StringIO.StringIO("1 \t 2\n1 \t\t 10\n")
        w = StringIO.StringIO()
        collatz_solve(r, w)
        self.assert_(w.getvalue() == "1 2 2\n1 10 20\n")

    def test_solve_empty (self) :
        r = StringIO.StringIO("")
        w = StringIO.StringIO()
        collatz_solve(r, w)
        self.assert_(w.getvalue() == "")


# ----
# main
# ----

print "TestCollatz.py"
unittest.main()
print "Done."
