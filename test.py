# -*- coding: UTF-8 -*-

import math
import json
import time
import re
import file_processing as fp


# 认知标记
def func_1(input_data):
    input_length = len(input_data)
    input_flag = input_length * [0]
    break_flag = 0
    # 获取词汇表中的相同词（若存在）
    for i, character in enumerate(input_data):
        if break_flag > i:
            continue
        # 初始化同首词集合
        vocab_tmp = []
        # 获取同首词集合
        for item in vocab:
            if character == item[0]:
                vocab_tmp.append(item)
        # 以当前字为起始匹配并标记同首词集合中的最长相同词（若存在）
        for num in range(input_length, i, -1):
            # print(input_data[i:num], i, character, num)
            if input_data[i:num] in vocab_tmp:
                input_flag[i] = 1
                input_flag[num - 1] = 2
                break_flag = num
                break
    phase_flag = 0
    # 将标记转换为[]
    for j, word_flag in enumerate(input_flag):
        j = j + phase_flag
        if word_flag:
            input_data = ' ' + input_data + ' '
            input_data = input_data[:j + word_flag] + chr(89 + 2 * word_flag) + input_data[j + word_flag:]
            input_data = input_data[1:-1]
            phase_flag = phase_flag + 1
    return input_data


# 判断当前词是否在vocab中
def func_2(input_word):
    if input_word not in vocab:
        vocab.append(input_word)


# 对输入文本打认知标记，以段落/行为单位
def func_3():
    with open("data/测试文本2.txt", "r", encoding="UTF-8") as fi:
        print("。".join([func_1(input_segment) for input_segment in fi.readline().split("。")]))


# 结束标记
def func_0():
    print("交流结束")


# 主功能函数
def main_1():
    input_select = input("请选择：1.搜寻模式；2.录入模式；3.交流模式\n")
    if input_select == "1":
        input_info = input("正在聆听：\n")
        while input_info != "0":
            start = time.perf_counter()
            print(func_1(input_info))
            end = time.perf_counter()
            print("查找耗时：" + str("%.6f" % ((end - start) * 1000)) + "ms")
            input_info = input("正在聆听：\n")
    elif input_select == "2":
        input_info = input("请输入：\n")
        while input_info != "0":
            func_2(input_info)
            input_info = input("请输入：\n")
    elif input_select == "3":
        start = time.perf_counter()
        func_3()
        end = time.perf_counter()
        print("查找耗时：" + str("%.6f" % ((end - start) * 1000)) + "ms")
    else:
        print("输入错误")
    func_0()


if __name__ == "__main__":
    vocab = fp.dir_io()
    main_1()
    fp.file_range(vocab)
