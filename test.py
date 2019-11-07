# -*- coding: UTF-8 -*-

import math
import json
import time
import re
import random
import math
import numpy as np
import file_processing as fp
from marker import func_1 as mark

dir_path = "data/测试.txt"
outer_path = "data/结果.txt"
flag_sentence = "En Taro Zeratul!"
feature_size = 42
max_step = 30


# 标准差
def standardization(input_data):
    data_mean = np.mean(input_data)
    data_sigma = np.std(input_data)
    # print("平均值 =", data_mean, "\n标准差 =", data_sigma)
    return (input_data - data_mean) / data_sigma


# 归一计算
def to_one(input_data):
    return input_data / np.sum(input_data)


# 计算相似性
def get_similarity(vector_1, vector_2):
    similarity = np.dot(vector_1.T, vector_2) / (np.linalg.norm(vector_1) * np.linalg.norm(vector_2))
    return similarity


# 获取value向量
def get_value(word):
    value = np.array([(math.pow(random.random() - 0.5, 3) * 2 + 1) * (ord(word) - 19967) for i in range(feature_size)])
    value = value.reshape(feature_size, 1)
    return value


# 注意力
def attention(query, value_list):
    list_length = value_list.shape[-1]
    similarities = np.zeros(shape=(list_length, 1))
    for key_index in range(list_length):
        similarities[key_index] = get_similarity(value_list[:, key_index].reshape(value_list.shape[0], 1), query)
    # 标准化
    # similarities = standardization(similarities)
    similarities = to_one(similarities)
    # 求加权和
    return np.dot(value_list, similarities)


# 自注意力
def self_attention(input_data):
    data_length = input_data.shape[-1]
    feature_list = np.zeros(shape=(input_data.shape[0], data_length))
    for query_index in range(data_length):
        feature_list[:, query_index] = attention(input_data[:, query_index], input_data)[:, 0]
    return feature_list


# value初始化
def get_text_value(input_text):
    text_length = len(input_text)
    value_list = np.zeros(shape=(feature_size, text_length))
    for word_index, word in enumerate(input_text):
        value_list[:, word_index] = get_value(word)[:, 0]
    return value_list


# 功能函数
def main():
    with open(dir_path, 'r', encoding='UTF-8') as ft:
        text = [input_segment + "。" for input_segment in ft.readline().split("。") if input_segment != ""]

    corpus_value = get_text_value(text[0])
    corpus_feature = self_attention(corpus_value)

    i = 0
    text_loop = corpus_feature
    while i < max_step:
        text_loop = self_attention(text_loop)
        i += 1

    print(text[0])
    print(corpus_value)
    print(corpus_feature)
    print(text_loop)

    # 请无视数据格式提醒↓
    # np.savetxt(outer_path, corpus_feature, fmt="%.8f")


if __name__ == "__main__":
    # vocab = fp.dir_io()
    main()
