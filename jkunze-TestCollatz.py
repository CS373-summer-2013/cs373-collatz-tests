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

from Collatz import collatz_read, collatz_eval, collatz_print, collatz_solve, collatz_length, collatz_init_cache

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

    def test_eval_backwards (self) :
        i = 1
        j = 100
        while i < j :
            self.assert_(collatz_eval(i, j) == collatz_eval(j, i))
            i += 1

    # -----
    # print
    # -----

    def test_print (self) :
        w = StringIO.StringIO()
        collatz_print(w, 1, 10, 20)
        self.assert_(w.getvalue() == "1 10 20\n")

    def test_print_wrong (self) :
        w = StringIO.StringIO()
        collatz_print(w, 9000000, 4, 33)
        self.assert_(w.getvalue() == "9000000 4 33\n")

    # -----
    # solve
    # -----

    def test_solve (self) :
        r = StringIO.StringIO("1 10\n100 200\n201 210\n900 1000\n")
        w = StringIO.StringIO()
        collatz_solve(r, w)
        self.assert_(w.getvalue() == "1 10 20\n100 200 125\n201 210 89\n900 1000 174\n")

    def test_solve_backwards (self) :
        r = StringIO.StringIO("10 1\n200 100\n210 201\n1000 900\n")
        w = StringIO.StringIO()
        collatz_solve(r, w)
        self.assert_(w.getvalue() == "10 1 20\n200 100 125\n210 201 89\n1000 900 174\n")

    def test_solve_same (self) :
        r = StringIO.StringIO("1 1\n2 2\n3 3\n4 4\n800 800\n")
        w = StringIO.StringIO()
        collatz_solve(r, w)
        self.assert_(w.getvalue() == "1 1 1\n2 2 2\n3 3 8\n4 4 3\n800 800 29\n")

    # -----
    # length
    # -----

    def test_length_powers (self) :
        self.assert_(collatz_length(1) == 1)
        self.assert_(collatz_length(2) == 2)
        self.assert_(collatz_length(4) == 3)
        self.assert_(collatz_length(8) == 4)
        self.assert_(collatz_length(16) == 5)
        self.assert_(collatz_length(32) == 6)
        self.assert_(collatz_length(64) == 7)
        self.assert_(collatz_length(128) == 8)
        self.assert_(collatz_length(256) == 9)
        self.assert_(collatz_length(512) == 10)
        self.assert_(collatz_length(1024) == 11)
        self.assert_(collatz_length(2048) == 12)
        self.assert_(collatz_length(4096) == 13)
        self.assert_(collatz_length(8192) == 14)
        self.assert_(collatz_length(16384) == 15)
        self.assert_(collatz_length(32768) == 16)
        self.assert_(collatz_length(65536) == 17)
        self.assert_(collatz_length(131072) == 18)
        self.assert_(collatz_length(262144) == 19)
        self.assert_(collatz_length(524288) == 20)

    def test_length_misc (self) :
        self.assert_(collatz_length(3) == 8)
        self.assert_(collatz_length(10) == 7)
        self.assert_(collatz_length(5) == 6)
        self.assert_(collatz_length(6) == 9)
        self.assert_(collatz_length(7) == 17)
        self.assert_(collatz_length(22) == 16)
        self.assert_(collatz_length(11) == 15)
        self.assert_(collatz_length(34) == 14)
        self.assert_(collatz_length(17) == 13)
        self.assert_(collatz_length(52) == 12)
        self.assert_(collatz_length(26) == 11)
        self.assert_(collatz_length(13) == 10)
        self.assert_(collatz_length(40) == 9)
        self.assert_(collatz_length(20) == 8)
        self.assert_(collatz_length(9) == 20)
        self.assert_(collatz_length(28) == 19)
        self.assert_(collatz_length(14) == 18)
        self.assert_(collatz_length(12) == 10)

    def test_length_large (self) :
        self.assert_(collatz_length(999990) == 166)
        self.assert_(collatz_length(999991) == 166)
        self.assert_(collatz_length(999992) == 114)
        self.assert_(collatz_length(999993) == 166)
        self.assert_(collatz_length(999994) == 114)
        self.assert_(collatz_length(999995) == 259)
        self.assert_(collatz_length(999996) == 114)
        self.assert_(collatz_length(999997) == 114)
        self.assert_(collatz_length(999998) == 259)
        self.assert_(collatz_length(999999) == 259)
        self.assert_(collatz_length(1000000) == 153)

    def test_length_doubling (self) :
        i = 2
        while i < 1000001 :
            self.assert_(collatz_length(i)+1 == collatz_length(i*2))
            i += 2

    def test_length_odds (self) :
        i = 3
        while i < 100000 :
            self.assert_(collatz_length(i)-1 == collatz_length((i*3)+1))
            i += 2

    def test_solve_length_sanity (self) :
        i = 1
        while i < 1000 :
            r = StringIO.StringIO(str(i) + " " + str(i))
            w = StringIO.StringIO()
            collatz_solve(r, w)
            a = w.getvalue().split()
            self.assert_(a[0] == a[1])
            self.assert_(a[2] == str(collatz_length(i)))
            i += 1

    def test_solve_length_sanity_high (self) :
        i = 999000
        while i < 1000000 :
            r = StringIO.StringIO(str(i) + " " + str(i))
            w = StringIO.StringIO()
            collatz_solve(r, w)
            a = w.getvalue().split()
            self.assert_(a[0] == a[1])
            self.assert_(a[2] == str(collatz_length(i)))
            i += 1

# ----
# main
# ----

print "TestCollatz.py"
collatz_init_cache()
unittest.main()
print "Done."
