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

import StringIO, unittest

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
        
    def test_read_reverse (self) :
        r = StringIO.StringIO("10 1\n")
        a = [0, 0]
        b = collatz_read(r, a)
        self.assert_(b    == True)
        self.assert_(a[0] ==  10)
        self.assert_(a[1] == 1)
        
    def test_read_null (self) :
        r = StringIO.StringIO("")
        a = [0, 0]
        b = collatz_read(r, a)
        self.assert_(b    == False)
        
    def test_read_multiple (self) :
        a = [0, 0]
        b = [0, 0]
        c = [0, 0]
        
        r = StringIO.StringIO("300 357\n")
        d = collatz_read(r, a)
        self.assert_(d    == True)
        self.assert_(a[0] ==  300)
        self.assert_(a[1] == 357)
        
        r = StringIO.StringIO("678 1000\n")
        d = collatz_read(r, b)
        self.assert_(d    == True)
        self.assert_(b[0] ==  678)
        self.assert_(b[1] == 1000)
        
        r = StringIO.StringIO("1 1000000\n")
        d = collatz_read(r, c)
        self.assert_(d    == True)
        self.assert_(c[0] ==  1)
        self.assert_(c[1] == 1000000)

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
        
    def test_eval_5(self):
        v = collatz_eval(263, 563)
        self.assert_(v == 144)
        
    def test_eval_6(self):
        v = collatz_eval(468, 3678)
        self.assert_(v == 217)
        
    def test_eval_ascending(self):
        v = collatz_eval(200, 300)
        self.assert_(v == 128)
    
    def test_eval_descending(self):
        v = collatz_eval(300, 200)
        self.assert_(v == 128)
        
    def test_eval_singleton(self):
        v  = collatz_eval(233, 233)
        self.assert_(v == 84)

    # -----
    # print
    # -----

    def test_print (self) :
        w = StringIO.StringIO()
        collatz_print(w, 1, 10, 20)
        self.assert_(w.getvalue() == "1 10 20\n")
        
    def test_print_null (self) :
        w = StringIO.StringIO()
        collatz_print(w, '', '', '')
        self.assert_(w.getvalue() == "  \n")
        
    def test_print_multiple (self) :
        w = StringIO.StringIO()
        collatz_print(w, 1, 10, 20)
        self.assert_(w.getvalue() == "1 10 20\n")
        
        w = StringIO.StringIO()
        collatz_print(w, 27, 456, 144)
        self.assert_(w.getvalue() == "27 456 144\n")
        
        w = StringIO.StringIO()
        collatz_print(w, 356, 100000, 351)
        self.assert_(w.getvalue() == "356 100000 351\n")
        
    def test_print_reverse (self) :
        w = StringIO.StringIO()
        collatz_print(w, 10, 1, 20)
        self.assert_(w.getvalue() == "10 1 20\n")

    # -----
    # solve
    # -----

    def test_solve (self) :
        r = StringIO.StringIO("1 10\n100 200\n201 210\n900 1000\n")
        w = StringIO.StringIO()
        collatz_solve(r, w)
        self.assert_(w.getvalue() == "1 10 20\n100 200 125\n201 210 89\n900 1000 174\n")
        
    def test_solve_single (self) :
        r = StringIO.StringIO("256 1000\n")
        w = StringIO.StringIO()
        collatz_solve(r, w)
        self.assert_(w.getvalue() == "256 1000 179\n")
        
    def test_solve_reverse (self) :
        r = StringIO.StringIO("1000 256\n")
        w = StringIO.StringIO()
        collatz_solve(r, w)
        self.assert_(w.getvalue() == "1000 256 179\n")
        
    def test_solve_full_range (self) :
        r = StringIO.StringIO("1 1000000\n")
        w = StringIO.StringIO()
        collatz_solve(r, w)
        self.assert_(w.getvalue() == "1 1000000 525\n")

# ----
# main
# ----

print "TestCollatz.py"
unittest.main()
print "Done."
