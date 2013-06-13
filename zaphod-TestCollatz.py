#!/usr/bin/env python

# -------------------------------
# projects/collatz/zaphod-TestCollatz.py
# Copyright (C) 2013
# Jason Brown
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

    def test_read1 (self) :
        r = StringIO.StringIO("1 1\n")
        a = [0, 0]
        b = collatz_read(r, a)
        self.assert_(b    == True)
        self.assert_(a[0] ==  1)
        self.assert_(a[1] == 1)

    def test_read2 (self) :
        r = StringIO.StringIO("999 1000\n")
        a = [0, 0]
        b = collatz_read(r, a)
        self.assert_(b    == True)
        self.assert_(a[0] ==  999)
        self.assert_(a[1] == 1000)
        
    def test_read3 (self) :
        r = StringIO.StringIO("999000 999999\n")
        a = [0, 0]
        b = collatz_read(r, a)
        self.assert_(b    == True)
        self.assert_(a[0] == 999000)
        self.assert_(a[1] == 999999)
    # ----
    # eval
    # ----

    def test_eval_1 (self) :
        v = collatz_eval(999, 1000)
        self.assert_(v == 112)

    def test_eval_2 (self) :
        v = collatz_eval(900, 1000)
        self.assert_(v == 174)

    def test_eval_3 (self) :
        v = collatz_eval(15000, 25000)
        self.assert_(v == 282)

    def test_eval_4 (self) :
        v = collatz_eval(9500, 10000)
        self.assert_(v == 242)

    #boundary
    def test_eval_5 (self) :
        v = collatz_eval(999999, 999999)
        self.assert_(v == 259)
        
    #same number
    def test_eval_6 (self) :
        v = collatz_eval(1, 1)
        self.assert_(v == 1)
        
    def test_eval_7 (self) :
        v = collatz_eval(500, 1000)
        self.assert_(v == 179)
        
    #reverse ranges
    def test_eval_8 (self) :
        v = collatz_eval(10, 1)
        self.assert_(v == 20)
        
        
    def test_eval_9 (self) :
        v = collatz_eval(500000, 600000)
        self.assert_(v == 470)
        
    def test_eval_10 (self) :
        v = collatz_eval(999000, 999999)
        self.assert_(v == 396)
        
    def test_eval_11 (self) :
        v = collatz_eval(1, 300000)
        self.assert_(v == 443)
        
    def test_eval_12 (self) :
        v = collatz_eval(500000, 999999)
        self.assert_(v == 525)
        
    def test_eval_13 (self) :
        v = collatz_eval(1, 500000)
        self.assert_(v == 449)
        
    def test_eval_13 (self) :
        v = collatz_eval(1, 999999)
        self.assert_(v == 525)
        
    # -----
    # print
    # -----

    def test_print1 (self) :
        w = StringIO.StringIO()
        collatz_print(w, 500, 1000, 179)
        self.assert_(w.getvalue() == "500 1000 179\n")
        
    def test_print2 (self) :
        w = StringIO.StringIO()
        collatz_print(w, 2500, 3000, 217)
        self.assert_(w.getvalue() == "2500 3000 217\n")

    def test_print3 (self) :
        w = StringIO.StringIO()
        collatz_print(w, 9500, 10000, 242)
        self.assert_(w.getvalue() == "9500 10000 242\n")

    # -----
    # solve
    # -----

    def test_solve1 (self) :
        r = StringIO.StringIO("1 1\n2 2\n3 3\n4 4\n5 5\n")
        w = StringIO.StringIO()
        collatz_solve(r, w)
        self.assert_(w.getvalue() == "1 1 1\n2 2 2\n3 3 8\n4 4 3\n5 5 6\n")
        
    def test_solve2 (self) :
        r = StringIO.StringIO("500 1000\n2500 3000\n9500 10000\n")
        w = StringIO.StringIO()
        collatz_solve(r, w)
        self.assert_(w.getvalue() == "500 1000 179\n2500 3000 217\n9500 10000 242\n")
        
    def test_solve3 (self) :
        r = StringIO.StringIO("10000 10000\n7520 7520\n5115 5115\n")
        w = StringIO.StringIO()
        collatz_solve(r, w)
        self.assert_(w.getvalue() == "10000 10000 30\n7520 7520 133\n5115 5115 60\n")

# ----
# main
# ----

print "zaphod-TestCollatz.py"
unittest.main()
print "Done."