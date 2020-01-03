# -*- coding: UTF-8 -*-
# 功能测试

import file_processing as fp
import random
import math
import numpy as np
import test as t


def calculate(input_data):
    length = len(input_data)
    # score_list = np.array([(math.pow(random.random() - 0.5, 3) * 2 + 1) for i in range(length)])
    score_list = np.array([random.randint(1, 9) for i in range(length)])
    score_list = score_list.reshape(length, 1)
    # score_list = np.random.randint(1, 10, (length, 1))
    print(score_list.T)
    print(np.size(score_list.T, 0))
    print(score_list.T[0, -1])
    multi = score_list.T * score_list
    print("星乘 =\n", multi)
    print("点乘 =\n", np.dot(score_list.T, score_list))
    mean = np.mean(multi, axis=1).reshape(length, 1)
    print("均值 =\n", mean)
    std = np.std(multi, axis=1).reshape(length, 1)
    print("标准差 =\n", std)
    standardization = (multi - mean)/std
    print("中心化 =\n", multi - mean)
    print("标准化 =\n", standardization)
    # print("标准矩阵 =", t.standardization(score_list))
    test = np.random.rand(length, length + 1)
    print(test)
    print("dot=", np.dot(test[0], test[1]))
    print(np.exp(score_list) / np.sum(np.exp(score_list)))
    test_num = np.random.normal(loc=0, scale=1)
    print(test_num)
    # for row in range(test.shape[-1]):
    #     print(test[:, row].reshape(test.shape[0], 1))
    # print(test[:, 1].reshape(length, 1))
    # score = np.dot(test, t.standardization(score_list))
    # print(score)
    # np.savetxt("data/test_out.txt", score, fmt="%.8f")
    # print(np.dot(test, score_list))
    return score_list


if __name__ == "__main__":
    # vocab = fp.dir_io()
    calculate([1, 1, 1, 1])
