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
py_score = pd.DataFrame(data=data, index=row_labels)
py_score
```

In this table, the first row contains the **column labels** (name, city, age, and py-score). The first column holds the **row labels** (101, 102, and so on). All other cells are filled with the **data values**.
![from_realpython](https://files.realpython.com/media/fig-1.d6e5d754edf5.png)


## 生成DataFrame


### 字典生成

```python
d = {'x': [1, 2, 3], 
     'y': np.array([2, 4, 8]), 
     'z': 100
    }
pd.DataFrame(d)
```

```python
# 指定索引, 列的顺序
pd.DataFrame(d, index=[100, 200, 300], columns=['z', 'y', 'x'])
```

### 列表创建


#### use a list of dictionaries 

```python
l = [{'x': 1, 'y': 2, 'z': 100},
     {'x': 2, 'y': 4, 'z': 100},
     {'x': 3, 'y': 8, 'z': 100}]
pd.DataFrame(l)
```

#### use a nested list

```python
l = [[1, 2, 100],
     [2, 4, 100],
     [3, 8, 100]]
df_l = pd.DataFrame(l, columns=['x', 'y', 'z'])
df_l
```

```python
l[0][0] = 999
df_l
```

### Creating a Pandas DataFrame With NumPy Arrays

```python
arr = np.array([[1, 2, 100],
                [2, 4, 100],
                [3, 8, 100]])
df_arr = pd.DataFrame(arr, columns=['x', 'y', 'z'])
df_arr
```

```python
arr[0,0] = 1000
df_arr
```

If this behavior isn’t what you want, then you should specify copy=True in the DataFrame constructor. That way, `df_arr` will be created with a copy of the values from arr instead of the actual values.


### 文件读取

```python
dath_valley = pd.read_csv('text_files/death_valley_2014.csv')
dath_valley.head()
```

## 快速预览

```python
py_score.head() # 默认显示前5行
```

```python
py_score.head(n=2)
```

```python
py_score.tail() # 显示最后几行
```

```python
py_score.info()
```

```python
# 把所有有数据类型的数据做一个简单统计
py_score.describe()
```

```python
type(py_score)
```

## 信息提取


### 获取列名

```python
py_score.columns
```

### 获取索引

```python
py_score.index
```

### 获取某一行信息

```python
# df.ix[0]   # 这个是自动指定
'''
.ix is deprecated. Please use
.loc for label based indexing or
.iloc for positional indexing
第三个好像有警告
'''
py_score.loc[103]  # 索引(默认是数字)

```

```python
py_score.iloc[2] #  行号
```

![from real python](https://files.realpython.com/media/fig-3.2e2d5c452c23.png)


### 获取某一列信息

```python
# 名字不带空格可以这样访问
py_score.city
```

```python
# 名字带空格这样访问
cities = py_score['city']
cities
```

![from realpython](https://files.realpython.com/media/fig-2.2bee1e181467.png)

```python
# 访问多列
py_score[['name', 'city']]
```

### 获取数组
Data as NumPy Arrays

```python
py_score.to_numpy()
```

```python
py_score.values
```

![from real python](https://files.realpython.com/media/fig-4.a19aadbe0f10.png)


## 数据处理


### 统计空数据数量

```python
dath_valley.isnull().sum()
```

```python
# 将空赋值
dath_valley.fillna(0)
```

```python
# 直接填充
dath_valley.fillna(0,inplace=True)
dath_valley.isnull().sum()
```

### 求中位数

```python
dath_valley.median()
```

### 筛选

```python
dath_valley['Max TemperatureF'] > 105
```

```python
type(dath_valley['Max TemperatureF'] > 65)
```

```python
dath_valley[dath_valley['Max TemperatureF'] > 109]
```

### 多条件的筛选

```python
dath_valley[(dath_valley['Max TemperatureF'] > 105) & (dath_valley['Min TemperatureF']>70)]
```

```python
dath_valley[(dath_valley['Max TemperatureF'] > 105) and (dath_valley['Min TemperatureF']>70)]
```

### 排序

```python
dath_valley.sort_values(['Mean TemperatureF'])[:5]
```

```python
dath_valley.sort_values(['Mean TemperatureF'])[:-3:-1] # 倒着排序只能用切片了
```

```python
#　多个数据排序
dath_valley.sort_values(['Mean TemperatureF','Min TemperatureF'])[:5]
```

### 简单统计

```python
dath_valley['Mean TemperatureF'].value_counts()
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
dath_valley['is_cool?'] = dath_valley['Mean TemperatureF'].map(is_cool)
dath_valley[['is_cool?','Mean TemperatureF']].head(15)
```

### 对全体应用函数

```python
dath_valley.applymap(lambda x: str(x)+'...').head()
```

### 删除数据

```python
dath_valley = dath_valley.drop(['is_cool?'],axis=1) # 利用drop去掉最后一列
dath_valley.head()
```

```python
# 还好不是彻底改变
dath_valley.head()
```

## 索引

```python
py_score
```

```python
py_score.index = np.arange(10, 17)
py_score.index
```

```python
py_score
```

In this example, you use numpy.arange() to generate a new sequence of row labels that holds the integers from 10 to 16. To learn more about arange(), check out NumPy arange(): [How to Use np.arange()](https://realpython.com/how-to-use-numpy-arange/).


## 绘图


### 线性图

```python
# 在单元里显示
%matplotlib inline
dath_valley.plot()
```

```python
dath_valley['Max TemperatureF'].plot()
```

### 柱状图

```python
dath_valley[['Max TemperatureF','Mean TemperatureF']].plot.bar()
```

```python
# 也可以这样写
dath_valley[['Max TemperatureF','Mean TemperatureF']].plot(kind='bar')
```

### 直方图

```python
# 单独
dath_valley[['Max TemperatureF','Mean TemperatureF']].hist()
```

```python
# 合并
dath_valley[['Max TemperatureF','Mean TemperatureF']].plot.hist()
```

### 密度图

```python
dath_valley[['Max TemperatureF','Mean TemperatureF']].plot.kde()
```

# reference


-   [The Pandas DataFrame: Make Working With Data Delightful](https://realpython.com/pandas-dataframe/)
