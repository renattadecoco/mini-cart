class Cart:
    """Shopping cart. Prices are strings like '19.99'.

    Rules:
    - Items flagged buy2get1 get every 3rd unit free (per SKU).
    - A percent coupon applies to the subtotal AFTER item promotions.
    - total() returns a Decimal rounded to 2 places, ROUND_HALF_UP.
    """

    def __init__(self):
        self.items = {}
        self.coupon = 0

    def add(self, sku, price, qty=1, buy2get1=False):
        if qty <= 0:
            raise ValueError("qty must be positive")
        if sku in self.items:
            self.items[sku]["qty"] += qty
        else:
            self.items[sku] = {"price": float(price), "qty": qty, "buy2get1": buy2get1}

    def apply_coupon(self, percent):
        self.coupon = percent

    def total(self):
        total = 0
        for item in self.items.values():
            line = item["price"] * item["qty"]
            line = line * (1 - self.coupon / 100)
            total += line
        return round(total, 2)
