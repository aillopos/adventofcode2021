import unittest
import binary_diagnostic


class TestAir(unittest.TestCase):
    def test_gamma(self):
        d = binary_diagnostic.read_input("test_data.txt")
        g, e = binary_diagnostic.calc_gamma(d)
        self.assertEqual(22, g, "gamma should be: 22")
        self.assertEqual(9, e, "epsilon should be: 9")

    def test_get_air(self):
        d = binary_diagnostic.read_input("test_data.txt")
        o, co2 = binary_diagnostic.get_air(d)
        self.assertEqual(23, o, "oxygen should be: 23")
        self.assertEqual(10, co2, "co2 should be: 10")


if __name__ == '__main__':
    unittest.main()
