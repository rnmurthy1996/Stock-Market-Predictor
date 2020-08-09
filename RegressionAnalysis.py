import pandas as pd
import numpy as np
import csv
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn import metrics

dataset = pd.read_csv('outputUpdated.txt')

X = dataset[['Pietroski F-Score']]
y = dataset['Quarterly Return']

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=0)
regressor = LinearRegression()
regressor.fit(X_train, y_train)

coeff_df = pd.DataFrame(regressor.coef_, X.columns, columns=['Coefficient'])
print(coeff_df)

y_pred = regressor.predict(X_test)
df = pd.DataFrame({'Actual': y_test, 'Predicted': y_pred})
df1 = df.head(25)

print('Mean Absolute Error:', metrics.mean_absolute_error(y_test, y_pred))
print('Mean Squared Error:', metrics.mean_squared_error(y_test, y_pred))
print('Root Mean Squared Error:', np.sqrt(metrics.mean_squared_error(y_test, y_pred)))


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
    averages[i] = sum[i] / float(count[i])
    plt.plot(i, averages[i], 'ro')

plt.xlabel('Pietroski F-Score')
plt.ylabel('Future Quarterly Return')
plt.show()
