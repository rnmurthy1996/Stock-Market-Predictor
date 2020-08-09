import csv

"""
f = open("outputUpdated.txt", "a")
i=1
with open('output.txt') as csvfile:
    readCSV = csv.reader(csvfile, delimiter=',')
    for row in readCSV:
        print(i)
        i += 1
        if (float(row[4])==0):
            continue
        else:
            with open('us-derived-quarterly.csv') as csvfile2:
                readCSV2 = csv.reader(csvfile2, delimiter=';')
                for row2 in readCSV2:
                    if(row2[0]==row[0] and row2[6]==row[1]):
                        f.write(row[0] + ',' + row[1] + ',' + row[2] + ',' + row[3] + ',' + row2[17] + ',' + row2[18] + ',' + row2[19] + ',' + row[4] + '\n')
"""

"""
f = open("SPYcomparison.txt", "a")
i=1
with open('output.txt') as csvfile:
    readCSV = csv.reader(csvfile, delimiter=',')
    for row in readCSV:
        print(i)
        i += 1

        outputStartDate = row[1].split('-')
        outputEndDate = row[2].split('-')
        outputStartYear = int(outputStartDate[0])
        outputStartMonth = int(outputStartDate[1])
        outputStartDay = int(outputStartDate[2])
        outputEndYear = int(outputEndDate[0])
        outputEndMonth = int(outputEndDate[1])
        outputEndDay = int(outputEndDate[2])

        if (float(row[4]) != 0):
            with open('SPY.csv') as csvfile2:
                SPYstartPrice = 0
                SPYendPrice = 0
                SPYreturns = 0
                readCSV2 = csv.reader(csvfile2, delimiter=',')
                for row2 in readCSV2:

                    if(row2[0] != 'Date'):
                        SPYdate = row2[0].split('/')
                        SPYyear = int(SPYdate[2])
                        SPYmonth = int(SPYdate[0])
                        SPYday = int(SPYdate[1])

                        if((outputStartYear == SPYyear) and (outputStartMonth == SPYmonth) and (outputStartDay == SPYday)):
                            SPYstartPrice = float(row2[1])

                        if((outputEndYear == SPYyear) and (outputEndMonth == SPYmonth) and (outputEndDay == SPYday)):
                            SPYendPrice = float(row2[1])

                        SPYreturns = 0
                        if(SPYstartPrice != 0 and SPYendPrice != 0):
                            SPYreturns = SPYendPrice/SPYstartPrice

                        if(SPYreturns != 0):
                            f.write(row[0] + ',' + row[3] + ',' + row[4] + ',' + str(SPYreturns) + '\n')
                            break
"""
