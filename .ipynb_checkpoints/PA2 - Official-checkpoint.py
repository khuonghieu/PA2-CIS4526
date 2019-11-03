#!/usr/bin/env python
# coding: utf-8
# %%
import sys
import csv
from sklearn import tree
from sklearn import preprocessing
import matplotlib
import graphviz
import numpy as np

def mostOccur(featureColumn,element, labelCol):
    oneOccur =0
    zeroOccur =0
    for i in range(len(featureColumn)):
        if(featureColumn[i]==element):
            if(labelCol[i]==1):
                oneOccur+=1
            elif(labelCol[i]==0):
                zeroOccur+=1
    if(oneOccur>=zeroOccur):
        return oneOccur
    else:
        return zeroOccur

def main():
    
    szDatasetPath = sys.argv[1]
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



    #Label encoder to use when encoding features and labels
    le = preprocessing.LabelEncoder()
    #Encode the label array
    classCol = [row[-1] for row in listData]
    classColEncoded = le.fit_transform(classCol)



    # For each feature, compute the training error of a one-level decision tree
    #Iterate through all features
    for i in range(0,len(listColNames)-1):

        #Create a feature array
        featureCol = [row[i] for row in listData]
        #Total numbers of predicted labels
        totalPredict = 0
        #Count number of occurences of label 0 and 1 in each element of each feature
        for element in listColUniqueVals[i]:
            mostOccurAmount = mostOccur(featureCol,element,classColEncoded)
            totalPredict += mostOccurAmount
            #print("Element ", element, " occured ",mostOccurAmount)
        print("Error rate of feature:",listColNames[i],": ",1- totalPredict/len(featureCol))

    # Construct a full decision tree on the dataset and compute the training error
    #Decision tree training on all features
    newListData = []
    for i in range(0,len(listColNames)-1):
        #Create a feature array, then encode it for decision tree
        featureCol = [row[i] for row in listData]
        featureCol = le.fit_transform(featureCol)
        newListData.append(featureCol)
    #Convert and transpose new listData
    encodedData = np.array(newListData)
    encodedData=encodedData.transpose()
    #Decision tree built with sklearn, iterating max depth from 3 to 10
    for n in range(1,21):
        decisiontree = tree.DecisionTreeClassifier(max_depth=n,criterion='entropy')
        decisiontree.fit(encodedData,classColEncoded)
        print("Max depth",n,": Error rate",1-decisiontree.score(encodedData,classColEncoded))
if __name__ == '__main__':
    main()

# %%
