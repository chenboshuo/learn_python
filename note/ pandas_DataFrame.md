# -*- coding: utf-8 -*-
---
jupyter:
  jupytext:
    formats: ipynb,py:light,md
    text_representation:
      extension: .md
      format_name: markdown
      format_version: '1.2'
      jupytext_version: 1.3.3
  kernelspec:
    display_name: Python 3
    language: python
    name: python3
---

# pandas 库
- [官方网站](http://pandas.pydata.org/)

pandas中的datafram的操作，很大一部分跟numpy中的二维数组的操作是近似的

```python
import pandas as pd
```

## Introducing the Pandas DataFrame
Pandas DataFrames are data structures that contain:

-   Data organized in two dimensions, rows and columns
-   Labels that correspond to the rows and columns

```python
data = {
     'name': ['Xavier', 'Ann', 'Jana', 'Yi', 'Robin', 'Amal', 'Nori'],
     'city': ['Mexico City', 'Toronto', 'Prague', 'Shanghai',
              'Manchester', 'Cairo', 'Osaka'],
     'age': [41, 28, 33, 34, 38, 31, 37],
     'py-score': [88.0, 79.0, 81.0, 80.0, 68.0, 61.0, 84.0]
 }

row_labels = [101, 102, 103, 104, 105, 106, 107]
df = pd.DataFrame(data=data, index=row_labels)
df
```

## 读取文件 快速预览

```python
df = pd.read_csv('text_files/death_valley_2014.csv')
df.head() # 读取文件,默认显示前5行
```

```python
df.tail() # 显示最后几行
```

```python
df.info()
```

```python
# 把所有有数据类型的数据做一个简单统计
df.describe()
```

```python
type(df)
```

## 信息提取


### 获取列名

```python
df.columns
```

### 获取索引

```python
df.index
```

说明从0开始,360行结束(不包括360)


### 获取某一行信息

```python
df.loc[0]  # 如果索引不是数字,那么里面填对应索引
df.iloc[0] #  如果索引不是数字,那么里面还是填数字
# df.ix[0]   # 这个是自动指定
'''
.ix is deprecated. Please use
.loc for label based indexing or
.iloc for positional indexing
第三个好像有警告
'''
```

```python
df.loc[360]
```

### 获取某一列信息

```python
# 名字不带空格可以这样访问
df.PST[:10]
```

```python
# 名字带空格这样访问
df['Max TemperatureF'][:3]
```

```python
# 访问多列
df[['Max TemperatureF','Min TemperatureF']][:3]
```

## 数据处理


### 统计空数据数量

```python
df.isnull().sum()
```

```python
# 将空赋值
df.fillna(0)
```

```python
# 直接填充
df.fillna(0,inplace=True)
df.isnull().sum()
```

### 求中位数

```python
df.median()
```

### 筛选

```python
df['Max TemperatureF'] > 105
```

```python
type(df['Max TemperatureF'] > 65)
```

```python
df[df['Max TemperatureF'] > 109]
```

### 多条件的筛选

```python
df[(df['Max TemperatureF'] > 105) & (df['Min TemperatureF']>70)]
```

```python
df[(df['Max TemperatureF'] > 105) and (df['Min TemperatureF']>70)]
```

### 排序

```python
df.sort_values(['Mean TemperatureF'])[:5]
```

```python
df.sort_values(['Mean TemperatureF'])[:-3:-1] # 倒着排序只能用切片了
```

```python
#　多个数据排序
df.sort_values(['Mean TemperatureF','Min TemperatureF'])[:5]
```

### 获取数组

```python
df['Mean TemperatureF'].values
```

### 简单统计

```python
df['Mean TemperatureF'].value_counts()
```

### 分类

```python
def is_cool(temperature):
    if temperature < 50:
        # 大约是10摄氏度
        return 'cool'
    else:
        return 'not_so_cool'

# 利用map函数
df['is_cool?'] = df['Mean TemperatureF'].map(is_cool)
df[['is_cool?','Mean TemperatureF']].head(15)
```

### 对全体应用函数

```python
df.applymap(lambda x: str(x)+'...').head()
```

### 删除数据

```python
df = df.drop(['is_cool?'],axis=1) # 利用drop去掉最后一列
df.head()
```

```python
# 还好不是彻底改变
df.head()
```

## 修改索引

```python
scores = {'英语':[90, 70,89],
         '数学':[64, 78, 45],
          '姓名':['w','l','s']
         }
d = pd.DataFrame(scores, index=['a','b','c'])
d
```

```python
d.iloc[0]
```

```python
d.loc['a']
```

```python
df[:2]
```

## 绘图


### 线性图

```python
# 在单元里显示
%matplotlib inline
df.plot()
```

```python
df['Max TemperatureF'].plot()
```

### 柱状图

```python
df[['Max TemperatureF','Mean TemperatureF']].plot.bar()
```

```python
# 也可以这样写
df[['Max TemperatureF','Mean TemperatureF']].plot(kind='bar')
```

### 直方图

```python
# 单独
df[['Max TemperatureF','Mean TemperatureF']].hist()
```

```python
# 合并
df[['Max TemperatureF','Mean TemperatureF']].plot.hist()
```

### 密度图

```python
df[['Max TemperatureF','Mean TemperatureF']].plot.kde()
```

# reference


-   [The Pandas DataFrame: Make Working With Data Delightful](https://realpython.com/pandas-dataframe/)
