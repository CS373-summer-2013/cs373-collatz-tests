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

    def test_read_reverse (self) :
        r = StringIO.StringIO("10 1\n")
        a = [0, 0]
        b = collatz_read(r, a)
        self.assert_(b    == True)
        self.assert_(a[0] == 10)
        self.assert_(a[1] == 1)

    def test_read_same_input (self) :
        r = StringIO.StringIO("10 10\n")
        a = [0, 0]
        b = collatz_read(r, a)
        self.assert_(b    == True)
        self.assert_(a[0] == 10)
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

    def test_eval_reverse (self) :
        v = collatz_eval(1000, 900)
        self.assert_(v == 174)

    def test_eval_same (self) :
        v = collatz_eval(20, 20)
        self.assert_(v == 8)

    def test_eval_1to5 (self) :
        v = collatz_eval(1, 5)
        self.assert_(v == 8)

    def test_eval_1 (self) :
        v = collatz_eval(1, 1)
        self.assert_(v == 1)


    # -----
    # print
    # -----

    def test_print (self) :
        w = StringIO.StringIO()
        collatz_print(w, 1, 10, 20)
        self.assert_(w.getvalue() == "1 10 20\n")

    def test_print_reverse (self) :
        w = StringIO.StringIO()
        collatz_print(w, 20, 10, 1)
        self.assert_(w.getvalue() == "20 10 1\n")

    def test_print_same (self) :
        w = StringIO.StringIO()
        collatz_print(w, 1, 1, 1)
        self.assert_(w.getvalue() == "1 1 1\n")


    # -----
    # solve
    # -----

    def test_solve (self) :
        r = StringIO.StringIO("1 10\n100 200\n201 210\n900 1000\n")
        w = StringIO.StringIO()
        collatz_solve(r, w)
        self.assert_(w.getvalue() == "1 10 20\n100 200 125\n201 210 89\n900 1000 174\n")

    def test_solve_same (self) :
        r = StringIO.StringIO("1 1\n5 5\n10 10\n")
        w = StringIO.StringIO()
        collatz_solve(r, w)
        self.assert_(w.getvalue() == "1 1 1\n5 5 6\n10 10 7\n")

    def test_solve_same_reverse (self) :
        r = StringIO.StringIO("10 1\n200 100\n210 201\n1000 900\n")
        w = StringIO.StringIO()
        collatz_solve(r, w)
        self.assert_(w.getvalue() == "10 1 20\n200 100 125\n210 201 89\n1000 900 174\n")

    # -----
    # cycle_length
    # -----

    def test_cycle_length_1(self) :
        v = cycle_length(1)
        self.assert_(v == 1)   

    def test_cycle_length_10(self) :
        v = cycle_length(10)
        self.assert_(v == 7)   

    def test_cycle_length_100(self) :
        v = cycle_length(100)
        self.assert_(v == 26)   


    def test_cycle_length_1mil(self) :
        v = cycle_length(1000000)
        self.assert_(v == 153)


# ----
# main
# ----

print "TestCollatz.py"
unittest.main()
print "Done."
