from solutions.CHK import checkout_solution


class TestCHK():
    def test_checkout(self):
        assert checkout_solution.checkout("AAACDBBBEEFFFSTX") == 355


"""
("FFFF") == 30
("AAACDBBBEEFFF") == 310
"""

