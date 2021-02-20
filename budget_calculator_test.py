from datetime import date

from budget_calculator import BudgetCalculator
from budget_repo import get_all

import unittest
from unittest.mock import patch


class BudgetCalculatorTest(unittest.TestCase):
    def setUp(self):
        get_all_patcher = patch("budget_calculator.get_all")
        self.fake_get_all = get_all_patcher.start()

    def tearDown(self) -> None:
        patch.stopall()

    def test_single_month_full(self):
        self.fake_get_all.return_value = [
            {"yearmonth": "202101",
             "amount": 31}]
        calculator = BudgetCalculator()
        budget = calculator.query(date(2021, 1, 1), date(2021, 1, 31))
        self.assertEqual(31, budget)



if __name__ == '__main__':
    unittest.main()
