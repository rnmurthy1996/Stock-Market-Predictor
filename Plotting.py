import matplotlib.pyplot as plt
import matplotlib.pyplot as plt2
import matplotlib.pyplot as plt3
import csv

def addIndex(countArr, sumArr, index, csvFScore, csvReturns):
    if(index == csvFScore):
        countArr[index] += 1
        sumArr[index] += float(csvReturns)

count = [0]*10
sum = [0]*10

with open('outputUpdated.txt') as csvfile:
    readCSV = csv.reader(csvfile, delimiter=',')
    for row in readCSV:
        if(row[0] != 'Ticker'):
            addIndex(count, sum, 0, int(float(row[3])), row[7])
            addIndex(count, sum, 1, int(float(row[3])), row[7])
            addIndex(count, sum, 2, int(float(row[3])), row[7])
            addIndex(count, sum, 3, int(float(row[3])), row[7])
            addIndex(count, sum, 4, int(float(row[3])), row[7])
            addIndex(count, sum, 5, int(float(row[3])), row[7])
            addIndex(count, sum, 6, int(float(row[3])), row[7])
            addIndex(count, sum, 7, int(float(row[3])), row[7])
            addIndex(count, sum, 8, int(float(row[3])), row[7])
            addIndex(count, sum, 9, int(float(row[3])), row[7])

averages = [0]*10
for i in range(0,10):
    averages[i] = float(sum[i]) / float(count[i])
    plt.plot(i, averages[i], 'ro')

plt.xlabel('Piotroski F-score')
plt.ylabel('Future Quarterly Return')
plt.show()

count2 = [0]*10
sum2 = [0]*10

with open('SPYcomparison.txt') as csvfile:
    readCSV = csv.reader(csvfile, delimiter=',')
    for row in readCSV:
        addIndex(count2, sum2, 0, int(float(row[1])), float(row[2])-float(row[3]))
        addIndex(count2, sum2, 1, int(float(row[1])), float(row[2])-float(row[3]))
        addIndex(count2, sum2, 2, int(float(row[1])), float(row[2])-float(row[3]))
        addIndex(count2, sum2, 3, int(float(row[1])), float(row[2])-float(row[3]))
        addIndex(count2, sum2, 4, int(float(row[1])), float(row[2])-float(row[3]))
        addIndex(count2, sum2, 5, int(float(row[1])), float(row[2])-float(row[3]))
        addIndex(count2, sum2, 6, int(float(row[1])), float(row[2])-float(row[3]))
        addIndex(count2, sum2, 7, int(float(row[1])), float(row[2])-float(row[3]))
        addIndex(count2, sum2, 8, int(float(row[1])), float(row[2])-float(row[3]))
        addIndex(count2, sum2, 9, int(float(row[1])), float(row[2])-float(row[3]))


averages2 = [0]*10
for i in range(0,10):
    averages2[i] = float(sum2[i]) / float(count2[i])
    plt2.plot(i, averages2[i], 'ro')

plt2.xlabel('Piotroski F-score')
plt2.ylabel('SPY Outperformance')
plt2.show()

fscoreArr = [0,1,2,3,4,5,6,7,8,9]
plt3.bar(fscoreArr, count2)
plt2.xlabel('Piotroski F-score')
plt2.ylabel('Number of Quarterly Reports')
plt3.show()
