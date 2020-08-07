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

# 数据建模

```python
from sklearn import  datasets

# 导入 线型回归方法
from sklearn.linear_model import LinearRegression

# 导入数据
loaded_data = datasets.load_boston()

# 获取数据输入与输出,sklearn规则的把数据分为data(输入)与target(输出)
data_X = loaded_data.data
data_Y = loaded_data.target

model = LinearRegression()
model.fit(data_X, data_Y)

# print(model.pedict(data_X[:4,:]))
print(model.predict(data_X[:4,:]))
print(model.score(data_X, data_Y))

print(model.coef_)
print('============')
print(model.intercept_)


```

```python
import sklearn
help(sklearn)
```

```python

```
