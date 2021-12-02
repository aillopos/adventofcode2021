import unittest
import dive


class TestSonarSweep(unittest.TestCase):
    def test_count_step_incs(self):
        d = dive.read_input("test_data.txt")
        aim, depth, forward = dive.get_directions(d)

        self.assertEqual(15, forward,
                         "horizontal position should be: 15")
        self.assertEqual(10, aim,
                         "aim should be: 10")
        self.assertEqual(60, depth,
                         "depth should be: 60")


if __name__ == '__main__':
    unittest.main()