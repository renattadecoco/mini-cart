# Tasks

Work on a new branch per task and open a pull request for each (or commit to the branch if PRs are not possible).
Do not change the tests. Do not add third-party dependencies.

1. **slugify (easy)** - `cart/text.py`: make all tests in `tests/test_text.py` pass.
2. **parse_duration (medium)** - `cart/duration.py`: implement `parse_duration` so `tests/test_duration.py` passes.
3. **Cart totals (hard)** - `cart/cart.py`: fix money handling and promotions so `tests/test_cart.py` passes.
   Keep the public API (`Cart.add`, `Cart.apply_coupon`, `Cart.total`) unchanged.

When done, reply with: what you changed per task, and the full test output.
