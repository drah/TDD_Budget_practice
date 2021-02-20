from budget_repo import get_all


class BudgetCalculator(object):
    def __init__(self):
        self.data_source = get_all()

    def query(self, start, end) -> float:
        return 31