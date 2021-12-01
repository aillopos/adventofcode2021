import unittest
import sonar_sweep


class TestSonarSweep(unittest.TestCase):
    def test_count_step_incs(self):
        d = sonar_sweep.read_input("test_data.txt")
        expect = 7
        self.assertEqual(expect, sonar_sweep.count_incs(d),
                         "total no of increases should be: {}".format(expect))

    def test_count_slide_incs(self):
        d = sonar_sweep.read_input("test_data.txt")
        sw = sonar_sweep.create_window(3, d)
        expect = 5
        self.assertEqual(expect, sonar_sweep.count_incs(sw),
                         "total no of increases should be: {}".format(expect))


if __name__ == '__main__':
    unittest.main()
