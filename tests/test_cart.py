import unittest
from decimal import Decimal
from cart.cart import Cart

class TestCart(unittest.TestCase):
    def test_money_exact(self):
        c = Cart()
        c.add("a", "0.10", 3)
        self.assertEqual(c.total(), Decimal("0.30"))
        self.assertIsInstance(c.total(), Decimal)
    def test_buy2get1(self):
        c = Cart()
        c.add("tee", "10.00", 7, buy2get1=True)  # 2 free
        self.assertEqual(c.total(), Decimal("50.00"))
    def test_buy2get1_merged_adds(self):
        c = Cart()
        c.add("tee", "10.00", 2, buy2get1=True)
        c.add("tee", "10.00", 1, buy2get1=True)
        self.assertEqual(c.total(), Decimal("20.00"))
    def test_coupon_after_promo(self):
        c = Cart()
        c.add("tee", "10.00", 3, buy2get1=True)
        c.add("mug", "5.55", 1)
        c.apply_coupon(10)
        self.assertEqual(c.total(), Decimal("23.00"))  # (20 + 5.55) * 0.9 = 22.995 -> 23.00
    def test_rounding_half_up(self):
        c = Cart()
        c.add("x", "0.125", 1)
        self.assertEqual(c.total(), Decimal("0.13"))
    def test_bad_qty(self):
        with self.assertRaises(ValueError):
            Cart().add("a", "1.00", 0)
    def test_bad_coupon(self):
        with self.assertRaises(ValueError):
            Cart().apply_coupon(150)

if __name__ == "__main__":
    unittest.main()
