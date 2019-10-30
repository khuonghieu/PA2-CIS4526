'''
In PA 2, you might finish the assignment with only built-in types of Python 3.
However, one may choose to use higher level libraries such as numpy and scipy.
Add your code below the TO-DO statement and include necessary import statements.
'''

import sys
import csv

def main():
    
    '''
    Get the first command line argument of the program.
    For example, sys.argv[1] could be a string such as 'breast_cancer.csv' or 'titanic_train.csv'
    '''
    # szDatasetPath = sys.argv[1]
	# Comment out the following line and uncomment the above line in your final submission
    szDatasetPath = 'breast_cancer.csv'

    '''
    Read the data from the csv file
    listColNames[j] stores the jth column name
    listData[i][:-1] are the features of the ith example
    listData[i][-1] is the target value of the ith example
    '''
    listColNames = [] # The list of column names
    listData = [] # The list of feature vectors of all the examples
    nRow = 0
    with open(szDatasetPath) as csvFile:
        csvReader = csv.reader(csvFile, delimiter=',')
        for row in csvReader:
            if 0 == nRow:
                listColNames = row
            else:
                listData.append(row)
            nRow += 1

    '''
    Scan the data and store the unique values of each column.
    listColUniqueVals[j] stores a list of unique values of the jth column
    '''
    listColUniqueVals = [[] for i in range(len(listColNames))]
    for example in listData:
        for i in range(len(example)):
            if example[i] not in listColUniqueVals[i]:
                listColUniqueVals[i].append(example[i])

    # For each feature, compute the training error of a one-level decision tree
    # TO-DO: add your code here

    # Construct a full decision tree on the dataset and compute the training error
    # TO-DO: add your code here

    return None

if __name__ == '__main__':

    main()
