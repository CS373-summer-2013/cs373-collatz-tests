#!/usr/bin/env python

# ----------------------------
# cs373-collatz/TestCollatz.py
# (C)2013 Stephen Chiang
# ----------------------------

'''
To test the program:
    % python TestCollatz.py >& TestCollatz.py.out
    % chmod ugo+x TestCollatz.py
    % TestCollatz.py >& TestCollatz.py.out
'''

# -------
# imports
# -------
import StringIO, unittest
from Collatz import collatz_read, collatz_eval, collatz_print, collatz_solve

# -----------
# TestCollatz
# -----------
class TestCollatz (unittest.TestCase):
    # ----
    # read
    # ----
    def test_read_ascending(self):
        r = StringIO.StringIO("1 10\n")
        a = [0, 0]
        b = collatz_read(r, a)
        self.assert_(b    == True)
        self.assert_(a[0] ==  1)
        self.assert_(a[1] == 10)

    def test_read_descending(self):
        r = StringIO.StringIO("10 1\n")
        a = [0, 0]
        b = collatz_read(r, a)
        self.assert_(b    == True)
        self.assert_(a[0] == 10)
        self.assert_(a[1] ==  1)

    def test_read_duplicates(self):
        r = StringIO.StringIO("5 5\n")
        a = [0, 0]
        b = collatz_read(r, a)
        self.assert_(b    == True)
        self.assert_(a[0] ==  5)
        self.assert_(a[1] ==  5)

    # ----
    # eval
    # ----
    def test_eval_example_1(self):
        v = collatz_eval(1, 10)
        self.assert_(v == 20)

    def test_eval_example_2(self):
        v = collatz_eval(100, 200)
        self.assert_(v == 125)

    def test_eval_example_3(self):
        v = collatz_eval(201, 210)
        self.assert_(v == 89)

    def test_eval_example_4(self):
        v = collatz_eval(900, 1000)
        self.assert_(v == 174)

    def test_eval_descending_1(self):
        v = collatz_eval(10, 1)
        self.assert_(v == 20)

    def test_eval_descending_2(self):
        v = collatz_eval(2, 1)
        self.assert_(v == 2)

    def test_eval_compare_to_descending(self):
        v = collatz_eval(1, 2)
        self.assert_(v == 2)

    def test_eval_duplicates_1(self):
        v = collatz_eval(5, 5)
        self.assert_(v == 6)

    def test_eval_duplicates_2(self):
        v = collatz_eval(1, 1)
        self.assert_(v == 1)

    # -----
    # print
    # -----
    def test_print_example_1(self):
        w = StringIO.StringIO()
        collatz_print(w, 1, 10, 20)
        self.assert_(w.getvalue() == "1 10 20\n")

    def test_print_example_2(self):
        w = StringIO.StringIO()
        collatz_print(w, 100, 200, 125)
        self.assert_(w.getvalue() == "100 200 125\n")

    def test_print_example_3(self):
        w = StringIO.StringIO()
        collatz_print(w, 201, 210, 89)
        self.assert_(w.getvalue() == "201 210 89\n")

    def test_print_example_4(self):
        w = StringIO.StringIO()
        collatz_print(w, 900, 1000, 174)
        self.assert_(w.getvalue() == "900 1000 174\n")

    def test_print_descending(self):
        w = StringIO.StringIO()
        collatz_print(w, 10, 1, 20)
        self.assert_(w.getvalue() == "10 1 20\n")

    def test_print_duplicates(self):
        w = StringIO.StringIO()
        collatz_print(w, 5, 5, 6)
        self.assert_(w.getvalue() == "5 5 6\n")

    # -----
    # solve
    # -----
    def test_solve_example(self):
        r = StringIO.StringIO("1 10\n100 200\n201 210\n900 1000\n")
        w = StringIO.StringIO()
        collatz_solve(r, w)
        self.assert_(w.getvalue() == "1 10 20\n100 200 125\n201 210 89\n900 1000 174\n")

    def test_solve_descending(self):
        r = StringIO.StringIO("10 1\n200 100\n210 201\n1000 900\n")
        w = StringIO.StringIO()
        collatz_solve(r, w)
        self.assert_(w.getvalue() == "10 1 20\n200 100 125\n210 201 89\n1000 900 174\n")

    def test_solve_duplicates(self):
        r = StringIO.StringIO("1 1\n5 5\n10 10\n2 2\n")
        w = StringIO.StringIO()
        collatz_solve(r, w)
        self.assert_(w.getvalue() == "1 1 1\n5 5 6\n10 10 7\n2 2 2\n")

# ----
# main
# ----
print "TestCollatz.py"
unittest.main()
print "Done."