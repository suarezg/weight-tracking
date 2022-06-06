from datetime import datetime
import csv

DATE_FORMAT = "%Y-%m-%d"
FILE = "weight-data.csv"
file = open(FILE)

data = csv.reader(file, delimiter=',')

days = []
weight_data = []

first_date = None

for count, line in enumerate(data):
    dt_str, w_str = line
    if count == 0:
        first_date = datetime.strptime(dt_str, DATE_FORMAT)
        days.append(1)
    else:
        assert(first_date != None)
        date = datetime.strptime(dt_str, DATE_FORMAT)
        delta = date - first_date
        days.append(delta.days + 1)

    weight_data.append( float(w_str) )

file.close()

out = open('pre-processed.csv', "w+")
for day, weight in zip(days, weight_data):
    out.write(f"{day},{weight}\n")

out.close()





