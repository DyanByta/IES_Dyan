# -*- coding: UTF-8 -*-

import time

dir_path = "data/vocab.txt"


# 对vocab文件内容进行插入式增量更新
def file_range(vocab, vocab_add):
    start = time.perf_counter()
    length = len(vocab)
    for word in vocab_add:
        for insert_index in range(length):
            if vocab[insert_index] < word:
                vocab.insert(insert_index, word)
                break
    end = time.perf_counter()
    print("排序耗时：" + str("%.6f" % ((end - start) * 1000)) + "ms")
    with open(dir_path, 'w', encoding='UTF-8') as fo_1:
        for vocab_item in vocab:
            fo_1.write(vocab_item + "\n")
    print(vocab)
    print("共计" + str(len(vocab)) + "个词")


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
def txt_write():
    with open("data/测试.txt", 'w', encoding='UTF-8') as ft_1:
        test_txt = input("请输入文本：\n")
        ft_1.write(test_txt)
        print("录入成功！")


if __name__ == "__main__":
    # dir_write()
    vocab_list = dir_io()
    vocab_new = []
    file_range(vocab_list, vocab_new)
    # txt_write()
