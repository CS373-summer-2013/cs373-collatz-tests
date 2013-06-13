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
        self.assert_(b == True)
        self.assert_(a[0] == 1)
        self.assert_(a[1] == 10)

    # ----
    # new unit tests for read
    # ----

    # inverted input case
    def test_read_inverted (self) :
        r = StringIO.StringIO("2 1\n")
        a = [0, 0]
        b = collatz_read(r, a)
        self.assert_(b == True)
        self.assert_(a[0] == 2)
        self.assert_(a[1] == 1)

    # no input case
    def test_read_noinput (self) :
        r = StringIO.StringIO("") 
        a = [0, 0]
        b = collatz_read(r, a)
        self.assert_(b == False)

    # duplicate input case
    def test_read_4 (self) :
        r = StringIO.StringIO("1 1") 
        a = [0, 0]
        b = collatz_read(r, a)
        self.assert_(b == True)
        self.assert_(a[0] == 1)
        self.assert_(a[1] == 1)
          
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

    # ----
    # new unit tests for eval
    # ----

    def test_eval_monad (self) :
        v = collatz_eval(1, 1)
        self.assert_(v == 1)

    def test_eval_inverted (self) :
        v = collatz_eval(10, 1)
        self.assert_(v == 20)

    def test_eval_dupe (self) :
        v = collatz_eval(4, 4)
        self.assert_(v == 3)
   
    # -----
    # print
    # -----

    def test_print (self) :
        w = StringIO.StringIO()
        collatz_print(w, 1, 10, 20)
        self.assert_(w.getvalue() == "1 10 20\n")

    # ----
    # new unit tests for print
    # ----

    def test_print_2 (self) : 
        w = StringIO.StringIO()
        collatz_print(w, 100, 200, 25)
        self.assert_(w.getvalue() == "100 200 25\n")

    def test_print_3 (self) : 
        w = StringIO.StringIO()
        collatz_print(w, 201, 210, 89)
        self.assert_(w.getvalue() == "201 210 89\n")

    def test_print_4 (self) : 
        w = StringIO.StringIO()
        collatz_print(w, 900, 1000, 174)
        self.assert_(w.getvalue() == "900 1000 174\n")

    def test_print_dupe (self) : 
        w = StringIO.StringIO()
        collatz_print(w, 4, 4, 3)
        self.assert_(w.getvalue() == "4 4 3\n")

    def test_print_inverted (self) : 
        w = StringIO.StringIO()
        collatz_print(w, 10, 1, 20)
        self.assert_(w.getvalue() == "10 1 20\n")

    def test_print_monad (self) : 
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

    # ----
    # new unit tests for print
    # ----

    # Using known inputs and outputs as arguments
    def test_solve_2 (self) :
        r = StringIO.StringIO("1 1\n4 4\n10 1\n210 201\n")
        w = StringIO.StringIO()
        collatz_solve(r, w)
        self.assert_(w.getvalue() == "1 1 1\n4 4 3\n10 1 20\n210 201 89\n")

    # ----
    # new unit tests for my own cycle_length function
    # ----

    def test_cycle_length (self) :
        c = 5
        self.assert_(cycle_length(c) == 6)

    def test_cycle_length_monad (self) :
        c = 1
        self.assert_(cycle_length(c) == 1)

    def test_cycle_length_3 (self) :
        c = 4
        self.assert_(cycle_length(c) == 3)

    def test_cycle_length_4 (self) :
        c = 8
        self.assert_(cycle_length(c) == 4)

# ----
# main
# ----

print "TestCollatz.py"
unittest.main()
print "Done."
