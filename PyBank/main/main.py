#Berkeley Data Analysis Bootcamp Python homework, PyBank
import os
import csv

csvpath = os.path.join('..', 'Resources', 'budget_data.csv')
raw_data = []
with open(csvpath) as csvfile:
	csvreader = csv.reader(csvfile, delimiter= ',')
	csv_header = next(csvreader)
	for row in csvreader:
		raw_data.append(dict(month=row[0], revenue=int(row[1])))

know_months = set([d['month'] for d in raw_data])
#know_months = (set([d['month']) for d in raw_data])
#set() convert a list of elements to a set of unique elements
total = sum([d['revenue'] for d in raw_data])
changes = [d['revenue'] - raw_data[i-1]['revenue']
           for i, d in enumerate(raw_data) if i > 0]
max_profit = max(changes)
max_profit_month = raw_data[changes.index(max_profit)+1]['month']
max_loss = min(changes)
max_loss_month = raw_data[changes.index(max_loss)+1]['month']
print(len(know_months))
print(total)
print(sum(changes)/len(changes))
print(max_profit_month, max(changes))
print(max_loss_month, min(changes))


