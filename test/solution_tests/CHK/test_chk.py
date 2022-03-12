from solutions.CHK import checkout_solution


class TestCHK():
    def test_checkout(self):
        assert checkout_solution.checkout("AAACDBBBEE") == 290

#3A + 2B + B + C + D + 2E === 130 + 45 + 0 + 20 + 15 + 80 ==

