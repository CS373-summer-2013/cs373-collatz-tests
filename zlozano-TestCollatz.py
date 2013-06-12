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

    def test_read (self) :                # Default test
        r = StringIO.StringIO("1 10\n")
        a = [0, 0]
        b = collatz_read(r, a)
        self.assert_(b    == True)
        self.assert_(a[0] ==  1)
        self.assert_(a[1] == 10)

    def test_read_2 (self) :              # Multiple line test
        r = StringIO.StringIO("2 4\n 6 8\n 10 12\n")
        a = [0, 0]
        b = [0, 0]
        c = [0, 0]
        d = collatz_read(r, a)
        e = collatz_read(r, b)
        f = collatz_read(r, c)
        self.assert_(d    == True)
        self.assert_(e    == True)
        self.assert_(f    == True)
        self.assert_(a[0] == 2)
        self.assert_(a[1] == 4)
        self.assert_(b[0] == 6)
        self.assert_(b[1] == 8)
        self.assert_(c[0] == 10)
        self.assert_(c[1] == 12)

    def test_read_3 (self) :              # Reverse read test
        r = StringIO.StringIO("1000 30\n")
        a = [0, 0]
        b = collatz_read(r, a)
        self.assert_(b    == True)
        self.assert_(a[0] == 1000)        
        self.assert_(a[1] ==   30)        

    def test_read_4 (self) :              # Nill test
        r = StringIO.StringIO("")
        a = [0, 0]
        b = collatz_read(r, a)
        self.assert_(b    == False)

    # ----
    # eval
    # ----

    def test_eval_1 (self) :              # Original test
        v = collatz_eval(1, 10)
        self.assert_(v == 20)

    def test_eval_2 (self) :              # Original test
        v = collatz_eval(100, 200)
        self.assert_(v == 125)

    def test_eval_3 (self) :              # Original test
        v = collatz_eval(201, 210)
        self.assert_(v == 89)

    def test_eval_4 (self) :              # Original test
        v = collatz_eval(900, 1000)
        self.assert_(v == 174)

    def test_eval_5 (self) :              # Decrementing range test
        v = collatz_eval(1000, 900)
        self.assert_(v == 174)

    def test_eval_6 (self) :              # Equal endpoints test
        v = collatz_eval(10, 10)
        self.assert_(v == 7)

    def test_eval_7 (self) :              # Input 1 test
        v = collatz_eval(1, 1)
        print str(v)
        self.assert_(v == 1)

    # ------------
    # cycle_length
    # ------------
    def test_cycle_length_1 (self) :
        v = cycle_length(5)
        self.assert_(v == 6)
    def test_cycle_length_2 (self) :
        v = cycle_length(10)
        self.assert_(v == 7)
    def test_cycle_length_3 (self) :
        v = cycle_length(3)
        self.assert_(v == 8)
    # -----
    # print
    # -----

    def test_print (self) :
        w = StringIO.StringIO()
        collatz_print(w, 1, 10, 20)
        self.assert_(w.getvalue() == "1 10 20\n")

    def test_print_2 (self) :             # Two line print
        w = StringIO.StringIO()
        collatz_print(w, 1, 1, 1)
        collatz_print(w, 1, 10, 20)
        self.assert_(w.getvalue() == "1 1 1\n1 10 20\n")

    def test_print_3 (self) :             # Multi-line print
        w = StringIO.StringIO()
        collatz_print(w, 1, 1, 1)
        collatz_print(w, 1, 10, 20)
        collatz_print(w, 900, 1000, 174)
        self.assert_(w.getvalue() == "1 1 1\n1 10 20\n900 1000 174\n")

    def test_print_4 (self) :             # Nill print
        w = StringIO.StringIO()
        collatz_print(w, "", "", "")
        self.assert_(w.getvalue() == "  \n")
    
    # -----
    # solve
    # -----

    def test_solve (self) :
        r = StringIO.StringIO("1 10\n100 200\n201 210\n900 1000\n")
        w = StringIO.StringIO()
        collatz_solve(r, w)
        self.assert_(w.getvalue() == "1 10 20\n100 200 125\n201 210 89\n900 1000 174\n")

    def test_solve_2 (self) :             # Max cycle length of 1 == 1
        r = StringIO.StringIO("1 1\n")
        w = StringIO.StringIO()
        collatz_solve(r, w)
        self.assert_(w.getvalue() == "1 1 1\n")

    def test_solve_3 (self) :             # Solve from hi to lo range
        r = StringIO.StringIO("10 1\n")
        w = StringIO.StringIO()
        collatz_solve(r, w)
        self.assert_(w.getvalue() == "10 1 20\n")

    def test_solve_4 (self) :             # Solve largest input
        r = StringIO.StringIO("1000000 1000000\n")
        w = StringIO.StringIO()
        collatz_solve(r, w)
        self.assert_(w.getvalue() == "1000000 1000000 153\n")

# ----
# main
# ----

print "TestCollatz.py"
unittest.main()
print "Done."
