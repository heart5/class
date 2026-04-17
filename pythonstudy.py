# ---
# jupyter:
#   jupytext:
#     cell_metadata_filter: -all
#     formats: ipynb,py:percent
#     notebook_metadata_filter: jupytext,-kernelspec,-jupytext.text_representation.jupytext_version
#     text_representation:
#       extension: .py
#       format_name: percent
#       format_version: '1.3'
# ---

# %% [markdown]
# # python学习笔记（***）

# %% [markdown]
# ## 编程英文翻译

# %% [markdown]
# 1. list 列表
# 2. tuple 元组
# 3. dict 字典

# %% [markdown]
# ## 基础数据类型

# %% [markdown]
# 基础类型我学习了str、list、int、bool、tuple、dict
# 列表list是有序的，里面的元素可以是任意类型（包括列表）

# %% [markdown]
# ## cell编辑技巧

# %% [markdown]
# ### 进入和退出编辑模式

# %% [markdown]
# 1. 进入cell默认是宽光标，按下“i”（insert）在光标字母前面处进入可编辑模式，按下“a”（append）在光标字母后面进入编辑模式，按下“o”（open a new line below）则在当前光标的下面新起一行，按下“O”（open a new line above）则在当前光标的上面新起一行
# 2. 按下“Esc”（键盘左上角的键，escape）则退出编辑模式到浏览模式

# %% [markdown]
# ### 复制和粘贴

# %% [markdown]
# 在浏览模式（宽光标）下，按下“yy”复制当前行；按下“P”则把复制的内容粘贴到当前行的上一行

# %% [markdown]
# ### 删除字符串

# %% [markdown]
# #### 删除到指定字符

# %% [markdown]
# 在浏览模式（宽光标）下，按下“dt]”，从当前光标所在字符删除至指定字符

# %% [markdown]
# ### 可视操作

# %% [markdown]
# 按下“v”进入可视操作，“w”选中单词，“]”选中内容块，然后根据需要进行合适的操作，比如整体右移一个Tab，或者注释掉选中内容所在的行

# %% [markdown]
# ### 注释和反注释当前代码行

# %% [markdown]
# “Ctrl+/”可以把当前行的代码在注释和非注释两种状态下切换

# %% [markdown]
# ## cell管理技巧

# %% [markdown]
# ### cell选中状态下，按下“a”（above）在上方新建cell；按下“b”（below）在下方新建cell。

# %%
# print("Today is weekend.")
print("Today is sunny.")

# %%
# !jupyter-labextension install jupyterlab-vimrc

# %%
