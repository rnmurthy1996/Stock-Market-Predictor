class StockReport:

    ticker = ""
    quarter = ""
    year = 0
    startDate = ""
    endDate = ""
    fscore = 0
    returns = 0

    def __init__(self, t, q, y, d, f):
        self.ticker = t
        self.quarter = q
        self.year = y
        self.startDate = d
        self.fscore = f

    def __str__(self):
        return self.ticker + " , " + self.quarter + " , " + self.year + " , " + self.startDate + " , " + self.endDate + " , " + self.fscore + " , " + str(self.returns)
