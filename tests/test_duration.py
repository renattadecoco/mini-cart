import unittest
from cart.duration import parse_duration

class TestDuration(unittest.TestCase):
    def test_simple(self):
        self.assertEqual(parse_duration("45s"), 45)
        self.assertEqual(parse_duration("2h"), 7200)
    def test_combo(self):
        self.assertEqual(parse_duration("1h30m"), 5400)
        self.assertEqual(parse_duration("1h 5m 10s"), 3910)
    def test_case_and_spaces(self):
        self.assertEqual(parse_duration(" 2M 3S "), 123)
    def test_invalid(self):
        for bad in ["", "abc", "5x", "1h2h", "h", "1.5h", "-3m"]:
            with self.assertRaises(ValueError, msg=bad):
                parse_duration(bad)

if __name__ == "__main__":
    unittest.main()
