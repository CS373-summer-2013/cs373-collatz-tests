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

from Collatz import collatz_read, collatz_eval, collatz_print, collatz_solve, collatz_cycle

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

    def test_read_descend (self) :
        r = StringIO.StringIO("10 1\n")
        a = [0, 0]
        b = collatz_read(r, a)
        self.assert_(b    == True)
        self.assert_(a[0] ==  10)
        self.assert_(a[1] == 1)
        
    def test_read_long (self) :
        r = StringIO.StringIO("1 100\n")
        a = [0, 0]
        b = collatz_read(r, a)
        self.assert_(b    == True)
        self.assert_(a[0] ==  1)
        self.assert_(a[1] == 100)
        
    def test_read_same (self) :
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
        
    #Should be the same as above since same range
    def test_eval_4descend (self) :
        v = collatz_eval(1000, 900)
        self.assert_(v == 174)
        
    def test_eval_3descend (self) :
        v = collatz_eval(210, 201)
        self.assert_(v == 89)
        
    #Duplicate input and base case test
    def test_eval_7 (self) :
        v = collatz_eval(1, 1)
        self.assert_(v == 1)


    # -----
    # cycle (my function)
    # -----
    
    #base case
    def test_cycle_1 (self) :
        v = collatz_cycle(1)
        self.assert_(v == 1)
        
    def test_cycle_2 (self) :
        v = collatz_cycle(2)
        self.assert_(v == 2)

    def test_cycle_3 (self) :
        v = collatz_cycle(3)
        self.assert_(v == 8)
    
    def test_cycle_4 (self) :
        v = collatz_cycle(4)
        self.assert_(v == 3)
    
    def test_cycle_5 (self) :
        v = collatz_cycle(5)
        self.assert_(v == 6)
    
    def test_cycle_6 (self) :
        v = collatz_cycle(6)
        self.assert_(v == 9)    
    




    # -----
    # print
    # -----

    def test_print (self) :
        w = StringIO.StringIO()
        collatz_print(w, 1, 10, 20)
        self.assert_(w.getvalue() == "1 10 20\n")
        
    def test_print1 (self) :
        w = StringIO.StringIO()
        collatz_print(w, 6, 6, 9)
        self.assert_(w.getvalue() == "6 6 9\n")

    def test_print2 (self) :
        w = StringIO.StringIO()
        collatz_print(w, 5, 5, 6)
        self.assert_(w.getvalue() == "5 5 6\n")
        
    def test_print3 (self) :
        w = StringIO.StringIO()
        collatz_print(w, 4, 4, 3)
        self.assert_(w.getvalue() == "4 4 3\n")

    # -----
    # solve
    # -----

    def test_solve (self) :
        r = StringIO.StringIO("1 10\n100 200\n201 210\n900 1000\n")
        w = StringIO.StringIO()
        collatz_solve(r, w)
        self.assert_(w.getvalue() == "1 10 20\n100 200 125\n201 210 89\n900 1000 174\n")
    
    #Backwards and inverted    
    def test_solve1 (self) :
        r = StringIO.StringIO("1000 900\n210 201\n200 100\n10 1\n")
        w = StringIO.StringIO()
        collatz_solve(r, w)
        self.assert_(w.getvalue() == "1000 900 174\n210 201 89\n200 100 125\n10 1 20\n")
     

# ----
# main
# ----

print "TestCollatz.py"
unittest.main()
print "Done."
