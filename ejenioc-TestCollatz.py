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

    # User Tests
    def test_read1 (self) :
        r = StringIO.StringIO("100 200\n")
        a = [0, 0]
        b = collatz_read(r, a)
        self.assert_(b == True)
        self.assert_(a[0] == 100)
        self.assert_(a[1] == 200)
  
    def test_read2 (self) :
        r = StringIO.StringIO("1000 50000\n")
        a = [0, 0]
        b = collatz_read(r, a)
        self.assert_(b == True)
        self.assert_(a[0] == 1000)
        self.assert_(a[1] == 50000)

    def test_read3 (self) :
        r = StringIO.StringIO("50001 777896\n")
        a = [0, 0]
        b = collatz_read(r, a)
        self.assert_(b == True)
        self.assert_(a[0] == 50001)
        self.assert_(a[1] == 777896)

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

    # User Tests
    def test_eval_5 (self) :
        v = collatz_eval(2429, 3496)
        self.assert_(v == 217)
    
    def test_eval_6 (self) :
        v = collatz_eval(6519, 2895)
        self.assert_(v == 262)

    def test_eval_7 (self) :
        v = collatz_eval(3830, 40652)
        self.assert_(v == 324)

    # -----
    # print
    # -----

    def test_print (self) :
        w = StringIO.StringIO()
        collatz_print(w, 1, 10, 20)
        self.assert_(w.getvalue() == "1 10 20\n")

    # User Tests
    def test_print1 (self) :
        w = StringIO.StringIO()
        collatz_print(w, 900, 1000, 174)
        self.assert_(w.getvalue() == "900 1000 174\n")
 
    def test_print2 (self) :
        w = StringIO.StringIO()
        collatz_print(w, 3830, 40652, 324)
        self.assert_(w.getvalue() == "3830 40652 324\n")
 
    def test_print3 (self) :
        w = StringIO.StringIO()
        collatz_print(w, 6519, 2895, 262)
        self.assert_(w.getvalue() == "6519 2895 262\n")

    # -----
    # solve
    # -----

    def test_solve (self) :
        r = StringIO.StringIO("1 10\n100 200\n201 210\n900 1000\n")
        w = StringIO.StringIO()
        collatz_solve(r, w)
        self.assert_(w.getvalue() == "1 10 20\n100 200 125\n201 210 89\n900 1000 174\n")

    # User Tests
    def test_solve1 (self) :
        r = StringIO.StringIO("3830 40652\n6519 2895\n2429 3496\n1185 38112\n")
        w = StringIO.StringIO()
        collatz_solve(r, w)
        self.assert_(w.getvalue() == "3830 40652 324\n6519 2895 262\n2429 3496 217\n1185 38112 324\n")

    def test_solve2 (self) :
        r = StringIO.StringIO("400 23244\n8224 14575\n7395 47307\n9926 4367\n")
        w = StringIO.StringIO()
        collatz_solve(r, w)
        self.assert_(w.getvalue() == "400 23244 279\n8224 14575 276\n7395 47307 324\n9926 4367 262\n")

    def test_solve3 (self) :
        r = StringIO.StringIO("8002 29\n7860 46420\n6009 91\n6691 22030\n")
        w = StringIO.StringIO()
        collatz_solve(r, w)
        self.assert_(w.getvalue() == "8002 29 262\n7860 46420 324\n6009 91 238\n6691 22030 279\n")

# ----
# main
# ----

print "TestCollatz.py"
unittest.main()
print "Done."
