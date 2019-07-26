"""
SBHealth Class :: Quantify
Quantifying the health of a small business
By Frankie Sanchez :: 900942699
"""

from Business import Business
import sqlite3


class SBHealth(Business):
    def __init__(self):
        super().__init__()
        self.b_data = []
        self.b_metrics = []
        self.percentage_score = 0.0
        self.final = 0.0
        self.col_counter = 1

    # Accept/store business information from user input
    def add_business(self):
        print('Welcome to Quantify...')
        while True:
            try:
                name = input('Business name: ')
                num_of_months = int(input('Number of months to evaluate: '))
                total_revenue = float(input('Total revenue: $'))
                cogs = float(input('Cost of goods sold: $'))
                op_expenses = float(input('Operating expenses (include payroll & taxes): $'))
                start_cash_balance = float(input('Starting cash balance: $'))
                end_cash_balance = float(input('Ending cash balance: $'))
                current_assets = float(input('Value of current assets: $'))
                current_liabilities = float(input('Value of short-term liabilities: $'))
                long_term_liabilities = float(input('Value of long-term liabilities: $'))
                total_inventory = float(input('Value of total inventory: $'))
                dead_inventory = float(input('Value of dead inventory (i.e. inventory > 60 days since last sale): $'))
            except ValueError:
                print('ValueError: Please try again')
            else:
                business = Business(name=name, total_revenue=total_revenue, cogs=cogs, op_expenses=op_expenses,
                                    start_cash_balance=start_cash_balance, end_cash_balance=end_cash_balance,
                                    num_of_months=num_of_months, current_assets=current_assets,
                                    current_liabilities=current_liabilities,
                                    long_term_liabilities=long_term_liabilities,
                                    total_inventory=total_inventory, dead_inventory=dead_inventory)

                # Adding business data to iterable list
                self.b_data.append(('business name: ', business.name))
                self.b_data.append(('date: ', self.date.strftime('%Y%m%d')))
                self.b_data.append(('gross profit: ', float('{:.2f}'.format(business.gross_profit()))))
                self.b_data.append(('gross profit margin: ', float('{:.2f}'.format(business.gross_profit_margin()))))
                self.b_data.append(('net profit/loss: ', float('{:.2f}'.format(business.net_profit_loss()))))
                self.b_data.append(('net profit margin: ', float('{:.2f}'.format(business.net_profit_margin()))))
                self.b_data.append(('liquidity: ', float('{:.2f}'.format(business.liquidity()))))
                self.b_data.append(('total debt: ', float('{:.2f}'.format(business.total_debt()))))
                self.b_data.append(('debt service coverage: ', float('{:.2f}'.format(business.net_profit_loss() /
                                                                                     business.current_liabilities))))
                self.b_data.append(('debt-to-asset ratio: ', float('{:.2f}'.format(business.debt_asset_ratio()))))
                self.b_data.append(('dead inventory ratio: ', float('{:.2f}'.format(business.inventory()))))
                self.b_data.append(('cash burn rate: ', float('{:.2f}'.format(business.burn_rate()))))

                return self.b_data

    # Display business results
    def print_results(self):
        print()
        print('=============== Company Results ===============')
        for data, value in self.b_data:
            print(data, value)
        print('score: {}/5.00'.format(round(sum(self.b_metrics), 2)))
        print('===============================================')
        print()

    # Create .txt report
    def create_report(self):
        date = self.date.strftime('%Y%m%d')
        with open(str(self.b_data[0][1]) + '_' + date + '.txt', 'w') as file:
            file.write('=============== Company Results ===============\n')
            for data in self.b_data:
                file.write(' '.join(str(s) for s in data) + '\n')
            file.write('score: {}/5.00'.format(round(sum(self.b_metrics), 2)))

    # Create DB for historical information
    def create_db(self):
        con = sqlite3.connect(self.b_data[0][1] + '.db')
        cur = con.cursor()
        cur.execute('CREATE TABLE ' + self.b_data[0][1] + '_financials (category str, col' + str(self.col_counter) +
                    ' decimal(10,2))')

        for item in self.b_data[2:]:
            cur.execute('INSERT INTO ' + self.b_data[0][1] + '_financials VALUES (?,?)', (item[0], item[1]))

        cur.execute('INSERT INTO ' + self.b_data[0][1] + '_financials VALUES (?,?)', ('score: ', self.final))

        con.commit()
        con.close()
        self.col_counter += 1

    # Add data to existing database
    def add_new_data_db(self):
        self.add_business()
        self._health_compilation()
        try:
            con = sqlite3.connect(self.b_data[0][1] + '.db')
            cur = con.cursor()

            cur.execute('ALTER TABLE ' + self.b_data[0][1] + '_financials\n'
                        + 'ADD col' + str(self.col_counter) + ' decimal(10,2);')

            cur.execute('UPDATE ' + self.b_data[0][1] + '_financials SET col' + str(self.col_counter) + ' = ' +
                        str(self.b_data[2][1]) + ' WHERE category = \"gross profit: \"')

            cur.execute('UPDATE ' + self.b_data[0][1] + '_financials SET col' + str(self.col_counter) + ' = ' +
                        str(self.b_data[3][1]) + ' WHERE category = \"gross profit margin: \"')

            cur.execute('UPDATE ' + self.b_data[0][1] + '_financials SET col' + str(self.col_counter) + ' = ' +
                        str(self.b_data[4][1]) + ' WHERE category = \"net profit/loss: \"')

            cur.execute('UPDATE ' + self.b_data[0][1] + '_financials SET col' + str(self.col_counter) + ' = ' +
                        str(self.b_data[5][1]) + ' WHERE category = \"net profit margin: \"')

            cur.execute('UPDATE ' + self.b_data[0][1] + '_financials SET col' + str(self.col_counter) + ' = ' +
                        str(self.b_data[6][1]) + ' WHERE category = \"liquidity: \"')

            cur.execute('UPDATE ' + self.b_data[0][1] + '_financials SET col' + str(self.col_counter) + ' = ' +
                        str(self.b_data[7][1]) + ' WHERE category = \"total debt: \"')

            cur.execute('UPDATE ' + self.b_data[0][1] + '_financials SET col' + str(self.col_counter) + ' = ' +
                        str(self.b_data[8][1]) + ' WHERE category = \"debt service coverage: \"')

            cur.execute('UPDATE ' + self.b_data[0][1] + '_financials SET col' + str(self.col_counter) + ' = ' +
                        str(self.b_data[9][1]) + ' WHERE category = \"debt-to-asset ratio: \"')

            cur.execute('UPDATE ' + self.b_data[0][1] + '_financials SET col' + str(self.col_counter) + ' = ' +
                        str(self.b_data[10][1]) + ' WHERE category = \"dead inventory ratio: \"')

            cur.execute('UPDATE ' + self.b_data[0][1] + '_financials SET col' + str(self.col_counter) + ' = ' +
                        str(self.b_data[11][1]) + ' WHERE category = \"cash burn rate: \"')

            cur.execute('UPDATE ' + self.b_data[0][1] + '_financials SET col' + str(self.col_counter) + ' = ' +
                        str(self.final) + ' WHERE category = \"score: \"')

            con.commit()
            con.close()
            self.col_counter += 1
        except Exception as ex:
            self.col_counter += 1
            self.update_db()
            return ex
        else:
            self.col_counter += 1

    # Update database when exception is raised
    def update_db(self):
        self._health_compilation()
        try:
            con = sqlite3.connect(self.b_data[0][1] + '.db')
            cur = con.cursor()

            cur.execute('ALTER TABLE ' + self.b_data[0][1] + '_financials\n'
                        + 'ADD col' + str(self.col_counter) + ' decimal(10,2);')

            cur.execute('UPDATE ' + self.b_data[0][1] + '_financials SET col' + str(self.col_counter) + ' = ' +
                        str(self.b_data[2][1]) + ' WHERE category = \"gross profit: \"')

            cur.execute('UPDATE ' + self.b_data[0][1] + '_financials SET col' + str(self.col_counter) + ' = ' +
                        str(self.b_data[3][1]) + ' WHERE category = \"gross profit margin: \"')

            cur.execute('UPDATE ' + self.b_data[0][1] + '_financials SET col' + str(self.col_counter) + ' = ' +
                        str(self.b_data[4][1]) + ' WHERE category = \"net profit/loss: \"')

            cur.execute('UPDATE ' + self.b_data[0][1] + '_financials SET col' + str(self.col_counter) + ' = ' +
                        str(self.b_data[5][1]) + ' WHERE category = \"net profit margin: \"')

            cur.execute('UPDATE ' + self.b_data[0][1] + '_financials SET col' + str(self.col_counter) + ' = ' +
                        str(self.b_data[6][1]) + ' WHERE category = \"liquidity: \"')

            cur.execute('UPDATE ' + self.b_data[0][1] + '_financials SET col' + str(self.col_counter) + ' = ' +
                        str(self.b_data[7][1]) + ' WHERE category = \"total debt: \"')

            cur.execute('UPDATE ' + self.b_data[0][1] + '_financials SET col' + str(self.col_counter) + ' = ' +
                        str(self.b_data[8][1]) + ' WHERE category = \"debt service coverage: \"')

            cur.execute('UPDATE ' + self.b_data[0][1] + '_financials SET col' + str(self.col_counter) + ' = ' +
                        str(self.b_data[9][1]) + ' WHERE category = \"debt-to-asset ratio: \"')

            cur.execute('UPDATE ' + self.b_data[0][1] + '_financials SET col' + str(self.col_counter) + ' = ' +
                        str(self.b_data[10][1]) + ' WHERE category = \"dead inventory ratio: \"')

            cur.execute('UPDATE ' + self.b_data[0][1] + '_financials SET col' + str(self.col_counter) + ' = ' +
                        str(self.b_data[11][1]) + ' WHERE category = \"cash burn rate: \"')

            cur.execute('UPDATE ' + self.b_data[0][1] + '_financials SET col' + str(self.col_counter) + ' = ' +
                        str(self.final) + ' WHERE category = \"score: \"')

            con.commit()
            con.close()
            self.col_counter += 1
        except Exception as ex:
            self.col_counter += 1
            self.update_db()
            return ex
        else:
            self.col_counter += 1

    # ==================== Metric System ==================== #

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
        elif self.b_data[9][1] > 0.60:
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
        elif self.b_data[10][1] >= 0.25:
            return 0.475

    # Health computation (in aggregate)
    def _health_compilation(self):
        if len(self.b_metrics) < 5:
            self.b_metrics.append(self._h_net_profit_margin())
            self.b_metrics.append(self._h_debt_service_coverage())
            self.b_metrics.append(self._h_debt_to_asset_ratio())
            self.b_metrics.append(self._h_liquidity())
            self.b_metrics.append(self._h_dead_inventory())

            self.percentage_score = round(sum(self.b_metrics) / 5.00, 2)
            self.final = self.percentage_score * 100.0
        return self.final

    # Final grade
    def _grade_review(self):
        if self.percentage_score >= 0.98:
            print('Grade: A+')
            print('Score: {}/5.00'.format(round(sum(self.b_metrics), 2)))
        elif 0.98 > self.percentage_score >= 0.92:
            print('Grade: A')
            print('Score: {}/5.00'.format(round(sum(self.b_metrics), 2)))
        elif 0.92 > self.percentage_score >= 0.90:
            print('Grade: A-')
            print('Score: {}/5.00'.format(round(sum(self.b_metrics), 2)))
        elif 0.90 > self.percentage_score >= 0.88:
            print('Grade: B+')
            print('Score: {}/5.00'.format(round(sum(self.b_metrics), 2)))
        elif 0.88 > self.percentage_score >= 0.82:
            print('Grade: B')
            print('Score: {}/5.00'.format(round(sum(self.b_metrics), 2)))
        elif 0.82 > self.percentage_score >= 0.80:
            print('Grade: B-')
            print('Score: {}/5.00'.format(round(sum(self.b_metrics), 2)))
        elif 0.80 > self.percentage_score >= 0.78:
            print('Grade: C+')
            print('Score: {}/5.00'.format(round(sum(self.b_metrics), 2)))
        elif 0.78 > self.percentage_score >= 0.72:
            print('Grade: C')
            print('Score: {}/5.00'.format(round(sum(self.b_metrics), 2)))
        elif 0.72 > self.percentage_score >= 0.70:
            print('Grade: C-')
            print('Score: {}/5.00'.format(round(sum(self.b_metrics), 2)))
        elif 0.70 > self.percentage_score >= 0.68:
            print('Grade: D+')
            print('Score: {}/5.00'.format(round(sum(self.b_metrics), 2)))
        elif 0.68 > self.percentage_score >= 0.62:
            print('Grade: D')
            print('Score: {}/5.00'.format(round(sum(self.b_metrics), 2)))
        elif 0.62 > self.percentage_score >= 0.60:
            print('Grade: D-')
            print('Score: {}/5.00'.format(round(sum(self.b_metrics), 2)))
        elif 0.60 > self.percentage_score:
            print('Grade: F')
            print('Score: {}/5.00'.format(round(sum(self.b_metrics), 2)))

    # Call from main to show final analysis
    def final_results(self):
        print()
        self._health_compilation()
        self._grade_review()



