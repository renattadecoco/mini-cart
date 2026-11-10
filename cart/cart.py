from decimal import Decimal, ROUND_HALF_UP


class Cart:
    """Shopping cart. Prices are strings like '19.99'.

    Rules:
    - Items flagged buy2get1 get every 3rd unit free (per SKU).
    - A percent coupon applies to the subtotal AFTER item promotions.
    - total() returns a Decimal rounded to 2 places, ROUND_HALF_UP.
    """

    def __init__(self):
        self.items = {}
        self.coupon = Decimal("0")

    def add(self, sku, price, qty=1, buy2get1=False):
        if qty <= 0:
            raise ValueError("qty must be positive")
        if sku in self.items:
            self.items[sku]["qty"] += qty
            # A later add for the same SKU must not lose the promotion.
            self.items[sku]["buy2get1"] = (
                self.items[sku]["buy2get1"] or buy2get1
            )
        else:
            self.items[sku] = {
                "price": Decimal(str(price)),
                "qty": qty,
                "buy2get1": buy2get1,
            }

    def apply_coupon(self, percent):
        percent = Decimal(str(percent))
        if percent < 0 or percent > 100:
            raise ValueError("coupon percent must be between 0 and 100")
        self.coupon = percent

    def total(self):
        subtotal = Decimal("0")
        for item in self.items.values():
            qty = item["qty"]
            if item["buy2get1"]:
                qty -= qty // 3  # every 3rd unit free
            subtotal += item["price"] * qty
        discounted = subtotal * (
            Decimal("1") - self.coupon / Decimal("100")
        )
        return discounted.quantize(Decimal("0.01"), rounding=ROUND_HALF_UP)
