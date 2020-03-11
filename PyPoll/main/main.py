#Berkeley Data Analysis Bootcamp Python homework, PyPoll
import os
import collections
import csv

csvpath = os.path.join('..', 'Resources', 'election_data.csv')

candidate = []
with open(csvpath) as csvfile:
	csvreader = csv.reader(csvfile, delimiter= ',')
	csv_header = next(csvreader)
	for row in csvreader:
		candidate.append(row[2])
c = collections.Counter(candidate)
#The data type of c is a counter

print(len(candidate))
print(c)
total_votes = len(candidate)
for candidate_name, votes in c.items():
	print('{0}: {1:.3f}% ({2})'.format(candidate_name, votes/total_votes*100, votes))
print('winner is: {}'.format(c.most_common(1)[0][0]))