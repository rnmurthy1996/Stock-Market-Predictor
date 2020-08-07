import csv
import matplotlib.pyplot as plt

def addArr(c, s, r, index):
    if(int(float(r[0])) == index):
        c[index] = c[index] + 1
        s[index] = s[index] + float(r[1])

counts = [0] * 10
sums = [0] * 10
with open('outputFixed.txt') as csvfile:
    readCSV = csv.reader(csvfile, delimiter=',')
    for row in readCSV:
        addArr(counts, sums, row, 0)
        addArr(counts, sums, row, 1)
        addArr(counts, sums, row, 2)
        addArr(counts, sums, row, 3)
        addArr(counts, sums, row, 4)
        addArr(counts, sums, row, 5)
        addArr(counts, sums, row, 6)
        addArr(counts, sums, row, 7)
        addArr(counts, sums, row, 8)
        addArr(counts, sums, row, 9)

avg = [0] * 10

for i in range (0,10):
    avg[i] = sums[i]/float(counts[i])

for i in range (0,10):
    print(counts[i])
    plt.plot(i, avg[i], 'ro')

plt.show()
