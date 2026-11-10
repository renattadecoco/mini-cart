import unittest
from cart.text import slugify

class TestSlugify(unittest.TestCase):
    def test_basic(self):
        self.assertEqual(slugify("Hello World"), "hello-world")
    def test_collapse(self):
        self.assertEqual(slugify("Hello,  World!!"), "hello-world")
    def test_trim(self):
        self.assertEqual(slugify("  --Start & End--  "), "start-end")
    def test_accents(self):
        self.assertEqual(slugify("Café au lait"), "cafe-au-lait")
    def test_empty(self):
        self.assertEqual(slugify("!!!"), "")

if __name__ == "__main__":
    unittest.main()
