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

from Collatz import collatz_read, collatz_eval, collatz_print, collatz_solve, collatz_find_length

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


    #---------------------------
    #Created unittests for read
    #---------------------------

    # big before small
    def test_read_1 (self) :
	r = StringIO.StringIO("142 69\n")
	a = [0, 0]
	b = collatz_read(r, a)
	self.assert_(b == True)
	self.assert_(a[0] == 142)
	self.assert_(a[1] == 69)


     # Big before small
    def test_read_2 (self) :
	r = StringIO.StringIO("15 3\n")
	a = [0, 0]
	b = collatz_read(r, a)
	self.assert_(b == True)
	self.assert_(a[0] == 15)
	self.assert_(a[1] == 3)
   
    # Same number
    def test_read_3 (self):
	r = StringIO.StringIO("1 1\n")
	a = [0, 0]
	b = collatz_read(r, a)
	self.assert_(b == True)
	self.assert_(a[0] == 1)
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


    #---------------------------
    #Created unittests for eval
    #---------------------------

    # Base case of 1
    def test_eval_5 (self) :
        v = collatz_eval(1, 1)
        self.assert_(v == 1)

    # Large number range
    def test_eval_6 (self) :
        v = collatz_eval(800000, 900000)
        self.assert_(v == 525)

    # Two numbers switched
    def test_eval_7 (self) :
        v = collatz_eval(225, 224)
        self.assert_(v == 53)



    # -----
    # print
    # -----

    def test_print_1 (self) :
        w = StringIO.StringIO()
        collatz_print(w, 1, 10, 20)
        self.assert_(w.getvalue() == "1 10 20\n")


    #---------------------------
    #Created unittests for print
    #---------------------------

    #   random numerical input 
    def test_print_2 (self) :
        w = StringIO.StringIO()
        collatz_print(w, 17829, 390514, 443)
        self.assert_(w.getvalue() == "17829 390514 443\n")

    # Base case of 1
    def test_print_3 (self) :
        w = StringIO.StringIO()
        collatz_print(w, 1, 1, 1)
        self.assert_(w.getvalue() == "1 1 1\n")


     # Random Range 
    def test_print_4 (self) :
        w = StringIO.StringIO()
        collatz_print(w, 35043, 209543, 383)
        self.assert_(w.getvalue() == "35043 209543 383\n")




    # -----
    # solve
    # -----

    def test_solve_1 (self) :
        r = StringIO.StringIO("1 10\n100 200\n201 210\n900 1000\n")
        w = StringIO.StringIO()
        collatz_solve(r, w)
        self.assert_(w.getvalue() == "1 10 20\n100 200 125\n201 210 89\n900 1000 174\n")


    #---------------------------
    #Created unittests for solve
    #---------------------------

    # one input reversed
    def test_solve_2 (self) :
        r = StringIO.StringIO("10 1\n")
        w = StringIO.StringIO()
        collatz_solve(r, w)
        self.assert_(w.getvalue() == "10 1 20\n")

    def test_solve_3 (self) :
        r = StringIO.StringIO("513662 442902\n44088 577929\n23605 268177\n")
        w = StringIO.StringIO()
        collatz_solve(r, w)
        self.assert_(w.getvalue() == "513662 442902 470\n44088 577929 470\n23605 268177 443\n")


    # 9 inputs
    def test_solve_4 (self) :
        r = StringIO.StringIO("513662 442902\n44088 577929\n23605 268177\n513662 442902\n44088 577929\n23605 268177\n513662 442902\n44088 577929\n23605 268177\n")

        w = StringIO.StringIO()
        collatz_solve(r, w)
        self.assert_(w.getvalue() == "513662 442902 470\n44088 577929 470\n23605 268177 443\n513662 442902 470\n44088 577929 470\n23605 268177 443\n513662 442902 470\n44088 577929 470\n23605 268177 443\n")


    #----------------------
    #test_find_cycle_length
    #----------------------

    #base case test
    def test_populate_helper_1(self) :
        start = 1
        result = collatz_find_length(start)
        self.assert_(result == 1)

    #last index in cache
    def test_populate_helper_2(self) :
        start = 999999
        result = collatz_find_length(start)
        self.assert_(result == 259)

    #Index oustide of cache
    def test_populate_helper_3(self) :
         l = 2094992
         self.assert_(collatz_find_length(l) == 136)





# ----
# main
# ----

print "TestCollatz.py"
unittest.main()
print "Done."
