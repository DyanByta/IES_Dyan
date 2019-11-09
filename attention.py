# -*- coding: UTF-8 -*-

import math
import json
import time
import re
from tqdm import tqdm
import random
import numpy as np

dir_path = "data/测试.txt"
outer_path = "data/结果.txt"
flag_sentence = "En Taro Zeratul!"
feature_size = 42
max_step = 50


# 标准化
def standardization(input_data):
    data_mean = np.mean(input_data)
    data_sigma = np.std(input_data)
    return (input_data - data_mean) / data_sigma


# 归一化
def normalization(input_data):
    data_min = np.min(input_data)
    return (input_data - data_min) / (np.max(input_data) - data_min)


# softmax
def softmax(input_data):
    data_exp = np.exp(input_data)
    return data_exp / np.sum(data_exp)


# 计算相似性
def get_similarity(vector_1, vector_2):
    similarity = np.dot(vector_1.T, vector_2) / (np.linalg.norm(vector_1) * np.linalg.norm(vector_2))
    return similarity


# 获取value向量
def get_value(word):
    # value = np.array([(math.pow(random.random() - 0.5, 3) * 2) * (ord(word) - 19967) for i in range(feature_size)])
    value = np.array([random.random() for i in range(feature_size)])
    value = value.reshape(feature_size, 1)
    return value


# 注意力
def attention(query, value_list):
    list_length = value_list.shape[-1]
    similarities = np.zeros(shape=(list_length, 1))
    for key_index in range(list_length):
        similarities[key_index] = get_similarity(value_list[:, key_index].reshape(value_list.shape[0], 1), query)
    # similarities = standardization(similarities)
    # similarities = normalization(similarities)
    similarities = softmax(similarities)
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
def get_attention():
    with open(dir_path, 'r', encoding='UTF-8') as ft:
        text = [input_segment + "。" for input_segment in ft.readline().split("。") if input_segment != ""]

    corpus_value = get_text_value(text[0])
    corpus_feature = self_attention(corpus_value)

    text_loop = corpus_feature
    step_count = tqdm(range(max_step))
    for i in step_count:
        text_loop = self_attention(text_loop)
        step_count.set_description("计算进度")
        step_count.set_postfix(loss=random.random())
        time.sleep(0.001)

    print("【文本内容】\n", text[0])
    print("【初始参数】\n", corpus_value)
    print("【1次训练结果】\n", corpus_feature)
    print("【%i次训练结果】\n" % max_step, text_loop)

    # 请无视数据格式提醒↓
    # np.savetxt(outer_path, corpus_feature, fmt="%.8f")


if __name__ == "__main__":
    get_attention()
