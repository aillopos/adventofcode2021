import unittest
import giant_squid


class TestBingo(unittest.TestCase):
    def test_bingo(self):
        nd, b = giant_squid.read_input("test_data.txt")
        first, last = giant_squid.tmp(nd, b)
        self.assertEqual(24, first[giant_squid.key_number_drawn],
                         "last drawn number for best board should be: 24")
        self.assertEqual(188, first[giant_squid.key_sum_unmarked],
                         "sum of unmarked numbers on best board should be: 188")
        self.assertEqual(13, last[giant_squid.key_number_drawn],
                         "last drawn number for worst board should be: 13")
        self.assertEqual(148, last[giant_squid.key_sum_unmarked],
                         "sum of unmarked numbers on worst board should be: 148")


if __name__ == '__main__':
    unittest.main()
