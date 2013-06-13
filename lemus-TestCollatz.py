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
        v = collatz_eval(7, 44)
        self.assert_(v == 112)
        
    def test_eval_6 (self) :
        v = collatz_eval(4, 75)
        self.assert_(v == 116)
        
    def test_eval_7 (self) :
        v = collatz_eval(6, 9)
        self.assert_(v == 20)
        
    def test_eval_8 (self) :
        v = collatz_eval(8, 3)
        self.assert_(v == 17)
        
    def test_eval_9 (self) :
        v = collatz_eval(10, 219)
        self.assert_(v == 125)
    def test_eval_10 (self) :
        v = collatz_eval(25, 12)
        self.assert_(v == 24)
    def test_eval_11 (self) :
        v = collatz_eval(45, 50)
        self.assert_(v == 105)
    def test_eval_12 (self) :
        v = collatz_eval(49, 76)
        self.assert_(v == 116)
    def test_eval_13 (self) :
        v = collatz_eval(11, 21)
        self.assert_(v == 21)
    def test_eval_14 (self) :
        v = collatz_eval(6, 99)
        self.assert_(v == 119)

        
    
    # -----
    # print
    # -----

    def test_print (self) :
        w = StringIO.StringIO()
        collatz_print(w, 1, 10, 20)
        self.assert_(w.getvalue() == "1 10 20\n")
    def test_print_2 (self) :
        w = StringIO.StringIO()
        collatz_print(w, 6, 99, 119)
        self.assert_(w.getvalue() == "6 99 119\n")

    # -----
    # solve
    # -----

    def test_solve (self) :
        r = StringIO.StringIO("1 10\n100 200\n201 210\n900 1000\n")
        w = StringIO.StringIO()
        collatz_solve(r, w)
        self.assert_(w.getvalue() == "1 10 20\n100 200 125\n201 210 89\n900 1000 174\n")
        
    def test_solve_2 (self) :
        r = StringIO.StringIO("15 98\n8 3\n6 9\n4 75\n")
        w = StringIO.StringIO()
        collatz_solve(r, w)
        self.assert_(w.getvalue() == "15 98 119\n8 3 17\n6 9 20\n4 75 116\n")
    def test_solve_3 (self) :
        r = StringIO.StringIO("11 21\n49 76\n")
        w = StringIO.StringIO()
        collatz_solve(r, w)
        self.assert_(w.getvalue() == "11 21 21\n49 76 116\n")
    def test_solve_4 (self) :
        r = StringIO.StringIO("10 219\n25 12\n")
        w = StringIO.StringIO()
        collatz_solve(r, w)
        self.assert_(w.getvalue() == "10 219 125\n25 12 24\n")
    
    
    

# ----
# main
# ----

print "TestCollatz.py"
unittest.main()
print "Done."
