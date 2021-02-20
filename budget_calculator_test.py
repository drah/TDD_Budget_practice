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

    def test_two_months_full(self):
        self.fake_get_all.return_value = [
            {"yearmonth": "202101",
             "amount": 31},
            {"yearmonth": "202102",
             "amount": 280},
        ]
        calculator = BudgetCalculator()
        budget = calculator.query(date(2021, 1, 1), date(2021, 2, 28))
        self.assertEqual(311, budget)

    def test_one_day(self):
        self.fake_get_all.return_value = [
            {"yearmonth": "202101",
             "amount": 31},
            {"yearmonth": "202102",
             "amount": 280},
        ]
        calculator = BudgetCalculator()
        budget = calculator.query(date(2021, 1, 1), date(2021, 1, 1))
        self.assertEqual(1, budget)

    def test_multiple_days(self):
        self.fake_get_all.return_value = [
            {"yearmonth": "202101",
             "amount": 31},
            {"yearmonth": "202102",
             "amount": 280},
        ]
        calculator = BudgetCalculator()
        budget = calculator.query(date(2021, 1, 1), date(2021, 1, 2))
        self.assertEqual(2, budget)

    def test_cross_months(self):
        self.fake_get_all.return_value = [
            {"yearmonth": "202101",
             "amount": 31},
            {"yearmonth": "202102",
             "amount": 280},
        ]
        calculator = BudgetCalculator()
        budget = calculator.query(date(2021, 1, 30), date(2021, 2, 1))
        self.assertEqual(12, budget)

    def test_one_day_given_null(self):
        self.fake_get_all.return_value = [

        ]
        calculator = BudgetCalculator()
        budget = calculator.query(date(2021, 1, 1), date(2021, 1, 1))
        self.assertEqual(0, budget)

    def test_cross_months_given_one_month_null(self):
        self.fake_get_all.return_value = [
            {"yearmonth": "202101",
             "amount": 31},
            {"yearmonth": "202103",
             "amount": 310},
        ]
        calculator = BudgetCalculator()
        budget = calculator.query(date(2021, 1, 31), date(2021, 3, 2))
        self.assertEqual(21, budget)

    def test_start_bigger_than_end(self):
        self.fake_get_all.return_value = [
            {"yearmonth": "202101",
             "amount": 31},
            {"yearmonth": "202103",
             "amount": 310},
        ]
        calculator = BudgetCalculator()
        budget = calculator.query(date(2021, 1, 2), date(2021, 1, 1))
        self.assertEqual(0, budget)

    def test_cross_year(self):
        self.fake_get_all.return_value = [
            {"yearmonth": "202101",
             "amount": 310},
            {"yearmonth": "202012",
             "amount": 31},
        ]
        calculator = BudgetCalculator()
        budget = calculator.query(date(2020, 12, 31), date(2021, 1, 2))
        self.assertEqual(21, budget)




if __name__ == '__main__':
    unittest.main()
