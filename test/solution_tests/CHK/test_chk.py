from solutions.CHK import checkout_solution


class TestCHK():
    def test_checkout(self):
        assert checkout_solution.checkout("AAAAAAAA") == 330


"""
 - {"method":"checkout","params":["AAAAAAAA"],"id":"CHK_R2_020"}, expected: 330, got: 350
 - {"method":"checkout","params":["AAAAAAAAA"],"id":"CHK_R2_021"}, expected: 380, got: 400
 - {"method":"checkout","params":["AAAAAEEBAAABB"],"id":"CHK_R2_040"}, expected: 455, got: 475
"""
