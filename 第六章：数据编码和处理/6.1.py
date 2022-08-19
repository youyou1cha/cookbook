#!/usr/bin/env python
# -*- coding: utf-8 -*-
import csv
with open('stocks.csv') as f:
    # fcsv = csv.reader(f)
    # header = next(fcsv)
    # for row in fcsv:
    #     print(row)
    fcsv = csv.DictReader(f)
    # for row in fcsv:
    #     print(row.get('Time'))

headers = ['Symbol', 'Price', 'Date', 'Time', 'Change', 'Volume']
rows1 = [('AA', 39.48, '6/11/2007', '9:36am', -0.18, 181800),
         ('AIG', 71.38, '6/11/2007', '9:36am', -0.15, 195500),
         ('AXP', 62.58, '6/11/2007', '9:36am', -0.46, 935000),
       ]

rows = [{'Symbol':'AA', 'Price':39.48, 'Date':'6/11/2007',
        'Time':'9:36am', 'Change':-0.18, 'Volume':181800},
        {'Symbol':'AIG', 'Price': 71.38, 'Date':'6/11/2007',
        'Time':'9:36am', 'Change':-0.15, 'Volume': 195500},
        {'Symbol':'AXP', 'Price': 62.58, 'Date':'6/11/2007',
        'Time':'9:36am', 'Change':-0.46, 'Volume': 935000},
        ]

with open('ss.csv','w') as f:
    fcsv = csv.writer(f)
    fcsv.writerow(headers)
    fcsv.writerows(rows1)

with open('ss1.csv','w') as f:
    fcsv = csv.DictWriter(f,headers)
    fcsv.writeheader()
    fcsv.writerows(rows)