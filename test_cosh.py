"""To find the cosh(x) for the given value say x """

import unittest
import cosh_logic_program


class TestCosh(unittest.TestCase):
    """class for unittesting"""

    def test_for_positive_number(self):
        """test case for checking a Positive number"""
        self.assertEqual(cosh_logic_program.trig_cosh(1), 1.5430798443133158)

    def test_for_negative_number(self):
        """test case for checking a Positive number"""
        self.assertEqual(cosh_logic_program.trig_cosh(-2), 3.762190811852014)

    def test_for_positive__floatingpoint_number(self):
        """test case for checking a Positive floating number"""
        self.assertEqual(cosh_logic_program.trig_cosh(1.8), 3.1074696140087874)

    def test_for_Zero(self):
        """test case for checking for Zero"""
        self.assertEqual(cosh_logic_program.trig_cosh(0), 1)


if __name__ == '__main__':
    unittest.main()
