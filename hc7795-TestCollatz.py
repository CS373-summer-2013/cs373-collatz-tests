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
    
    def test_read2 (self) :
        r = StringIO.StringIO("20 30\n")
        a = [0, 0]
        b = collatz_read(r, a)
        self.assert_(b    == True)
        self.assert_(a[0] ==  20)
        self.assert_(a[1] == 30)
    
    def test_read3 (self) :
        r = StringIO.StringIO("1001 1004\n")
        a = [0, 0]
        b = collatz_read(r, a)
        self.assert_(b    == True)
        self.assert_(a[0] ==  1001)
        self.assert_(a[1] == 1004)

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
        v = collatz_eval(10, 1)
        self.assert_(v == 20)
        
    def test_eval_6 (self) :
        v = collatz_eval(1, 1)
        self.assert_(v == 1)
    
    def test_eval_7 (self) :
        v = collatz_eval(10, 10)
        self.assert_(v == 7)
    
    def test_eval_8 (self) :
        v = collatz_eval(100, 110)
        self.assert_(v == 114)
        
    def test_eval_9 (self) :
        v = collatz_eval(35, 23)
        self.assert_(v == 112)
    
    def test_eval_10 (self) :
        v = collatz_eval(47, 55)
        self.assert_(v == 113)
    

    # -----
    # print
    # -----

    def test_print1 (self) :
        w = StringIO.StringIO()
        collatz_print(w, 1, 10, 20)
        self.assert_(w.getvalue() == "1 10 20\n")
        
    def test_print2 (self) :
        w = StringIO.StringIO()
        collatz_print(w, 100, 200, 125)
        self.assert_(w.getvalue() == "100 200 125\n")
    
    def test_print3 (self) :
        w = StringIO.StringIO()
        collatz_print(w, 201, 210, 89)
        self.assert_(w.getvalue() == "201 210 89\n")
        
    def test_print4 (self) :
        w = StringIO.StringIO()
        collatz_print(w, 900, 100, 174)
        self.assert_(w.getvalue() == "900 100 174\n")

    # -----
    # solve
    # -----


    def test_solve1 (self) :
        r = StringIO.StringIO("1 10\n100 200\n201 210\n900 1000\n")
        w = StringIO.StringIO()
        collatz_solve(r, w)
        self.assert_(w.getvalue() == "1 10 20\n100 200 125\n201 210 89\n900 1000 174\n")
    
    def test_solve2 (self) :
        r = StringIO.StringIO("1 1\n10 1\n")
        w = StringIO.StringIO()
        collatz_solve(r, w)
        self.assert_(w.getvalue() == "1 1 1\n10 1 20\n")
    
    def test_solve3 (self) :
        r = StringIO.StringIO("100 110\n35 23\n47 55\n")
        w = StringIO.StringIO()
        collatz_solve(r, w)
        self.assert_(w.getvalue() == "100 110 114\n35 23 112\n47 55 113\n")
    
    def test_solve4 (self) :
        r = StringIO.StringIO("13 19\n91 101\n")
        w = StringIO.StringIO()
        collatz_solve(r, w)
        self.assert_(w.getvalue() == "13 19 21\n91 101 119\n")

# ----
# main
# ----

print "TestCollatz.py"
unittest.main()
print "Done."
