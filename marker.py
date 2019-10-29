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
        # 跳过标记词
        if break_flag > i:
            continue
        # 初始化同首词集合及最长词长度
        vocab_tmp = []
        vocab_tmp_max = 0
        # 获取同首词集合
        break_sig = 0
        for item in vocab:
            if character == item[0]:
                break_sig = len(item)
                vocab_tmp.append(item)
                if break_sig > vocab_tmp_max:
                    vocab_tmp_max = break_sig
            elif break_sig:
                break
        # 以当前字为起始匹配并标记同首词集合中的最长相同词（若存在）
        for num in range(min(i + vocab_tmp_max, input_length), i, -1):
            if input_data[i:num] in vocab_tmp:
                input_flag[i] = 1
                input_flag[num - 1] = 2
                break_flag = num
                break
    # 将标记转换为[]
    phase_flag = 0
    for j, word_flag in enumerate(input_flag):
        j = j + phase_flag
        if word_flag:
            input_data = ' ' + input_data + ' '
            input_data = input_data[:j + word_flag] + chr(89 + 2 * word_flag) + input_data[j + word_flag:]
            input_data = input_data[1:-1]
            phase_flag += 1
    return input_data


# 对输入文本打认知标记，以段落/行为单位
def func_2(test_dir):
    txt_dir = "data/" + test_dir + ".txt"
    try:
        with open(txt_dir, "r", encoding="UTF-8") as fi:
            print("。".join([func_1(input_segment) for input_segment in fi.readline().split("。")]))
    except IOError:
        print("文件无法读取！")


# 处理新词输入
def func_3(input_word):
    if input_word == "help":
        print("返回操作：0\n删除操作：del 待删除词\n")
    elif input_word[:3] == "del":
        if input_word[4:] in vocab:
            vocab.remove(input_word[4:])
            print("删除成功！")
        else:
            print("不存在！")
    else:
        if input_word not in vocab:
            vocab_new.append(input_word)
            print("添加成功！")
        else:
            print("已存在！")


# 结束标记
def func_0():
    print("交流结束")


# 主功能函数——标记
def marker():
    input_select = input("请选择：1.手打模式；2.文件模式；3.录入模式；0.结束\n")
    while input_select != 0:
        if input_select == "1":
            input_info = input("正在聆听（输入0返回上一层）：\n")
            while input_info != "0":
                start = time.perf_counter()
                print(func_1(input_info))
                end = time.perf_counter()
                print("查找耗时：" + str("%.6f" % ((end - start) * 1000)) + "ms")
                input_info = input("正在聆听（输入0返回上一层）：\n")
        elif input_select == "2":
            input_info = input("请输入文件名（输入0返回上一层）：\n")
            while input_info != "0":
                start = time.perf_counter()
                func_2(input_info)
                end = time.perf_counter()
                print("查找耗时：" + str("%.6f" % ((end - start) * 1000)) + "ms")
                input_info = input("请输入文件名（输入0返回上一层）：\n")
        elif input_select == "3":
            input_info = input("请输入单词（输入0返回上一层）：\n")
            while input_info != "0":
                func_3(input_info)
                input_info = input("请输入单词（输入0返回上一层）：\n")
            fp.file_range(vocab, vocab_new)
        elif input_select == "0":
            print("交流结束")
            break
        else:
            print("输入错误！")
        input_select = input("请选择：1.手打模式；2.文件模式；3.录入模式；0.结束\n")


if __name__ == "__main__":
    vocab = fp.dir_io()
    vocab_new = []
    marker()
