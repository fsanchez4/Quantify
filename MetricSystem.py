"""
MetricSystem Class :: Quantify
Quantifying the health of a small business
By Frankie Sanchez :: 900942699
"""

from Business import Business


class MetricSystem(Business):

    def __init__(self):
        super().__init__()
        self.b_metrics = []
        self.score = 0.0

    # Metric 1: Net profit margin ratio (organizational)
    def _h_net_profit_margin(self):
        if self.b_data[3][1] >= 0.2:
            return 1.0
        elif 0.18 <= self.b_data[5][1] < 0.20:
            return 0.95
        elif 0.16 <= self.b_data[5][1] < 0.18:
            return 0.90
        elif 0.14 <= self.b_data[5][1] < 0.16:
            return 0.85
        elif 0.12 <= self.b_data[5][1] < 0.14:
            return 0.80
        elif 0.10 <= self.b_data[5][1] < 0.12:
            return 0.75
        elif 0.08 <= self.b_data[5][1] < 0.10:
            return 0.70
        elif 0.06 <= self.b_data[5][1] < 0.08:
            return 0.65
        elif 0.04 <= self.b_data[5][1] < 0.06:
            return 0.60
        elif 0.02 <= self.b_data[5][1] < 0.04:
            return 0.55
        elif 0.001 <= self.b_data[5][1] < 0.02:
            return 0.50
        elif self.b_data[5][1] < 0:
            return 0.45

    # Metric 2: Debt service coverage ratio (institutional)
    def _h_debt_service_coverage(self):
        if self.b_data[8][1] >= 1.25:
            return 1.0
        elif 1.20 <= self.b_data[8][1] < 1.25:
            return 0.95
        elif 1.18 <= self.b_data[8][1] < 1.20:
            return 0.90
        elif 1.16 <= self.b_data[8][1] < 1.18:
            return 0.85
        elif 1.14 <= self.b_data[8][1] < 1.16:
            return 0.80
        elif 1.12 <= self.b_data[8][1] < 1.14:
            return 0.75
        elif 1.10 <= self.b_data[8][1] < 1.12:
            return 0.70
        elif 1.075 <= self.b_data[8][1] < 1.10:
            return 0.65
        elif 1.050 <= self.b_data[8][1] < 1.075:
            return 0.60
        elif 1.025 <= self.b_data[8][1] < 1.050:
            return 0.55
        elif 1.00 <= self.b_data[8][1] < 1.025:
            return 0.50
        elif self.b_data[8][1] < 1:
            return 0.45

    # Metric 3: Debt-to-asset ratio (the higher the ratio, the greater the risk)
    def _h_debt_to_asset_ratio(self):
        if self.b_data[9][1] <= 0.15:
            return 1.0
        elif 0.20 >= self.b_data[9][1] > 0.15:
            return 0.95
        elif 0.25 >= self.b_data[9][1] > 0.20:
            return 0.90
        elif 0.30 >= self.b_data[9][1] > 0.25:
            return 0.85
        elif 0.35 >= self.b_data[9][1] > 0.30:
            return 0.80
        elif 0.40 >= self.b_data[9][1] > 0.35:
            return 0.75
        elif 0.45 >= self.b_data[9][1] > 0.40:
            return 0.70
        elif 0.50 >= self.b_data[9][1] > 0.45:
            return 0.65
        elif 0.55 >= self.b_data[9][1] > 0.50:
            return 0.60
        elif 0.60 >= self.b_data[9][1] > 0.55:
            return 0.55
        elif self.b_data[8][1] > 0.60:
            return 0.50

    # Metric 4: Liquidity health (current ratio)
    def _h_liquidity(self):
        if self.b_data[6][1] > 3.0:
            return 0.85
        elif 2.50 <= self.b_data[6][1] < 3.0:
            return 1.0
        elif 2.00 <= self.b_data[6][1] < 2.50:
            return 0.95
        elif 1.50 <= self.b_data[6][1] < 2.00:
            return 0.90
        elif 1.25 <= self.b_data[6][1] < 1.50:
            return 0.85
        elif 1.20 <= self.b_data[6][1] < 1.25:
            return 0.75
        elif 1.15 <= self.b_data[6][1] < 1.20:
            return 0.70
        elif 1.10 <= self.b_data[6][1] < 1.15:
            return 0.65
        elif 1.05 <= self.b_data[6][1] < 1.10:
            return 0.60
        elif 1.00 <= self.b_data[6][1] < 1.05:
            return 0.55
        elif self.b_data[6][1] < 1:
            return 0.50

    # Metric 5: Inventory health (inventory movement)
    def _h_dead_inventory(self):
        if self.b_data[10][1] < 0.05:
            return 1.0
        elif 0.05 <= self.b_data[10][1] < 0.06:
            return 0.975
        elif 0.06 <= self.b_data[10][1] < 0.07:
            return 0.95
        elif 0.07 <= self.b_data[10][1] < 0.08:
            return 0.925
        elif 0.08 <= self.b_data[10][1] < 0.09:
            return 0.90
        elif 0.09 <= self.b_data[10][1] < 0.10:
            return 0.875
        elif 0.10 <= self.b_data[10][1] < 0.11:
            return 0.85
        elif 0.11 <= self.b_data[10][1] < 0.12:
            return 0.825
        elif 0.12 <= self.b_data[10][1] < 0.13:
            return 0.80
        elif 0.13 <= self.b_data[10][1] < 0.14:
            return 0.775
        elif 0.14 <= self.b_data[10][1] < 0.15:
            return 0.75
        elif 0.15 <= self.b_data[10][1] < 0.16:
            return 0.725
        elif 0.16 <= self.b_data[10][1] < 0.17:
            return 0.70
        elif 0.17 <= self.b_data[10][1] < 0.18:
            return 0.675
        elif 0.18 <= self.b_data[10][1] < 0.19:
            return 0.65
        elif 0.19 <= self.b_data[10][1] < 0.20:
            return 0.625
        elif 0.20 <= self.b_data[10][1] < 0.21:
            return 0.60
        elif 0.21 <= self.b_data[10][1] < 0.22:
            return 0.575
        elif 0.22 <= self.b_data[10][1] < 0.23:
            return 0.55
        elif 0.23 <= self.b_data[10][1] < 0.24:
            return 0.525
        elif 0.24 <= self.b_data[10][1] < 0.25:
            return 0.50
        elif self.b_data[10][1] < 0.25:
            return 0.475

    # Health computation (in aggregate)
    def health_compilation(self):
        self.b_metrics.append(self._h_net_profit_margin())
        self.b_metrics.append(self._h_debt_service_coverage())
        self.b_metrics.append(self._h_debt_to_asset_ratio())
        self.b_metrics.append(self._h_liquidity())
        self.b_metrics.append(self._h_dead_inventory())

        self.score = sum(self.b_metrics) / 5.00
        return self.score

    # Final grade
    def grade_review(self):
        if self.score >= 0.98:
            print('Grade: A+')
            print('Score: {}/5.00'.format(self.score))
        elif 0.98 > self.score >= 0.92:
            print('Grade: A')
            print('Score: {}/5.00'.format(self.score))
        elif 0.92 > self.score >= 0.90:
            print('Grade: A-')
            print('Score: {}/5.00'.format(self.score))
        elif 0.90 > self.score >= 0.88:
            print('Grade: B+')
            print('Score: {}/5.00'.format(self.score))
        elif 0.88 > self.score >= 0.82:
            print('Grade: B')
            print('Score: {}/5.00'.format(self.score))
        elif 0.82 > self.score >= 0.80:
            print('Grade: B-')
            print('Score: {}/5.00'.format(self.score))
        elif 0.80 > self.score >= 0.78:
            print('Grade: C+')
            print('Score: {}/5.00'.format(self.score))
        elif 0.78 > self.score >= 0.72:
            print('Grade: C')
            print('Score: {}/5.00'.format(self.score))
        elif 0.72 > self.score >= 0.70:
            print('Grade: C-')
            print('Score: {}/5.00'.format(self.score))
        elif 0.70 > self.score >= 0.68:
            print('Grade: D+')
            print('Score: {}/5.00'.format(self.score))
        elif 0.68 > self.score >= 0.62:
            print('Grade: D')
            print('Score: {}/5.00'.format(self.score))
        elif 0.62 > self.score >= 0.60:
            print('Grade: D-')
            print('Score: {}/5.00'.format(self.score))
        elif 0.60 > self.score:
            print('Grade: F')
            print('Score: {}/5.00'.format(self.score))
