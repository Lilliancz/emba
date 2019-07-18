# many thanks to https://gist.github.com/simofacc/f47774dff4817e775461
# the csv should only contain 2 columns, no headers: just the old name and new name in 2 columns

import os
import csv

with open('emba26_r.csv', 'r') as csvfile:
    csvreader = csv.reader(csvfile, delimiter=',', quotechar='"')
    for row in csvreader:
        name = row[0] + '.jpg'
        new = row[1] + '.jpg'
        if os.path.exists(name):
            os.rename(name, new)
            print(new + " is done!!!")
        else:
            print(name + " " + new + " does not exist")