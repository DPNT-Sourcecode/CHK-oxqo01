from solutions.CHK import checkout_solution


class TestCHK():
    def test_checkout(self):
        assert checkout_solution.checkout("SSSZ") == 65


"""
("FFFF") == 30
("AAACDBBBEEFFF") == 310
 - {"method":"checkout","params":["STXSTX"],"id":"CHK_R5_140"}, expected: 90, got: 102
 - {"method":"checkout","params":["SSS"],"id":"CHK_R5_141"}, expected: 45, got: 60
 - {"method":"checkout","params":["SSSZ"],"id":"CHK_R5_142"}, expected: 65, got: 81
"""



