# encoding:utf-8
# 教育机构：哈尔滨工程大学
# 学   生；吴军宝
# 开发时间:2021-12-22 23:14

#功能功能，查找某个文件中的字符串，若不在则输出文件名
import time
import os
import re

import numpy

file_dir='C:\\Users\\18252\\Desktop\\数据集标签'
for root, dirs, files in os.walk(file_dir, topdown=False):

    print(root)  # 当前目录路径
  # print(dirs)  # 当前目录下所有子目录
    print(files)  # 当前路径下所有非目录子文件

#with open()
#readlines()

import codecs


def readFilename(file_dir):
    for root, dirs, files in os.walk(file_dir):  # os.walk是获取文件下文件名的方法
        return files, dirs, root


# 自定义的查找指定字符串的方法
def findstring(pathfile):
    fp = open(pathfile, "r", encoding='utf-8')  # 注意这里的打开文件编码方式
    strr = fp.read()
    if (strr.find(goal) != -1):
       # print('您要查找的文件在这儿吗?')
        return True
    return False


# 输出文件的名字
def startfind(files, dirs, root):
    for ii in files:  # 发现指定的字符在文件中
        try:
            if (findstring(root + "\\" + ii)==0):
                print(list[ii])
             #   input("请问您对结果满意吗(输入任何字符，程序会退出): ")
        except Exception as err:
            print(err)
            continue

    for jj in dirs:
        fi, di, ro = readFilename(root + "\\" + jj)
        startfind(fi, di, ro)


# 程序的入口
if __name__ == '__main__':
    default_dir = r"C:\\Users\\18252\\Desktop\\数据集标签"  # 设置默认打开目录
    file_path = default_dir  # th.expanduser(default_dir)))
    goal = input("请问您想要查找什么字符呢: ")
    files, dirs, root = readFilename(file_path)
    startfind(files, dirs, root)
