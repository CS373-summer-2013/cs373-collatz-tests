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
    
    # Ensure 'collatz_read' can properly handle out of range inputs
    def test_read_2(self):
        r = StringIO.StringIO('1 -1\n') 
        a = [0, 0]
        failure = False
        try:
            b = collatz_read(r, a)
        except Exception, e:
            self.assert_(type(e) == AssertionError)
            failure = True
            b = False
        
        self.assert_(failure == True)
        self.assert_(b == False)
        self.assert_(a[0] == 1)
        self.assert_(a[1] == -1)
    
    # Ensure that 'collatz_read' can properly handle non-integer inputs
    def test_read_3(self):
        r = StringIO.StringIO('0.01 55 \n')
        a = [0, 0]
        
        failure = False
        try:
            b = collatz_read(r,a)
        except Exception, e:
            self.assert_(type(e) == ValueError)
            failure = True
            b = False
            
        self.assert_(failure == True)
        self.assert_(b == False)
        self.assert_(a[0] == 0)
        self.assert_(a[1] == 0)
    
    # Ensure that 'collatz_read' can terminate
    def test_read_4(self):
        r = StringIO.StringIO('')
        a = [ 0, 0 ]
        b = collatz_read(r, a)
        
        self.assert_(b == False)
        self.assert_(a[0] == 0)
        self.assert_(a[0] == 0)


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
        try:
            v = collatz_eval(-1, 100)
            self.assert_(False) # Should never get to this point. 'collatz_eval' must fail
        except Exception, e:
            self.assert_(type(e) == AssertionError)
            
    def test_eval_6(self):
        v = collatz_eval(1, 1)
        self.assert_(v == 1)
        
    def test_eval_7(self):
        v = collatz_eval(10, 1)
        self.assert_(v == 20)
            
    # -----
    # print
    # -----

    def test_print (self) :
        w = StringIO.StringIO()
        collatz_print(w, 1, 10, 20)
        self.assert_(w.getvalue() == "1 10 20\n")
    
    def test_print_2(self):
        w = StringIO.StringIO()
        collatz_print(w, 100, 200, 125)
        self.assert_(w.getvalue() == '100 200 125\n')
    
    def test_print_3(self):
        w = StringIO.StringIO()
        collatz_print(w, 201, 210, 89)
        self.assert_(w.getvalue() == '201 210 89\n')

    # -----
    # solve
    # -----

    def test_solve (self) :
        r = StringIO.StringIO("1 10\n100 200\n201 210\n900 1000\n")
        w = StringIO.StringIO()
        collatz_solve(r, w)
        self.assert_(w.getvalue() == "1 10 20\n100 200 125\n201 210 89\n900 1000 174\n")
    
    def test_solve_2(self):
        r = StringIO.StringIO("")
        w = StringIO.StringIO()
        collatz_solve(r, w)
        self.assert_(w.getvalue() == "")
    
    def test_solve_3(self):
        r = StringIO.StringIO("1 1\n")
        w = StringIO.StringIO()
        collatz_solve(r, w)
        self.assert_(w.getvalue() == "1 1 1\n")
    
# ----
# main
# ----

print "TestCollatz.py"
unittest.main()
print "Done."
