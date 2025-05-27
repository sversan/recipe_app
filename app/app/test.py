"""Sample test"""

from django.test import SimpleTestCase

from app import calc 

class CalcTests(SimpleTestCase):
    """Test Module"""

    def test_add_numbers(self):
        "Test Adding numbers together"

        res = calc.add(5,6)
        self.assertAlmostEqual(res, 11)