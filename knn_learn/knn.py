"""
Author: Meng
Date: 2019/5/19
"""
from numpy import *
import operator
import matplotlib.pyplot as plt


def create_data_set():
    group = array([[1.0, 1.1], [1.0, 1.0], [0, 0], [0, 0.1]])
    labels = ['a', 'a', 'b', 'b']
    return group, labels


def classify0(inx, data_set, labels, k):
    data_set_size = data_set.shape[0]
    # print(data_set_size)
    t = tile(inx, (data_set_size, 1))
    # print(t)
    diffmat = t - data_set
    # print(diffmat)
    sqdiffmat = diffmat ** 2
    sqdistances = sqdiffmat.sum(axis=1)
    distances = sqdistances ** 0.5
    # print(distances)
    sorted_dist_indicies = distances.argsort()
    # print(sorted_dist_indicies)
    class_count = {}
    for i in range(k):
        voteilabel = labels[sorted_dist_indicies[i]]
        # print(voteilabel)
        class_count[voteilabel] = class_count.get(voteilabel, 0) + 1
    sorted_class_count = sorted(class_count.items(), key=operator.itemgetter(1), reverse=True)
    # print(sorted_class_count)
    return sorted_class_count[0][0]


def file_matrix(filename):
    with open(filename) as f:
        data = f.readlines()
    number_lines = len(data)
    return_mat = zeros((number_lines, 3))
    class_label_vector = []
    index = 0
    labels = []
    for line in data:
        line = line.strip()
        list_form_line = line.split('\t')

        return_mat[index, :] = list_form_line[0:3]
        if list_form_line[-1] not in labels:
            labels.append(list_form_line[-1])
        class_label_vector.append(labels.index(list_form_line[-1]) + 1)
        index += 1
    return return_mat, class_label_vector, labels


def show_filed(data):
    fig = plt.figure()
    ax = fig.add_subplot(111)
    ax.scatter(data[0][:, 0], data[0][:, 1], 15.0 * array(data[1]), 15.0 * array(data[1]))
    # ax.axis([-2, 25, -0.2, 2.0])
    plt.xlabel('plan km')
    plt.ylabel('game time')

    plt.show()


def autoNorm(data):
    minval = data.min(0)
    print(minval)

    maxval = data.max(0)
    print(maxval)
    ranges = maxval - minval
    print(ranges)
    normdataset = zeros(shape(data))
    m = data.shape[0]
    print(tile(minval, (m, 1)))
    normadataset = data - tile(minval, (m, 1))
    print(normadataset)
    normadataset = normadataset / tile(ranges, (m, 1))
    return normadataset, ranges, minval


def datingclasstest():
    hotatio = 0.5
    datingdatamat, datinglabels, a = file_matrix(r'datingTestSet.txt')
    normat, rages, minvals = autoNorm(datingdatamat)
    errorcount = 0
    m = normat.shape[0]
    numtest = int(m * hotatio)
    for i in range(numtest):
        classifierresult = classify0(normat[i, :], normat[numtest:m, :], datinglabels[numtest:m], 5)
        print(f'the calssif came: {classifierresult}, real: {datinglabels[i]}')
        if classifierresult != datinglabels[i]: errorcount += 1
    print(f'rate: {errorcount/float(numtest)*100}%')


if __name__ == '__main__':
    # data = create_data_set()
    # r = classify0([1, 1], data[0], data[1], 3)
    # print(r)
    # for da in data[0]:
    #     plt.scatter(*da)
    # plt.show()
    data = file_matrix(r'datingTestSet.txt')
    print(data[2])
    show_filed(data)
    m = autoNorm(data[0])
    print(m[0])
    datingclasstest()
