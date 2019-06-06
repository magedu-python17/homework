#!/usr/bin/env python

import csv


csv_file_name = "csv1.csv"

with open(csv_file_name,newline="") as csvfile:
    csv_reader = csv.reader(csvfile,delimiter=" ",quotechar='|')
    for row in csv_reader:
        print(', '.join(row))

