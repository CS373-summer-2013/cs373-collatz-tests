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

    def test_read_1 (self) :
        r = StringIO.StringIO("1 1\n")
        a = [0, 0]
        b = collatz_read(r, a)
        self.assert_(b    == True)
        self.assert_(a[0] == 1)
        self.assert_(a[1] == 1)

    def test_read_long_number (self) :
        r = StringIO.StringIO("1 100000\n")
        a = [0, 0]
        b = collatz_read(r, a)
        self.assert_(b    == True)
        self.assert_(a[0] ==  1)
        self.assert_(a[1] == 100000)

    # ----
    # eval
    # ----

    def test_eval_1 (self) :
        v = collatz_eval(1, 10)
        self.assertEqual(v, 20)

    def test_eval_2 (self) :
        v = collatz_eval(100, 200)
        self.assertEqual(v, 125)

    def test_eval_3 (self) :
        v = collatz_eval(201, 210)
        self.assertEqual(v, 89)

    def test_eval_4 (self) :
        v = collatz_eval(5, 5)
        self.assertEqual(v, 6)

    # ------------
    # cycle_length
    # ------------

    def test_cycle_length_1 (self) :
        cache = dict()
        l = cycle_length(5, cache)
        self.assertEqual(l, 6)

    def test_cycle_length_2 (self) :
        cache = dict()
        l = cycle_length (13, cache)
        self.assertEqual(l, 10)

    def test_cycle_length_3 (self) :
        cache = dict()
        l = cycle_length (110, cache)
        self.assertEqual(l, 114)

    def test_cycle_length_4 (self) :
        cache = dict()
        l = cycle_length (1, cache)
        self.assertEqual(l, 1)


    # -----
    # print
    # -----
    def test_print (self) :
        w = StringIO.StringIO()
        collatz_print(w, 1, 10, 20)
        self.assert_(w.getvalue() == "1 10 20\n")

    def test_print_long (self) :
        w = StringIO.StringIO()
        collatz_print(w, 10000, 1000000, 2000000)
        self.assert_(w.getvalue() == "10000 1000000 2000000\n")

    def test_print_longer (self) :
        w = StringIO.StringIO()
        collatz_print(w, 1000000, 100000000, 200000000)
        self.assert_(w.getvalue() == "1000000 100000000 200000000\n")

    # -----
    # solve
    # -----

    def test_solve (self) :
        r = StringIO.StringIO("1 10\n100 200\n201 210\n900 1000\n")
        w = StringIO.StringIO()
        collatz_solve(r, w)
        self.assert_(w.getvalue() == "1 10 20\n100 200 125\n201 210 89\n900 1000 174\n")

    def test_solve_2 (self) :
        r = StringIO.StringIO("1 10\n42 4242\n1000000 1000000\n")
        w = StringIO.StringIO()
        collatz_solve(r, w)
        self.assert_(w.getvalue() == "1 10 20\n42 4242 238\n1000000 1000000 153\n")

    def test_solve_3 (self) :
        r = StringIO.StringIO("7 15\n")
        w = StringIO.StringIO()
        collatz_solve(r, w)
        self.assert_(w.getvalue() == "7 15 20\n")

    def test_solve_4 (self) :
        r = StringIO.StringIO("835 158\n")
        w = StringIO.StringIO()
        collatz_solve(r, w)
        self.assert_(w.getvalue() == "835 158 171\n")

# ----
# main
# ----

print "TestCollatz.py"
unittest.main()
print "Done."
