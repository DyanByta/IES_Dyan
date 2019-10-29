# -*- coding: UTF-8 -*-

import math
import json
import codecs
import time

dir_path = "data/vocab.txt"


# 对vocab文件内容进行字典化排序
def file_range(vocab):
    fo_1 = open(dir_path, 'w', encoding='UTF-8')
    length = len(vocab)
    start = time.perf_counter()
    for i in range(length):
        for j in range(length):
            if vocab[i] > vocab[j]:
                tmp = vocab[i]
                vocab[i] = vocab[j]
                vocab[j] = tmp
    end = time.perf_counter()
    print("排序耗时：" + str("%.6f" % ((end - start) * 1000)) + "ms")
    for vocab_item in vocab:
        fo_1.write(vocab_item + "\n")
    fo_1.close()
    print(vocab)


# 向词表导入vocab的内容
def dir_io():
    vocab = []
    fi_1 = open(dir_path, 'r', encoding='UTF-8')
    for fi_1_line in fi_1:
        vocab.append(fi_1_line.strip())
    fi_1.close()
    return vocab


# 【字典初始化】向vocab写入数据
def dir_write():
    vocab_0 = ['语义空间', '测试样例', '语义解析', '测试纹路', '测试文本', '复杂度', '测试', '测试文本数据集']
    fw_1 = open(dir_path, 'w', encoding='UTF-8')
    for vocab_0_line in vocab_0:
        fw_1.write(vocab_0_line + "\n")
    fw_1.close()


# 【测试初始化】生成测试文本文件
def test_write():
    ft_1 = open("data/测试文本2.txt", 'w', encoding='UTF-8')
    test_txt = "知识抽取涉及的“知识”通常是清楚的、事实性的信息，这些信息来自不同的来源和结构，而对不同数据源进行的知识抽取的方法各有不同，从结构化数据中获取知识用 D2R，其难点在于复杂表数据的处理，包括嵌套表、多列、外键关联等，从链接数据中获取知识用图映射，难点在于数据对齐，从半结构化数据中获取知识用包装器，难点在于 wrapper 的自动生成、更新和维护，这一篇主要讲从文本中获取知识，也就是我们广义上说的信息抽取。实体抽取或者说命名实体识别（NER）在信息抽取中扮演着重要角色，主要抽取的是文本中的原子信息元素，如人名、组织/机构名、地理位置、事件/日期、字符值、金额值等。实体抽取任务有两个关键词：find & classify，找到命名实体，并进行分类。半监督学习主要是利用少量的标注信息进行学习，这方面的工作主要是基于 Bootstrap 的方法以及远程监督方法（distance supervision）。基于 Bootstrap 的方法主要是利用少量实例作为初始种子(seed tuples)的集合，然后利用 pattern 学习方法进行学习，通过不断迭代从非结构化数据中抽取实例，然后从新学到的实例中学习新的 pattern 并扩充 pattern 集合，寻找和发现新的潜在关系三元组。远程监督方法主要是对知识库与非结构化文本对齐来自动构建大量训练数据，减少模型对人工标注数据的依赖，增强模型跨领域适应能力。"
    ft_1.write(test_txt)
    ft_1.close()


if __name__ == "__main__":
    dir_write()
    vocab_list = dir_io()
    file_range(vocab_list)
    # test_write()
