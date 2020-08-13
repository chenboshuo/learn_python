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
    display_name: 'Python 3.7.4 64-bit (''base'': conda)'
    language: python
    name: python37464bitbaseconda3cf756b78fb64f58b9cac533c82461ea
---

# Hypothesis Testing


## Kolmogorov–Smirnov test

```python
from scipy import stats
import numpy as np
np.random.seed(12345678)
x = stats.norm.rvs(loc=0, scale=1, size=300)
stats.kstest(x,'norm')
```

K-S 检验原假设为数据符合正态分布，
运行结果的第一个返回值是统计量，
第二个值为p-value,
其中$p-value > 0.05$ 说明不能拒绝原假设,
需要注意的是,
K-S 检验只能检验标准正态分布(也称U分布),
即期望值$\mu=0$,
标准差$\sigma=1$


## Shapiro-Wilk test

```python
from scipy import stats
import numpy as np

np.random.seed(12345678)
x = stats.norm.rvs(loc=10, scale=2, size=70)
stats.shapiro(x)
```

Shapiro-Wilk 检验的是数据符合正态分布，
运行结果的第一个返回值是统计量，
第二个值为p-value,
其中$p-value > 0.05$ 说明不能拒绝原假设。
