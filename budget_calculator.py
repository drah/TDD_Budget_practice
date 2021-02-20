import datetime
from datetime import timedelta
from calendar import monthrange

from budget_repo import get_all


class BudgetCalculator(object):
    def __init__(self):
        data_source = get_all()
        self.data_source = {item['yearmonth']: item['amount'] for item in data_source}

    def query(self, start: datetime.date, end: datetime.date) -> float:
        # date.strftime(%Y%m) -> yyyymm
        amount = 0
        delta_days = (end - start).days + 1
        for d in range(delta_days):
            cur_day = start + timedelta(days=d)
            amount += self.get_day_amount_of_month(cur_day)
        return amount

    def get_days_of_month(self, _date):
        return monthrange(_date.year, _date.month)[1]

    def get_day_amount_of_month(self, _date):
        return self.data_source.get(_date.strftime("%Y%m"), 0) / self.get_days_of_month(_date)
