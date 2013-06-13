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

from Collatz import collatz_read, collatz_eval, collatz_print, collatz_solve, collatz_cycle_length

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
        self.assert_(b    ==  True)
        self.assert_(a[0] ==  1)
        self.assert_(a[1] ==  10)

    def test_read_largeint (self) :
        r = StringIO.StringIO("1 4294967295\n")
        a = [0, 0]
        b = collatz_read(r, a)
        self.assert_(b    ==  True)
        self.assert_(a[0] ==  1)
        self.assert_(a[1] ==  4294967295)

    def test_read_sameint (self) :
        r = StringIO.StringIO("78 78\n")
        a = [0, 0]
        b = collatz_read(r, a)
        self.assert_(b    ==  True)
        self.assert_(a[0] ==  78)
        self.assert_(a[1] ==  78)

    def test_read_samelargeint (self) :
        r = StringIO.StringIO("4294967295 4294967295\n")
        a = [0, 0]
        b = collatz_read(r, a)
        self.assert_(b    ==  True)
        self.assert_(a[0] ==  4294967295)
        self.assert_(a[1] ==  4294967295)

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
        v = collatz_eval(1, 1000)
        self.assert_(v == 179)

    def test_eval_same_1 (self) :
        v = collatz_eval(1, 1)
        self.assert_(v == 1)

    def test_eval_same_2 (self) :
        v = collatz_eval(5, 5)
        self.assert_(v == 6)

    # -----
    # print
    # -----

    def test_print (self) :
        w = StringIO.StringIO()
        collatz_print(w, 1, 10, 20)
        self.assert_(w.getvalue() == "1 10 20\n")

    def test_print_largeint (self) :
        w = StringIO.StringIO()
        collatz_print(w, 1, 4294967295, 99999)
        self.assert_(w.getvalue() == "1 4294967295 99999\n")

    def test_print_sameint (self) :
        w = StringIO.StringIO()
        collatz_print(w, 78, 78, 78)
        self.assert_(w.getvalue() == "78 78 78\n")

    def test_print_samelargeint (self) :
        w = StringIO.StringIO()
        collatz_print(w, 4294967295, 4294967295, 4294967295)
        self.assert_(w.getvalue() == "4294967295 4294967295 4294967295\n")

    # -----
    # solve
    # -----

    def test_solve (self) :
        r = StringIO.StringIO("1 10\n100 200\n201 210\n900 1000\n")
        w = StringIO.StringIO()
        collatz_solve(r, w)
        self.assert_(w.getvalue() == "1 10 20\n100 200 125\n201 210 89\n900 1000 174\n")

    def test_solve_02 (self) :
        r = StringIO.StringIO("1 1\n2 2\n8 8\n27 27\n")
        w = StringIO.StringIO()
        collatz_solve(r, w)
        self.assert_(w.getvalue() == "1 1 1\n2 2 2\n8 8 4\n27 27 112\n")

    def test_solve_03 (self) :
        r = StringIO.StringIO("1 1000\n")
        w = StringIO.StringIO()
        collatz_solve(r, w)
        self.assert_(w.getvalue() == "1 1000 179\n")

    def test_solve_04 (self) :
        r = StringIO.StringIO("1 1000\n1 10000\n1 100\n")
        w = StringIO.StringIO()
        collatz_solve(r, w)
        self.assert_(w.getvalue() == "1 1000 179\n1 10000 262\n1 100 119\n")

    def test_solve_05 (self) :
        r = StringIO.StringIO("1 1\n")
        w = StringIO.StringIO()
        collatz_solve(r, w)
        self.assert_(w.getvalue() == "1 1 1\n")


    # -----------------
    # test_cycle-length
    # -----------------

    def test_cycle_length_01 (self) :
        value = collatz_cycle_length(1)
        self.assert_(value == 1)

    def test_cycle_length_02 (self) :
        value = collatz_cycle_length(2)
        self.assert_(value == 2)

    def test_cycle_length_03 (self) :
        value = collatz_cycle_length(8)
        self.assert_(value == 4)

    def test_cycle_length_04 (self) :
        value = collatz_cycle_length(27)
        self.assert_(value == 112)

    def test_cycle_length_05 (self) :
        value = collatz_cycle_length(5)
        self.assert_(value == 6)

    def test_cycle_length_06 (self) :
        value = collatz_cycle_length(6)
        self.assert_(value == 9)

    """ Only test this with a cache or the test may never finish!!! 
    def test_cycle_length_07 (self) :
        value = collatz_cycle_length(4294967295)
        self.assert_(value == 452)
    """

# ----
# main
# ----

print "TestCollatz.py"
unittest.main()
print "Done."
