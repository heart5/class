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
# # 数独解题

# %% [markdown]
# ## 功能模块

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


# %% [markdown]
# ### showmatrix(ladata), 显示函数迭代

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
    for hang in range(len(ldata)):
        # print(ldata[hang])
        tmpline = [shownullforzero(x) for x in ldata[hang]]
        # print(tmpline)
        # 第二层循环，按照位置处理行中间的元素
        for lie in range(len(tmpline)):
            # 行尾换行
            endchar = '\n' if lie == (len(tmpline) - 1) else ' '
            # 逢三加竖线
#             shuchar = '|' if (ii + 1) % 3 == 0 else ''
            shuchar = '|' if (lie % 3) == 2 else ''
#             print(f"{str(tmpline[ii])}{shuchar}", end=endchar)
            print(f"{tmpline[lie]}{shuchar}", end=endchar)
        # 每三行输出横线
        if ((hang + 1) % 3) == 0:
            print("--" * (len(ldata) + 1))
#     print("\n")


# %%
showmatrix(getrawarray())


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


# %% [markdown]
# ## 循环遍历，填充数值

# %%
# 生成数独题面的数组（二维）
ld_raw = getrawarray()

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
