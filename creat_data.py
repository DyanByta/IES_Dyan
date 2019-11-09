# -*- coding: UTF-8 -*-

import file_processing as fp
import random
import math
import numpy as np
import test as t


def calculate(input_data):
    length = len(input_data)
    score_list = np.array([(math.pow(random.random() - 0.5, 3) * 2 + 1) for i in range(length)])
    score_list = score_list.reshape(len(input_data), 1)
    # score_list = np.random.randint(1, 10, (length, 1))
    print(score_list)
    print("星乘 =", score_list.T * score_list)
    print("点乘 =", np.dot(score_list.T, score_list))
    # print("标准矩阵 =", t.standardization(score_list))
    test = np.random.rand(length, length + 1)
    print(test)
    print(np.exp(score_list) / np.sum(np.exp(score_list)))
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
    calculate([1, 1, 1])
