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

from Collatz import collatz_read, cyc_len, collatz_eval, collatz_print, collatz_solve

# -----------
# TestCollatz
# -----------

class TestCollatz (unittest.TestCase) :
    # ----
    # read
    # ----

    def test_read_1 (self) :
        r = StringIO.StringIO("1 10\n")
        a = [0, 0]
        b = collatz_read(r, a)
        self.assert_(b    == True)
        self.assert_(a[0] ==  1)
        self.assert_(a[1] == 10)

    def test_read_2 (self) :
        r = StringIO.StringIO(" 100 200\n")
        a = [0, 0]
        b = collatz_read(r, a)
        self.assert_(b    == True)
        self.assert_(a[0] == 100)
        self.assert_(a[1] == 200)
    
    def test_read_3 (self) :
        r = StringIO.StringIO("300   950\n")
        a = [0, 0]
        b = collatz_read(r, a)
        self.assert_(b    == True)
        self.assert_(a[0] == 300)
        self.assert_(a[1] == 950)
    
    def test_read_4 (self) :
        r = StringIO.StringIO(" 100 200 \n")
        a = [0, 0]
        b = collatz_read(r, a)
        self.assert_(b    == True)
        self.assert_(a[0] == 100)
        self.assert_(a[1] == 200)

    def test_read_5 (self) :
        r = StringIO.StringIO("")
        a = [0, 0]
        b = collatz_read(r, a)
        self.assert_(b == False)

    # ------------
    # cycle length
    # ------------

    def test_length_1 (self) :
	k = cyc_len(1)
	self.assert_(k == 1)

    def test_length_2 (self) :
	k = cyc_len(10)
	self.assert_(k == 7)

    def test_length_3 (self) :
	k = cyc_len(3521)
	self.assert_(k == 106)

    def test_length_4 (self) :
	k = cyc_len(1000000)
	self.assert_(k == 153)

    def test_length_5 (self) :
	k = cyc_len(301020)
	self.assert_(k == 66)

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

    # -----
    # print
    # -----

    def test_print (self) :
        w = StringIO.StringIO()
        collatz_print(w, 1, 10, 20)
        self.assert_(w.getvalue() == "1 10 20\n")

    def test_print (self) :
        w = StringIO.StringIO()
        collatz_print(w, 1, 1000000, 525)
        self.assert_(w.getvalue() == "1 1000000 525\n")

    def test_print (self) :
        w = StringIO.StringIO()
        collatz_print(w, 343, 450, 134)
        self.assert_(w.getvalue() == "343 450 134\n")


    # -----
    # solve
    # -----

    def test_solve (self) :
        r = StringIO.StringIO("1 10\n100 200\n201 210\n900 1000\n")
        w = StringIO.StringIO()
        collatz_solve(r, w)
        self.assert_(w.getvalue() == "1 10 20\n100 200 125\n201 210 89\n900 1000 174\n")

    def test_solve (self) :
        r = StringIO.StringIO("\n")
        w = StringIO.StringIO()
        collatz_solve(r, w)
        self.assert_(w.getvalue() == "")

    def test_solve (self) :
        r = StringIO.StringIO("1 10\n")
        w = StringIO.StringIO()
        collatz_solve(r, w)
        self.assert_(w.getvalue() == "1 10 20\n")

    def test_solve (self) :
        r = StringIO.StringIO("1000 10\n")
        w = StringIO.StringIO()
        collatz_solve(r, w)
        self.assert_(w.getvalue() == "1000 10 179\n")

# ----
# main
# ----

print "TestCollatz.py"
unittest.main()
print "Done."
