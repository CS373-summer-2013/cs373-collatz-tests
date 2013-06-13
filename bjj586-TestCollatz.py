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
        
    def test_read1 (self) :
        r = StringIO.StringIO("37 49\n")
        a = [0, 0]
        b = collatz_read(r, a)
        self.assert_(b    == True)
        self.assert_(a[0] ==  37)
        self.assert_(a[1] == 49)
        
    def test_read_2 (self) :
        r = StringIO.StringIO("")
        a = [0, 0]
        b = collatz_read(r, a)
        self.assert_(b    == False)
        
    def test_read_3 (self) :
        r = StringIO.StringIO("1 1\n")
        a = [0, 0]
        b = collatz_read(r, a)
        self.assert_(b    == True)
        self.assert_(a[0] ==  1)
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
        
    def test_eval_5 (self) :
        v = collatz_eval(1, 1)
        self.assert_(v == 1)
        
    def test_eval_6 (self) :
        v = collatz_eval(10000, 10010)
        self.assert_(v == 180)
        
    def test_eval_7 (self) :
        v = collatz_eval(100, 210)
        self.assert_(v == 125)

    # -----
    # print
    # -----

    def test_print (self) :
        w = StringIO.StringIO()
        collatz_print(w, 1, 10, 20)
        self.assert_(w.getvalue() == "1 10 20\n")
        
    def test_print_1 (self) :
        w = StringIO.StringIO()
        collatz_print(w, 900, 1000, 174)
        self.assert_(w.getvalue() == "900 1000 174\n")
        
    def test_print_2 (self) :
        w = StringIO.StringIO()
        collatz_print(w, 100, 210, 175)
        self.assert_(w.getvalue() == "100 210 175\n")

    def test_print_3 (self) :
        w = StringIO.StringIO()
        collatz_print(w, 10000, 10010, 180)
        self.assert_(w.getvalue() == "10000 10010 180\n")

    # -----
    # solve
    # -----

    def test_solve (self) :
        r = StringIO.StringIO("1 10\n100 200\n201 210\n900 1000\n")
        w = StringIO.StringIO()
        collatz_solve(r, w)
        self.assert_(w.getvalue() == "1 10 20\n100 200 125\n201 210 89\n900 1000 174\n")

    def test_solve_1 (self) :
            r = StringIO.StringIO("10000 10010\n100 210\n1 20\n7 12\n")
            w = StringIO.StringIO()
            collatz_solve(r, w)
            self.assert_(w.getvalue() == "10000 10010 180\n100 210 125\n1 20 21\n7 12 20\n")
    
    def test_solve_2 (self) :
            r = StringIO.StringIO("1234 1240\n777 780\n150 155\n160 165\n")
            w = StringIO.StringIO()
            collatz_solve(r, w)
            self.assert_(w.getvalue() == "1234 1240 133\n777 780 122\n150 155 85\n160 165 112\n")
    
    def test_solve_3 (self) :
            r = StringIO.StringIO("156 160\n150 165\n1 1\n777 777\n")
            w = StringIO.StringIO()
            collatz_solve(r, w)
            self.assert_(w.getvalue() == "156 160 55\n150 165 112\n1 1 1\n777 777 34\n")

# ----
# main
# ----

print "TestCollatz.py"
unittest.main()
print "Done."
