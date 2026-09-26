# -*- coding: utf-8 -*-
# ---
# jupyter:
#   jupytext:
#     cell_metadata_filter: -all
#     formats: ipynb,py:percent
#     notebook_metadata_filter: jupytext,-kernelspec,-jupytext.text_representation.jupytext_version
#     split_at_heading: true
#     text_representation:
#       extension: .py
#       format_name: percent
#       format_version: '1.3'
# ---

# %% [markdown]
# # python之禅

# %%
import this

# %%
print("Hi, Python.")
happystr = "I'm happy. Happy weekend."
print(happystr)

# %% [markdown]
# # python基础

# %% [markdown]
# ## python是解释型语言

# %% [markdown]
# 解释型语言是明文编写的代码，被逐行解析并直接运行，速度较慢，但容易学习，容易读懂；相对而言，c语言是编译型语言，需要经过编译过程转换为机器码后运行，特点是速度飞快，但需要更专业的计算机技能。

# %% [markdown]
# ## 常用搜索引擎网址

# %% [markdown]
# 1. google.cn
# 2. bing.com
# 3. baidu.com

# %% [markdown]
# ## 数据类型

# %% [markdown]
# ### 数字

# %%
aaa = 8888
bbb = 9999

# %% [markdown]
# #### 内置命令type()

# %%
print(type(12.0))
print(type(12))
print(type(aaa))
print(type(True))

# %% [markdown]
# #### 数字的四则运算

# %%
print(888 * 890)
print(900 - (44 * 3))
print(8 + 90)
print(98 / 23)
print(29 // 13)
print(29 % 13)

# %%
print(33 % 21)

# %%
print(33 / 11)

# %%
print("*+" * 20)

# %% [markdown]
# #### 四则运算（变量名）

# %%
print(aaa + bbb)
print(aaa - bbb)
print(aaa * bbb)
print(aaa / bbb)
print(aaa % bbb)

# %%
print(bbb)
print(aaa)
print(aaa * bbb)


# %% [markdown]
# #### 课堂作业（乘法口诀）

# %%
def multi_table1(num):    
    for i in range(1, num + 1): # i是行
        for j in range(1, num + 1): # j是列
            result = i * j
            multistr = str(i) + "*" + str(j) + "=" + resultstr
            print(multistr, end="\t")
        print()


# %%
multi_table1(9)


# %%
def multi_table2(num):    
    for i in range(1, num + 1): # i是行
        for j in range(1, num + 1): # j是列
            if i > j :
                continue
            multistr = str(i) + "*" + str(j) + "=" + str(i * j)
            print(multistr, end="\t")
        print()


# %%
multi_table2(9)


# %%
def multi_table3(num):    
    for i in range(1, num + 1): # i是行
        print("\t" * (i - 1), end="")
        for j in range(1, num + 1): # j是列
            if i > j :
                continue
            result = i * j
            if j > 3:
                resultstr = f"{result:2}" if result < 10 else f"{result}"
            else:
                resultstr = f"{result}"
            # resultstr = f"{result:2}" if result < 10 else f"{result}"
            multistr = str(i) + "*" + str(j) + "=" + resultstr
            print(multistr, end="\t")
        print()


# %%
multi_table3(9)

# %%

# %% [markdown]
# ### 字符串

# %%
bstr = "I'm happy.I'm happy.I'm happy.I'm happy.I'm happy.I'm happy.I'm happy."

# %%
print(bstr)

# %% [markdown]
# #### 字符串切片

# %%
abcstr = "aKcdefg"
print(abcstr[4:2:-1])

# %%
bzsstr.title()
bzsstr.upper()
bzsstr.lower()
bzsstr.strip()
bzsstr.split()

# %%
bzsstr = "shang Zihao "
print(bzsstr)
# print(bzsstr[3])
# print(bzsstr[:])
# print(bzsstr[:-1])
# print(bzsstr[1:-1])
print(bzsstr[-1:1:-1])

# %% [markdown]
# ### 列表

# %% [markdown]
# 列表是个框，啥都可以装

# %%
sonls = ["a", "b", "c"]
tlst = [0, 1, 2, 3, 4, "haohao", sonls]
print(tlst)
# 索引取值
print(tlst[4])
# 切片
print(tlst[1:4])
anotherls = [6, 7]
# 列表相加
print(tlst + anotherls)
# 列表乘
print(tlst * 2)
print(len(sonls))
print(max(sonls))
print(min(sonls))

# %% [markdown]
# #### 列表定义

# %%
lista = [0, 2, 900]
lista = ["a", "bk2", "900", "jiushiwu", "0ajfaijjio9fjpafsjp1asjifdapio"]
listb = list()

# %% [markdown]
# dt] delete to ]

# %% [markdown]
# #### 列表内置函数

# %%
print(len(lista))
print(max(lista))
print(min(lista))
print(sorted(lista))

# %% [markdown]
# #### 列表切片

# %%
listc = list(range(15))

# %%
listd = listc[:3:-7]

# %%
list(range(10))

# %% [markdown]
# #### 列表插入删除

# %%
listd.insert(5, 5)

# %%
listd.append(78)

# %%
listd.pop()

# %%
listd

# %% [markdown]
# ### 元组

# %%
stup = (1, 2, 3)

# %%
print(stup)

# %% [markdown]
# ### 集合

# %%
lst2set = [1, 2, 3, 4, 1, 4, 5]

# %%
ttset = set(lst2set)

# %%
print(ttset)

# %%
tset = {'a', 'b', 'c'}

# %%
print(tset)

# %% [markdown]
# ### 字典

# %% [markdown]
# 键值对，key, value。

# %%
tdict = {"age": 12, "height": 150, "man": True}

# %%
print(tdict)

# %%
print(tdict["age"])


# %% [markdown]
# ## 函数

# %% [markdown]
# 三部曲：
# 1. 定义
# 2. 运行
# 3. 调用

# %%
def firsttest():
    print("HihiHi")


# %%
def testodd(num):
    if num % 2 == 0:
        return "偶数"
    else:
        return "奇数"


# %%
print("Home is warmful.")
testodd(128)
ddd = 999
print(ddd)
print(ddd)

# %% [markdown]
# ## 循环

# %% [markdown]
# ### for循环

# %%
tlst = ["mom", "daddy", "brother"]

# %%
for item in tlst:
    print(item)

# %%
for szh in range(len(tlst)):
    print(szh, tlst[szh])

# %% [markdown]
# #### 知识点
# 1. for循环
# 2. range
# 3. tlst[i]，索引取值
# 4. len
# 5. print(i ,tlst[i])

# %% [markdown]
# ##### 测试：要求实现如下输出结果

# %% [markdown]
# - 2 shangzihao
# - 3 baizhenshi
# - 4 yangzixi
# - 5 zhanglingyun

# %% [markdown]
# ##### 测试：要求实现如下输出结果

# %% [markdown]
# 1. 1 * 1 = 1
# 2. 2 * 2 = 4
# 3. 3 * 3 = 9
# 4. 4 * 4 = 16

# %% [markdown]
# ##### 测试：要求实现如下输出结果

# %% [markdown]
# 1. 1 * 2 = 2
# 2. 2 * 3 = 6
# 3. 3 * 4 = 12
# 4. 4 * 5 = 20

# %% [markdown]
# ##### 测试：要求实现如下输出结果

# %% [markdown]
# - 0 1 * 2 = 2
# - 1 2 * 3 = 6
# - 2 3 * 4 = 12
# - 3 4 * 5 = 20

# %% [markdown]
# ##### 测试：要求实现如下输出结果

# %% [markdown]
# * 0 10
# * 1 18
# * 2 28
# * 3 40
# * 4 54

# %% [markdown]
# * 0 1 + 9 = 10
# * 1 2 + 16 = 18
# * 2 3 + 25 = 28
# * 3 4 + 36 = 40
# * 4 5 + 49 = 54

# %%
for i in range(9):
    print(i, i + 1 + (i + 3) * (i + 3))

# %% [markdown]
# ##### 测试：要求实现如下输出结果

# %% [markdown]
# - 0 6
# - 1 9
# - 2 14
# - 3 21
# - 4 30

# %% [markdown]
# ##### 测试：要求实现如下输出结果

# %% [markdown]
# - 9 6
# - 8 9
# - 7 14
# - 6 21
# - 5 30

# %%
for i in range(5):
    print(i, 5 + (i + 1) * (i + 1))

# %%
[(x, 5 + (x + 1) * (x + 1)) for x in range(5)]

# %% [markdown]
# ##### 测试：要求实现如下输出结果

# %% [markdown]
# - 0 15
# - 1 20
# - 2 25
# - 3 30
# - 4 35
# - 5 40

# %% [markdown]
# ##### 测试：要求实现如下输出结果

# %% [markdown]
# - 2 8
# - 3 15
# - 4 22
# - 5 29
# - 6 36
# - 7 43

# %% [markdown]
# ##### 测试：要求实现如下输出结果

# %% [markdown]
# - 2 10
# - 4 28
# - 6 54
# - 8 88
# - 10 130

# %% [markdown]
# ##### 测试：要求实现如下输出结果

# %% [markdown]
# - 2 10
# - 4 28
# - 6 54
# - 8 88
# - 10 130

# %%
list(range(2, 12, 2))

# %%
for i in range(2, 15, 2):
    if i > 10:
        break
    print(i, "\t", i * 3 + i * i)

# %%
for i in range(2, 12, 2):
    print(i, i * (3 + i))

# %%
# %%timeit
for i in range(10000):
    n = i + 1

# %%
# %%timeit
n = 0
while n < 10000:
    n = n + 1

# %%
遍历

# %% [markdown]
# ### while循环

# %% [markdown]
# while循环三要件：
# 1. 判断变量赋值
# 2. 跳出循环条件
# 3. 判断变量修改调整或特定条件break

# %%
n = 0
while n < 5:
    print(n)
    n = n + 1

# %%
n = 0
while n < 5:
    print(n)
    n = n + 1
    if n == 3:
        break

# %%
n = 0
while n < 5:
    print(n)
    n = n + 1
    if n > 3:
        break
else:
    print("The while loop has done normally.")

# %% [markdown]
# # 知识点集锦

# %% [markdown]
# ## 列表解析式

# %% [markdown]
# ### 数值列表解析

# %%
lll = list([1, 2, 3, 4, 5])

# %%
lll = list(range(1, 15))

# %%
[x*x for x in lll]

# %% [markdown]
# #### 用列表解析式生成15以内偶数的平方（新列表）

# %%
[x*x for x in range(15) if x % 2 == 0]

# %%
[x*x for x in range(15) if x % 2 == 1]

# %%
[x*x for x in range(15) if x % 3 == 0]

# %%
[(x, x*x) for x in range(15) if x % 3 == 0]

# %%
evillist = [3, 12]

# %%
[(x, x*x) for x in range(15) if x not in evillist]

# %%
3 % 2 == 0

# %% [markdown]
# ### 字符串列表解析

# %%
lstr = ["shang zi hao", "yang zi xi", "zhang ling yun", "bai zhen shi"]

# %%
[s for s in lstr]

# %%
lstr[0].split()

# %%
[s.split()[0] for s in lstr]

# %% [markdown]
# # 数独问题解决

# %% [markdown]
# ## 定义数组

# %%
l0 = [5, 3, 0, 0, 7, 0, 0, 0, 0]
l1 = [6, 0, 0, 1, 9, 5, 0, 0, 0]
l2 = [0, 9, 8, 0, 0, 0, 0, 6, 0]
l3 = [8, 0, 0, 0, 6, 0, 0, 0, 3]
l4 = [4, 0, 0, 8, 0, 3, 0, 0, 1]
l5 = [7, 0, 0, 0, 2, 0, 0, 0, 6]
l6 = [0, 6, 0, 0, 0, 0, 2, 8, 0]
l7 = [0, 0, 0, 4, 1, 9, 0, 0, 5]
l8 = [0, 0, 0, 0, 8, 0, 0, 7, 9]


# %% [markdown]
# ### def getrawarray()

# %%
def getrawarray():
    """
    获得数独原始题面数组的函数，返回二维数组
    """
    l0 = [5, 3, 0, 0, 7, 0, 0, 0, 0]
    l1 = [6, 0, 0, 1, 9, 5, 0, 0, 0]
    l2 = [0, 9, 8, 0, 0, 0, 0, 6, 0]
    l3 = [8, 0, 0, 0, 6, 0, 0, 0, 3]
    l4 = [4, 0, 0, 8, 0, 3, 0, 0, 1]
    l5 = [7, 0, 0, 0, 2, 0, 0, 0, 6]
    l6 = [0, 6, 0, 0, 0, 0, 2, 8, 0]
    l7 = [0, 0, 0, 4, 1, 9, 0, 0, 5]
    l8 = [0, 0, 0, 0, 8, 0, 0, 7, 9]

    return [l0, l1, l2, l3, l4, l5, l6, l7, l8]


# %%
getrawarray()

# %%
ld = [l0, l1, l2, l3, l4, l5, l6, l7, l8]
ldinput = [l0, l1, l2, l3, l4, l5, l6, l7, l8]


# %%
def getrawarray():
    """
    获得数独原始题面数组的函数，返回二维数组
    """
    l0 = [5, 3, 0, 0, 7, 0, 0, 0, 0]
    l1 = [6, 0, 0, 1, 9, 5, 0, 0, 0]
    l2 = [0, 9, 8, 0, 0, 0, 0, 6, 0]
    l3 = [8, 0, 0, 0, 6, 0, 0, 0, 3]
    l4 = [4, 0, 0, 8, 0, 3, 0, 0, 1]
    l5 = [7, 0, 0, 0, 2, 0, 0, 0, 6]
    l6 = [0, 6, 0, 0, 0, 0, 2, 8, 0]
    l7 = [0, 0, 0, 4, 1, 9, 0, 0, 5]
    l8 = [0, 0, 0, 0, 8, 0, 0, 7, 9]

    return [l0, l1, l2, l3, l4, l5, l6, l7, l8]


# %% [markdown]
# ## 定义显示函数

# %% [markdown]
# ### 深入学习逐行显示和排版

# %% [markdown]
# #### len()

# %%
len(ld)

# %% [markdown]
# #### range()

# %%
range(4)

# %%
range(5, 9)

# %%
for i in range(5, 9):
    print(i)

# %% [markdown]
# #### print()

# %%
print(33, end="|")
print(22)

# %%
uuu = 903
print(f"{uuu}\n\nabc")

# %% [markdown]
# #### 三个数换行

# %%
for i in range(9):
    print(i, end=" ")
    if i % 3 == 2:
        print()

# %% [markdown]
# #### 四个及更多数换行

# %%
for ii in range(16):
    print(ii, end=" ")
    if ii % 4 == 3:
        print("")

# %%
for ii in range(16):
    print(f"{ii:2}", end=" ")
    if ii % 4 == 3:
        print("")

# %%
for ii in range(95, 120):
    print(f"{ii:03}", end=" ")
    if ii % 5 == 4:
        print("")


# %% [markdown]
# 0 1 2 3
# 4 5 6 7 
# 8 9 10 11
# 12 13 14 15

# %% [markdown]
# ### 显示函数迭代

# %% [markdown]
# #### 第一版

# %%
def showmatrix1(ldata):
    for line in range(len(ldata)):
        print(ldata[line])


# %%
showmatrix1(ld)


# %% [markdown]
# #### 第二版

# %%
def showmatrix2(ldata):
    # 取用每一行的数据
    for i in range(len(ldata)):
        # 取用行中每一个数字，并根据位置决定是否换行
        for ii in range(len(ldata[i])):
            endchar = '\n' if ii == (len(ldata[ii]) - 1) else ' '
            print(f"{ldata[i][ii]}{endchar}", end='')


# %%
showmatrix2(ld)


# %% [markdown]
# #### 够用版

# %%
def showmatrix(ldata):
    """
    格式化显示数独矩阵。零则置空，三行、三列显示横线纵线，形成3*3的大方格
    """

    def shownullforzero(x):
        """
        如果值为0则显示空格
        """
        if x == 0:
            return " "
        else:
            return x
    # 第一层循环，处理各行数据
    for i in range(len(ldata)):
        tmpline = [shownullforzero(x) for x in ldata[i]]
#         print(tmpline)
        # 第二层循环，按照位置处理行中间的元素
        for ii in range(len(tmpline)):
            # 行尾换行
            endchar = '\n' if ii == (len(tmpline) - 1) else ' '
            # 逢三加线
#             shuchar = '|' if (ii + 1) % 3 == 0 else ''
            shuchar = '|' if ii % 3 == 2 else ''
#             print(f"{str(tmpline[ii])}{shuchar}", end=endchar)
            print(f"{tmpline[ii]}{shuchar}", end=endchar)
        # 每三行输出横线
        if ((i + 1) % 3) == 0:
            print("--" * (len(ldata) + 1))
#     print("\n")


# %%
showmatrix(getrawarray())


# %% [markdown]
# ## 找出每个位置的斥集

# %% [markdown]
# ### getvalues函数定义

# %%
def getvalues(ldata, x, y):
    """
    得到指定坐标处的斥值集，返回可能的值集
    ldata: 二维数组
    x: 横坐标
    y: 纵坐标
    """
#     print(len(ldata), len(ldata[0]))
    if not (x < len(ldata) and y < len(ldata[0])):
        print(f"坐标（{x}，{y}）溢出")
        return

    # 获取行中包含的数字，存入集合tgset
    tgset = set(ldata[x])

    # 获取列种包含的数字，添加到集合tget
    for i in range(len(ldata)):
        tgset.add(ldata[i][y])

    # 获取方块中包含的数字，添加到集合tgset
    startx = (x // 3) * 3
    starty = (y // 3) * 3
    for i in range(3):
        for j in range(3):
            tgset.add(ldata[startx + i][starty + j])

    # 获取反值列表，用列表解析的方式获取
    valuelist = [x for x in range(len(ldata) + 1) if x not in tgset]

    return valuelist


# %%
def getvalues1(ldata, x, y):
    """
    得到指定坐标处的斥值集，返回可能的值集
    """
    if not (x < len(ldata) and y < len(ldata[0])):
        print(f"坐标（{x}，{y}）溢出")
        return
#     print(f"({x},{y}):\t{ldata[x][y]}")
    # 行斥值进入集合
#     print(f"所在行值：\t{ldata[x]}")
    tgset = set(ldata[x])
#     print(f"斥值集合：\t{tgset}")
    # 列斥值进入集合
    tmplst = []
    for i in range(len(ldata)):
        tmplst.append(ldata[i][y])
        tgset.add(ldata[i][y])
#     print(f"所在列值：\t{tmplst}")
#     print(f"斥值集合：\t{tgset}")
    # 方块斥值进入集合
    # 找到方块的低角坐标
    startx = (x // 3) * 3
    starty = (y // 3) * 3
#     print(f"方块起点坐标：\t（{startx}, {starty}）")
    fkdata = []
    for i in range(3):
        tmpl = []
        for j in range(3):
            tmpl.append(ldata[startx + i][starty + j])
            tgset.add(ldata[startx + i][starty + j])
        fkdata.append(tmpl)
#     showmatrix(fkdata)
#     print(f"斥值集合：\t{tgset}")
    # 反转，得到可能的值集
    valuelist = [x for x in range(len(ldata) + 1) if x not in tgset]

    return valuelist


# %% [markdown]
# ### getvalues函数调用

# %%
ld_raw = getrawarray()
showmatrix(ld_raw)
getvalues(ld_raw, 8, 2)


# %% [markdown]
# ## 解题

# %% [markdown]
# ### def getblankvalues(ldata)

# %%
def getblankvalues(ldata):
    """
    遍历二维数组，得到空值处可能的值集，返回最短的那个值集（一般就是确定了具体数字的）；如果全部完成，则返回None
    """
    valnum = 9
    targetset = set()
    pos = None
    for i in range(len(ldata)):
        for j in range(len(ldata[0])):
            if ldata[i][j] == 0:
                tgvalues = list(getvalues(ldata, i, j))
                if len(tgvalues) <= valnum:
                    valnum = len(tgvalues)
                    pos = [i, j]
                    targetset = tgvalues
#                     print(f"{pos}:\t{valnum}\t{targetset}")
                    continue

    if pos:
        return [pos, targetset]


# %%
getblankvalues(ld_raw)

# %% [markdown]
# ### 循环填值

# %%
# 遍历整张表，返回值集最短的那个坐标并填充数据，然后继续，直到全部填充完毕
while (rtvalues := getblankvalues(ld_raw)) and (len(rtvalues[1]) == 1):
    print(rtvalues)
    vline = ld_raw[rtvalues[0][0]]
    vline[rtvalues[0][1]] = rtvalues[1][0]
    ld_raw[rtvalues[0][0]] = vline
    showmatrix(ld_raw)
    print("\n")

# %%

# %% [markdown]
# # 测试训练

# %%
print("Hey, python, I'm here now.")

# %%
print("I'm happy now.")

# %%
print("Happy weekend.")

# %%
