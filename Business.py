"""
Business Class :: Quantify
Quantifying the health of a small business
By Frankie Sanchez :: 900942699
"""
import datetime


class Business:

    def __init__(self, name='', total_revenue=0.0, cogs=0.0, op_expenses=0.0, start_cash_balance=0.0,
                 end_cash_balance=0.0, num_of_months=0, current_assets=0.0, current_liabilities=0.0,
                 long_term_liabilities=0.0, total_inventory=0.0, dead_inventory=0.0,):

        # ==================== General business information ==================== #
        # Date / Previous Month
        today = datetime.date.today()
        self.date = today
        # first = today.replace(day=1)
        # previous_month = first - datetime.timedelta(days=1)
        # self.date = previous_month.strftime('%m-%Y')

        # Business info
        self.name = name
        self.location = ''
        self.industry = ''

        # Revenue (i.e. total income before expenses)
        self.total_revenue = total_revenue

        # Cost of goods sold (e.g. inventory, merchant fees, shipping)
        self.cogs = cogs

        # Operating expenses (e.g. rent, payroll, taxes, utilities, etc.)
        self.op_expenses = op_expenses

        # Cash-on-hand and burn rate variables
        self.start_cash_balance = start_cash_balance
        self.end_cash_balance = end_cash_balance
        self.num_of_months = num_of_months

        # Liquid assets (i.e. assets that can be converted to cash within 1 year)
        self.current_assets = current_assets

        # Short-term liabilities and interest due (< 12 months)
        self.current_liabilities = current_liabilities

        # Long-term debt obligations
        self.long_term_liabilities = long_term_liabilities

        # KTLO
        self.break_even = 0.0

        # Current & dead inventory
        self.total_inventory = total_inventory
        self.dead_inventory = dead_inventory

    # ==================== Computational methods ==================== #

    # Gross profit
    def gross_profit(self):
        ni = self.total_revenue - self.cogs
        return ni

    # Gross profit margin
    def gross_profit_margin(self):
        gpm = (self.total_revenue - self.cogs) / self.total_revenue
        return gpm

    # Profitability factor
    def net_profit_loss(self):
        npl = self.total_revenue - self.cogs - self.op_expenses
        return npl

    # Net profit margin
    def net_profit_margin(self):
        npm = (self.total_revenue - self.cogs - self.op_expenses) / self.total_revenue
        return npm

    # Current ratio (< 1.0 signals danger as current liabilities exceeds current assets)
    def liquidity(self):
        liquid = (self.end_cash_balance + self.current_assets) / self.current_liabilities
        return liquid

    # Debt information
    def total_debt(self):
        td = self.current_liabilities + self.long_term_liabilities
        return td

    # Debt-to-asset ratio (0.4 and lower signal healthy debt)
    def debt_asset_ratio(self):
        dar = (self.current_liabilities + self.long_term_liabilities) / (self.current_assets + self.end_cash_balance)
        return dar

    # Inventory health; < 15% is healthy
    def inventory(self):
        inventory_health = self.dead_inventory / self.total_inventory
        return inventory_health

    # Burn rate (cash)
    def burn_rate(self):
        cash_burn_rate = abs(self.start_cash_balance - self.end_cash_balance) / self.num_of_months
        return cash_burn_rate

