#!/usr/bin/env python
import StringIO
import unittest

from Collatz import cycle_len, cycle_lens, BUCKET_SIZE, PRE_START, \
        max_cycle_len, collatz_read, collatz_eval, collatz_print, \
        collatz_solve, pairs, output_result
from generate_caches import solutions, maxs, pre


class TestCollatz(unittest.TestCase):
    def assert_deep_equal(self, iter1, iter2):
        """
        compare two iterables recursively. if the items in the lists are
        iterable, compare each of those as well
        iter1: the first iterable
        iter2: the second iterable
        returns: None
        """
        # convert to lists so we can compare length
        iter1 = [i1 for i1 in iter1]
        iter2 = [i2 for i2 in iter2]
        self.assertEqual(len(iter1), len(iter2))
        for i1, i2 in zip(iter1, iter2):
            if hasattr(i1, '__iter__') and hasattr(i2, '__iter__'):
                self.assert_deep_equal(i1, i2)
            else:
                self.assertEqual(i1, i2)

    def test_cycle_len_22(self):
        self.assertEqual(cycle_len(22), 16)

    def test_cycle_len_10(self):
        self.assertEqual(cycle_len(10), 7)

    def test_cycle_len_5(self):
        self.assertEqual(cycle_len(5), 6)

    def test_cycle_len_999999(self):
        self.assertEqual(cycle_len(999999), 259)

    def test_cycle_lens(self):
        self.assert_deep_equal(cycle_lens(5, 10), [6, 9, 17, 4, 20, 7])

    def test_cycle_lens_throws_for_input_too_small(self):
        self.assertRaises(AssertionError, lambda: cycle_lens(0, 2))

    def test_cycle_lens_reversed_inputs(self):
        self.assert_deep_equal(cycle_lens(10, 5), [6, 9, 17, 4, 20, 7])

    def test_max_cycle_len(self):
        self.assertEqual(max_cycle_len(95, 205), 125)

    def test_max_cycle_len_with_inputs_reversed(self):
        self.assertEqual(max_cycle_len(5, 10), 20)

    def test_max_cycle_len_throws_if_input_too_small(self):
        self.assertRaises(AssertionError, lambda: max_cycle_len(0, 5))

    def test_collatz_read_one(self):
        r = StringIO.StringIO('1 10\n')
        a = [None, None]
        collatz_read(r, a)
        self.assert_deep_equal(a, [1, 10])

    def test_collatz_read_returns_false_for_no_more_data(self):
        r = StringIO.StringIO()
        a = [None, None]
        ret = collatz_read(r, a)
        self.assertEqual(ret, False)

    def test_collatz_read_throws_on_invalid_input(self):
        r = StringIO.StringIO('-1 -2\n')
        self.assertRaises(AssertionError, lambda: collatz_read(r, [0, 0]))

    def test_collatz_eval(self):
        self.assertEqual(collatz_eval(95, 205), 125)

    def test_collatz_eval_with_inputs_reversed(self):
        self.assertEqual(collatz_eval(5, 10), 20)

    def test_collatz_eval_throws_if_input_too_small(self):
        self.assertRaises(AssertionError, lambda: collatz_eval(0, 5))
        self.assertRaises(AssertionError, lambda: collatz_eval(5, 0))

    def test_collatz_print(self):
        out = StringIO.StringIO()
        collatz_print(out, 5, 10, 20)
        out.seek(0)
        self.assertEqual(out.read().strip(), '5 10 20')

    def test_collatz_print_throws_if_not_given_filelike_obj(self):
        self.assertRaises(
            AssertionError, lambda: collatz_print(None, 5, 10, 20))

    def test_collatz_print_called_multiple_times(self):
        out = StringIO.StringIO()
        collatz_print(out, 5, 10, 20)
        collatz_print(out, 3, 7, 17)
        out.seek(0)
        self.assertEqual(out.read().strip(), '5 10 20\n3 7 17')

    def test_collatz_solve(self):
        inf = StringIO.StringIO('5 10\n3 7')
        out = StringIO.StringIO()
        collatz_solve(inf, out)
        out.seek(0)
        self.assertEqual(out.read().strip(), '5 10 20\n3 7 17')

    def test_collatz_solve_varying_whitespace(self):
        inf = StringIO.StringIO('5\t10\n3  7\n')
        out = StringIO.StringIO()
        collatz_solve(inf, out)
        out.seek(0)
        self.assertEqual(out.read().strip(), '5 10 20\n3 7 17')

    def test_collatz_solve_empty_newlines(self):
        inf = StringIO.StringIO('5 10\n3 7\n\n\n')
        out = StringIO.StringIO()
        collatz_solve(inf, out)
        out.seek(0)
        self.assertEqual(out.read().strip(), '5 10 20\n3 7 17')

    def test_collatz_solve_empty_leading_newlines(self):
        inf = StringIO.StringIO('\n\n\n5 10\n3 7')
        out = StringIO.StringIO()
        collatz_solve(inf, out)
        out.seek(0)
        self.assertEqual(out.read().strip(), '')

    def test_collatz_solve_reversed_input(self):
        inf = StringIO.StringIO('10 5\n3 7')
        out = StringIO.StringIO()
        collatz_solve(inf, out)
        out.seek(0)
        self.assertEqual(out.read().strip(), '10 5 20\n3 7 17')

    def test_collatz_solve_throws_for_invalid_inputs(self):
        self.assertRaises(AssertionError, lambda: collatz_solve(0, 0))

    def test_pairs(self):
        r = StringIO.StringIO('1 10\n')
        self.assert_deep_equal(pairs(r), [[1, 10]])

    def test_multiple_pairs(self):
        r = StringIO.StringIO('1 10\n3 7')
        self.assert_deep_equal(pairs(r), [[1, 10], [3, 7]])

    def test_varying_whitespace(self):
        r = StringIO.StringIO('1  10\n3\t7')
        self.assert_deep_equal(pairs(r), [[1, 10], [3, 7]])

    def test_empty_input_to_pairs(self):
        r = StringIO.StringIO('')
        self.assert_deep_equal(pairs(r), [])

    def test_empty_line_to_pairs(self):
        r = StringIO.StringIO('\n\n1 10\n')
        self.assert_deep_equal(pairs(r), [[1, 10]])

    def test_output_result(self):
        out = StringIO.StringIO()
        output_result(out, [5, 10], 20)
        out.seek(0)
        self.assertEqual(out.read().strip(), '5 10 20')

    def test_output_result_throws_if_not_given_filelike_obj(self):
        self.assertRaises(
            AssertionError, lambda: output_result(None, [5, 10], 20))

    def test_output_result_called_multiple_times(self):
        out = StringIO.StringIO()
        output_result(out, [5, 10], 20)
        output_result(out, [3, 7], 17)
        out.seek(0)
        self.assertEqual(out.read().strip(), '5 10 20\n3 7 17')

    # def test_maxs(self):
    #     ss = tuple(solutions())
    #     for i,m in enumerate(maxs()):
    #         self.assertEqual(
    #             max(ss[i*BUCKET_SIZE:i*BUCKET_SIZE+BUCKET_SIZE]), m)

    # def test_pre(self):
    #     for i,p in enumerate(pre()):
    #         self.assertEqual(cycle_len(PRE_START+i), p)


if __name__ == '__main__':
    unittest.main()
