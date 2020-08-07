import csv
import StockReport
from itertools import islice

stockList = []
stockListFix = []

with open('us-derived-quarterly.csv') as csvfile:
    readCSV = csv.reader(csvfile, delimiter=';')
    for row in readCSV:
        if (not row[0]) or (not row[3]) or (not [4]) or (not row[6]) or (not row[26]) or (row[0] == "Ticker"):
            continue
        sr = StockReport.StockReport(row[0], row[4], row[3], row[6], row[26])
        stockList.append(sr)

i = 1
for report in stockList:
    if(report.quarter == "Q1"):
        for report2 in stockList:
            if(report2.ticker == report.ticker and report2.quarter == "Q2" and report2.year == report.year):
                report.endDate = report2.startDate
    if(report.quarter == "Q2"):
        for report2 in stockList:
            if(report2.ticker == report.ticker and report2.quarter == "Q3" and report2.year == report.year):
                report.endDate = report2.startDate
    if(report.quarter == "Q3"):
        for report2 in stockList:
            if(report2.ticker == report.ticker and report2.quarter == "Q4" and report2.year == report.year):
                report.endDate = report2.startDate
    if(report.quarter == "Q4"):
        for report2 in stockList:
            if(report2.ticker == report.ticker and report2.quarter == "Q1" and int(report2.year) == int(report.year) + 1):
                report.endDate = report2.startDate
    print(i)
    i+=1
    if(i>100000): break

for report in stockList:
    if (not report.ticker) or (not report.quarter) or (not report.year) or (not report.startDate) or (not report.endDate) or (not report.fscore):
        continue
    else:
        stockListFix.append(report)

i = 1
ticker = ""
rowNum=0
for report in stockListFix:
    startPrice = 0
    endPrice = 0
    ratio = 0
    with open('us-shareprices-daily.csv') as csvfile:
        if (ticker != report.ticker):
            ticker = report.ticker
            rowNum=0
            for row in islice(csv.reader(csvfile), 0, None):

                rowTicker = row[0].split(";")[0]
                rowDate = row[0].split(";")[2]
                rowPrice = row[0].split(";")[3]
                rowNum +=1

                if (not rowTicker) or (not rowDate) or (not rowPrice) or (rowTicker == "Ticker"):
                    continue
                elif (rowTicker == report.ticker) and (rowDate == report.startDate):
                    startPrice = rowPrice
                elif (rowTicker == report.ticker) and (rowDate == report.endDate):
                    endPrice = rowPrice
                    break
        else:
            for row in islice(csv.reader(csvfile), rowNum-365, None): #starting at rowNum was skipping some start date values so adjusted it back a year

                rowTicker = row[0].split(";")[0]
                rowDate = row[0].split(";")[2]
                rowPrice = row[0].split(";")[3]

                if (not rowTicker) or (not rowDate) or (not rowPrice) or (rowTicker == "Ticker"):
                    continue
                elif (rowTicker == report.ticker) and (rowDate == report.startDate):
                    startPrice = rowPrice
                elif (rowTicker == report.ticker) and (rowDate == report.endDate):
                    endPrice = rowPrice
                    break

    if (float(endPrice) > 0) and (float(startPrice) > 0):
        ratio = float(endPrice) / float(startPrice)
    report.returns = ratio
    print(report)
    f = open("FinalOutput.txt", "a")
    f.write(report.ticker + " , " + report.startDate + " , " + report.endDate + " , " + str(report.fscore) + " , " + str(report.returns) + "\n")
    print(i)
    i += 1
