# -*- coding: UTF-8 -*-
# 嵌入表示为行向量


import math
import time
from tqdm import tqdm
import random
import numpy as np

dir_path = "data/测试.txt"
outer_path = "data/结果.txt"
flag_sentence = "En Taro Zeratul!"
feature_size = 4
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


# 计算相似性 - 向量dot模式
def get_similarity_dot(vector_1, vector_2):
    similarity = np.dot(vector_1, vector_2) / np.sqrt(vector_1.size)
    return similarity


# 生成value
def get_value(word):
    value = np.array([np.random.normal(loc=0, scale=1) for i in range(feature_size)])
    return value


# 注意力
def attention(query, value_list):
    list_length = value_list.shape[0]
    similarities = np.zeros(shape=(1, list_length))
    for key_index in range(list_length):
        similarities[0, key_index] = get_similarity_dot(query, value_list[key_index])
    similarities = softmax(similarities)
    # 求加权和
    return np.dot(similarities, value_list)


# 自注意力
def self_attention(input_data):
    data_length = input_data.shape[0]
    feature_list = np.zeros(shape=(data_length, input_data.shape[-1]))
    for query_index in range(data_length):
        feature_list[query_index] = attention(input_data[query_index], input_data)
    return feature_list


# value初始化
def get_text_value(input_text):
    value_list = np.zeros(shape=(len(input_text), feature_size))
    for word_index, word in enumerate(input_text):
        value_list[word_index] = get_value(word)
    return value_list


# 功能函数
def get_attention(text_input):
    corpus_value = get_text_value(text_input)
    corpus_feature = self_attention(corpus_value)

    text_loop = corpus_feature
    step_count = tqdm(range(max_step))
    for i in step_count:
        text_loop = self_attention(text_loop)
        step_count.set_description("计算进度")
        step_count.set_postfix(loss=random.random())

    print("【文本内容】\n", text_input)
    print("【初始参数】\n", corpus_value)
    print("【1次训练结果】\n", corpus_feature)
    print("【%i次训练结果】\n" % max_step, text_loop)

    # 请无视数据格式提醒↓
    # np.savetxt(outer_path, corpus_feature, fmt="%.8f")

    return text_loop


if __name__ == "__main__":
    with open(dir_path, 'r', encoding='UTF-8') as ft:
        text = [input_segment + "。" for input_segment in ft.readline().split("。") if input_segment != ""]
    attention_value = get_attention(text[0].strip("。"))
