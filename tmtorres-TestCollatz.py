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

from Collatz import collatz_read, collatz_eval, collatz_print, collatz_solve, collatz_len

# -----------
# TestCollatz
# -----------

class TestCollatz (unittest.TestCase) :
   # ----
   # read
   # ----

   def test_read_1 (self) :
       r = StringIO.StringIO("1 10\n")
       a = [0, 0]
       b = collatz_read(r, a)
       self.assert_(b    == True)
       self.assert_(a[0] ==  1)
       self.assert_(a[1] == 10)


   def test_read_2 (self) :
       r = StringIO.StringIO("12 21\n")
       a = [0, 0]
       b = collatz_read(r, a)
       self.assert_(b    == True)
       self.assert_(a[0] ==  12)
       self.assert_(a[1] == 21)

   def test_read_3 (self) :
       r = StringIO.StringIO("160 210\n")
       a = [0, 0]
       b = collatz_read(r, a)
       self.assert_(b    == True)
       self.assert_(a[0] ==  160)
       self.assert_(a[1] == 210)

   # ---
   # len
   # ---
   def test_len_1 (self) :
       v = collatz_len(1, 10)
       self.assert_(v == 20)

   def test_len_2 (self) :
       v = collatz_len(100, 200)
       self.assert_(v == 125)

   def test_len_3 (self) :
       v = collatz_len(201, 210)
       self.assert_(v == 89)

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

   # -----
   # print
   # -----

   def test_print_1 (self) :
       w = StringIO.StringIO()
       collatz_print(w, 1, 10, 20)
       self.assert_(w.getvalue() == "1 10 20\n")

   def test_print_2 (self) :
       w = StringIO.StringIO()
       collatz_print(w, 100, 200, 125)
       self.assert_(w.getvalue() == "100 200 125\n")

   def test_print_3 (self) :
       w = StringIO.StringIO()
       collatz_print(w, 900, 1000, 174)
       self.assert_(w.getvalue() == "900 1000 174\n")

   # -----
   # solve
   # -----

   def test_solve_1 (self) :
       r = StringIO.StringIO("1 10\n100 200\n201 210\n900 1000\n")
       w = StringIO.StringIO()
       collatz_solve(r, w)
       self.assert_(w.getvalue() == "1 10 20\n100 200 125\n201 210 89\n900 1000 174\n")

   def test_solve_2 (self) :
       r = StringIO.StringIO("")
       w = StringIO.StringIO()
       collatz_solve(r, w)
       self.assert_(w.getvalue() == "")

   def test_solve_3 (self) :
       r = StringIO.StringIO("200 100")
       w = StringIO.StringIO()
       collatz_solve(r, w)
       self.assert_(w.getvalue() == "200 100 125\n")

# ----
# main
# ----

print "TestCollatz.py"
unittest.main()
print "Done."