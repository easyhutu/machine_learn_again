"""
Author: Meng
Date: 2019/6/4
"""
from numpy import *
import operator
import matplotlib.pyplot as plt
import os


def classify0(inX, dataSet, labels, k):
    dataSetSize = dataSet.shape[0]
    diffMat = tile(inX, (dataSetSize,1)) - dataSet
    sqDiffMat = diffMat**2
    sqDistances = sqDiffMat.sum(axis=1)
    distances = sqDistances**0.5
    sortedDistIndicies = distances.argsort()
    classCount={}
    for i in range(k):
        voteIlabel = labels[sortedDistIndicies[i]]
        classCount[voteIlabel] = classCount.get(voteIlabel,0) + 1
    sortedClassCount = sorted(classCount.items(), key=operator.itemgetter(1), reverse=True)
    return sortedClassCount[0][0]

def img_vector(filename):
    return_vect = zeros((1, 1024))
    fr = open(filename)
    for i in range(32):
        lineStr = fr.readline()
        for j in range(32):
            return_vect[0, 32*8+j] = int(lineStr[j])
    return return_vect


def image_test():
    hw_labels = []
    file_list = os.listdir(r'testDigits')
    print(file_list[0])
    m = len(file_list)
    training_mat = zeros((m, 1024))
    for i in range(m):
        filename_str = file_list[i]
        filestr = filename_str.split('.')[0]
        classnumstr = int(filestr.split('_')[0])
        hw_labels.append(classnumstr)
        training_mat[i, :] = img_vector(r'testDigits/{}'.format(filename_str))
    testfilelist = os.listdir(r'testDigits')
    errorcount = 0.0
    mtest = len(testfilelist)
    for i in range(mtest):
        filenamestr = testfilelist[i]
        filestr = filenamestr.split('.')[0]
        classnumstr = int(filestr.split('_')[0])
        vectorundertest = img_vector(r'testDigits/{}'.format(filenamestr))
        classifierresult = classify0(vectorundertest, training_mat, hw_labels, 3)
        print(f'the class back with: {classifierresult}, real is:{classnumstr}')
        if classifierresult != classnumstr:
            errorcount += 1.0
    print(mtest)
    print(f'error count: {errorcount}')
    print(f'error rate is : {errorcount/float (mtest)}')





if __name__ == '__main__':
    testv = img_vector(r'testDigits/0_0.txt')
    print(testv[0, 32:63])
    image_test()