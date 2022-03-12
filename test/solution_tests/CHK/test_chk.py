from solutions.CHK import checkout_solution


class TestCHK():
    def test_checkout(self):
        assert checkout_solution.checkout("FF") == 20


"""
("AAACDBBBEEFFF") == 310
"""


