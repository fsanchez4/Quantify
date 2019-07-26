import numpy as np

# ========== 5 years (60 months) of data for visualization ========== #
revenue = [float('{:.2f}'.format(x)) for x in np.random.uniform(low=20000.00, high=30000.00, size=60)]
op_expenses = [float('{:.2f}'.format(x)) for x in np.random.uniform(low=15000.00, high=20000.00, size=60)]
cogs = [float('{:.2f}'.format(x)) for x in np.random.uniform(low=5000.00, high=15000.00, size=60)]

# Starting cash value = $5000.00
cash_on_hand = []
cash_setup_arr = [5000.00] * 60

for a, b, c, d in zip(cash_setup_arr, revenue, op_expenses, cogs):
    val = float('{:.2f}'.format(a + (b - c - d)))
    cash_on_hand.append(val)
    print('revenue', a)
    print('op_exp', b)
    print('cogs', c)
    print('cash', val)
    print()

print('Revenue: ', revenue)
print('Expenses: ', op_expenses)
print('COGS: ', cogs)
print('Cash-on-hand: ', cash_on_hand)

# print(len(revenue))
# print(len(op_expenses))
# print(len(cogs))
# print(len(cash_on_hand))
