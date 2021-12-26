# -*- coding: utf-8 -*-
# ---
# jupyter:
#   jupytext:
#     text_representation:
#       jupytext_version: 1.13.4
#   kernelspec:
#     display_name: Python 3.9 (XPython)
#     language: python
#     name: xpython
# ---

# %% [markdown]
# # python之禅

# %%
import this

# %% tags=[]
print("Hi, Python.")
happystr = "I'm happy. Happy weekend."
print(happystr)

# %% [markdown]
# # python基础

# %% [markdown]
# ## 数据类型

# %% [markdown]
# ### 数字

# %%
aaa =8888
bbb = 9999

print(bbb)
print(aaa)
print(aaa + bbb)

# %%
# %config Completer.use_jedi = False

# %% [markdown]
# ### 字符串

# %%
bstr = "I'm happy.I'm happy.I'm happy.I'm happy.I'm happy.I'm happy.I'm happy."

# %%
print(bstr)

# %% [markdown]
# ### 列表

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
# ### 元组

# %%
stup = (1, 2, 3)

# %%
print(stup)

# %% [markdown]
# ### 集合

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

# %% [markdown]
# ### while循环

# %%
n = 0
while n < 5:
    print(n)
    n = n + 1

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

# %%
ld = [l0, l1, l2, l3, l4, l5, l6, l7, l8]

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

# %% [markdown]
# #### print()

# %%
print(33, end="|")

# %%
uuu = 903
print(f"{uuu}\n\nabc")

# %% [markdown]
# #### 三个数换行

# %%
for i in range(9):
    print(i, end=" ")
    if i % 3 == 2:
        print("")

# %% [markdown]
# #### 四个及更多数换行

# %%
for ii in range(16):
    print(ii, end=" ")
    if ii % 4 == 3:
        print("")

# %%
for ii in range(16):
    print(f"{ii:02}", end=" ")
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
# #### 字符串切片

# %%
bzsstr = "baizhenshi"
print(bzsstr[3])
print(bzsstr[:-1])
print(bzsstr[1:-1])
print(bzsstr[1:])


# %% [markdown]
# ### 显示函数迭代

# %%
def showmatrix1(ldata):
    for line in range(len(ldata)):
        print(ldata[line])


# %%
showmatrix1(ld)


# %%
def showmatrix2(ldata):
    for i in range(len(ldata)):
        for ii in range(len(ldata[i])):
            endchar = '\n' if ii == (len(ldata[ii]) - 1) else ' '
            print(f"{ldata[i][ii]}{endchar}", end='')


# %%
showmatrix2(ld)


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
            if ii == (len(tmpline) - 1):
                endchar = '\n'
            else:
                endchar = ' '
            # endchar = '\n' if ii == (len(tmpline) - 1) else ' '
            shuchar = '|' if (ii + 1) % 3 == 0 else ''
            print(f"{str(tmpline[ii])}{shuchar}", end=endchar)
        # 每三行输出横线
        if ((i + 1) % 3) == 0:
            print("--" * (len(ldata) + 1))
#     print("\n")


# %%
showmatrix(ld)

# %% [markdown]
# # 测试训练

# %%
print("Hey, python, I'm here now.")

# %%
print("I'm happy now.")

# %%
print("Happy weekend.")

# %%
