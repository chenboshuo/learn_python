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

<center> 数据可视化初步</center>


参考
2. [数据可视化｜详解六种可视化图表（二）Python编程时光](https://mp.weixin.qq.com/s?__biz=MzU4OTUwMDE1Mw==&mid=2247484034&idx=1&sn=0eb885075992a83a0617897bc3933314&chksm=fdcdd914caba5002f2322a77fc520fed4cf0937fe6809ca03518360269f577cd97f93b5a4cc2)


# 简介
axis：可以认为是两个轴，他可以设置轴的大小限制，set_xlim() ，set_ylim() ，还有设置刻度 ticks（由Locator对象定义），还有ticklabel（由Formatter对象定义）等

axes：可以认为是axis的复数，是多个axis组成的。在二维图里，就是两个axis组成，在三D图里，就是三个axis组成。所以你可以粗浅的理解为一个图表就是一个axes，他们可以设置 标题：set_title()，标签：set_xlabel()，set_ylabel()等


## 图片排版

```python
import numpy as np
import matplotlib.pyplot as plt


x = np.linspace(0,10,60)

plt.subplot(2,1,1) # 两行一列的第一个
plt.plot(x,np.sin(x))
plt.ylim(-1,1) # 限定范围,x轴同理

plt.subplot(2,1,2) # 两行一列的第二个
plt.plot(x,np.cos(x),'o',color='red')
```

## 简单绘图

```python
%matplotlib inline
# 上一行表示在jupyter里显示
import numpy as np
import matplotlib.pyplot as plt

# x轴对应值
x = np.linspace(0,5,100)# [1]

# 画图,设置线型和颜色,b为blue,-为线型
plt.plot(x,x**2,'b-')

# 设置x,y轴名字
plt.ylabel('y')
plt.xlabel('x')

# 设置标题
plt.title('Frist Figure')

# 设置栅格
plt.grid(True)

# 设置坐标范围
plt.xlim(0,3)
plt.ylim(0,7)

# 在指定坐标,标注文字
plt.text(1,4,r'y=x^2',fontsize=20)

# 添加图例,注意是个tuple
plt.legend(('Ming',),loc='upper right')

'''
# 设置刻度标签
lables=[x for x in range(10)]
lt.xticks(x.labels)
'''

# 打开刻度Minor tick
plt.minorticks_on()


'''
# 显示图片,notebook中可以忽略
plt.show()
'''
```

# 详解六种可视化图表


## 折线图

```python
import numpy as np
import matplotlib.pyplot as plt

x = np.linspace(0,2,200)

plt.plot(x,x,label='linear')
plt.plot(x,x**2,label='quardratic')
plt.plot(x,x**3,label='cubic')

plt.xlabel('x label')
plt.ylabel('y label')

plt.title('Simple Plot')
# plt.tittle('Simple Plot') 

plt.legend()
# legend 图例

# plt.show()
```

## 散点图
其实散点图和折线图是一样的原理，将散点图里的点用线连接起来就是折线图了。所以绘制散点图，只要设置一下线型即可。

注意：这里我也绘制三条线，和上面不同的是，我只用一个plt.plot就可以了。


### 函数的部分图像

```python
import numpy as np
import matplotlib.pyplot as plt

x = np.arange(0., 5., 0.2)

# 红色破折号,蓝色方块,绿色三角形
plt.plot(x,x,'r--',x,x**2,'bs',x,x**3,'g^')

# plt.show()
```

### 随机数散点图

```python
x = np.random.randn(100)
y = np.random.randn(100)
colors = np.random.rand(100)
sizes = 1000 * np.random.rand(100)
plt.scatter(x, y, c=colors, s=sizes, alpha=0.4)
plt.colorbar() # 显示色彩对应值
```

```python
# 使用样式
plt.style.use('seaborn-whitegrid')

x = np.random.randn(100)
y = np.random.randn(100)
colors = np.random.rand(100)
sizes = 1000 * np.random.rand(100)
plt.scatter(x, y, c=colors, s=sizes, alpha=0.4)
plt.colorbar() # 显示色彩对应值
```

```python
# 使用样式:经典样式
plt.style.use('classic')

x = np.random.randn(100)
y = np.random.randn(100)
colors = np.random.rand(100)
sizes = 1000 * np.random.rand(100)
plt.scatter(x, y, c=colors, s=sizes, alpha=0.4)
plt.colorbar() # 显示色彩对应值
```

## 直方图

```python
import numpy as np
import matplotlib.pyplot as plt
# import mathplotlib.pyplot as plt

np.random.seed(19680801)
# [1]

mu1, sigmal = 100, 15
mu2, sigma2 = 80, 15

mu1, signam1 = 100, 15
mu2, signam2 = 80, 15
x1 = mu1 + signam1 * np.random.randn(10000)
x2 = mu2 + signam2 * np.random.randn(10000)

# the histogram(直方图) of the data
# 50: 将数据分成50组
# facecolor:颜色 alpha:透明度
# density: 密度而不是具体数值
# n:概率值;bins:具体数值; patches:直方图对象

n1, bins1, patches1 = plt.hist(x1, 50, density=True, facecolor='g', alpha=1)
n2, bins2, patches2 = plt.hist(x2, 50, density=True, facecolor='r',alpha=0.2)

plt.xlabel('Smarts')
plt.ylabel('Probablity')
plt.title('Historgram of IQ')

plt.text(110, .025, r'$\mu=100,\ \sigma=15$')
plt.text(50, .025, r'$\mu=80,\ \sigma=15$')

# 设置x,y轴具体范围
plt.axis([40, 160, 0, 0.03])
plt.grid(True)

# plt.show()
```

###  [1]numpy.random.seed的使用
每次设置相同seed,生成随机数也相同

```python
import numpy
help(numpy.random.seed)
```

```python
from numpy.random import rand
import numpy as np

# 不使用seed
a = rand(5)
print('第一次列表:',a)
```

```python
a = rand(5)
print('第二次列表:',a)
```

```python
# 使用seed
np.random.seed(3)
b = rand(5)
print('第一次列表',b)
```

```python
np.random.seed(3)
b = rand(5)
print('第二次列表',b)
```

## 柱状图


### 并列柱状图

```python
import numpy as np
import matplotlib.pyplot as plt
size = 5
a = np.random.random(size)
b = np.random.random(size)
c = np.random.random(size)
x = np.arange(size)

# 有多少个类型,只需修改n即可
total_width, n = 0.8, 3
width = total_width / n 

# 重新拟定x坐标
x = x - (total_width - width) / 2

# 这里使用的偏移
plt.bar(x, a, width=width, label='a') 
plt.bar(x + width, b, width=width, label='b')
plt.bar(x + 2 * width, c, width=width, label='c')
plt.legend()
# plt.show
```

### 叠加柱状图

```python
import numpy as np
import matplotlib.pyplot as plt

size = 5
a = np.random.random(size)
b = np.random.random(size)
c = np.random.random(size)

x = np.arange(size)


# 这里用的偏移
plt.bar(x, a, width=0.5, label='a', fc='r')
plt.bar(x, b, bottom=a, width=0.5, label='b', fc='g')
plt.bar(x, c, bottom=a+b, width=0.5, label='c', fc='b')

plt.ylim(0, 2.5)
plt.legend()
plt.grid(True)
#plt.show()
```

## 饼图


### 普通饼图

```python
import matplotlib.pyplot as plt

labels = 'Frogs','Hogs', 'Dogs', 'Logs'
sizes = [15, 30, 45, 10]

# 设置分离距离,0为不分离
explode = (0, 0.1, 0, 0)

plt.pie(sizes, explode=explode, labels=labels, autopct='%1.1f%%',
       shadow=True, startangle=90)

# Equal aspect ratio 保证画出来是圆形

plt.axis('equal')

# plt.show()
```

### 嵌套饼图

```python
import numpy as np
import matplotlib.pyplot as plt

# 设置每个环的宽度
size = 0.3
vals = np.array([[60., 32.,],[37., 40.], [29., 10.]])

# 通过get_cmap随机获得颜色
cmap = plt.get_cmap('tab20c')
outer_colors = cmap(np.arange(3)*4)
inner_colors = cmap(np.array([1, 2, 5, 6, 9, 10]))

print(vals.sum(axis=1))

plt.pie(vals.sum(axis=1), radius=1, colors=outer_colors,
        wedgeprops=dict(width=size, edgecolor= 'w'))
print(vals.flatten())

'''
plt.pie(vals.fatten(), radius=1-size, colors=inner_colors,
       wedgeprops=dict(width= size, edgecolor='w'))
        'numpy.ndarray' object has no attribute 'fatte
'''

plt.pie(vals.flatten(), radius=1-size, colors=inner_colors,
       wedgeprops=dict(width= size, edgecolor='w'))

# equal 使得为正圆
plt.axis('equal')
# plt.show()
```

### 极轴饼图

```python
import numpy as np
import matplotlib.pyplot as plt

np.random.seed(5)

N = 10
theta = np.linspace(0.0, 2 * np.pi , N, endpoint=False)
radii = 10 * np.random.rand(N)
width = np.pi / 4 * np.random.rand(N)

ax = plt.subplot(111, projection='polar') #[1]
bars = ax.bar(theta, radii ,width=width, bottom =0.0)
# left表示从哪开始
# radii表示半径
# width表示弧长

# 自定义颜色和不透明度
for r,bar in zip(radii, bars):
    bar.set_facecolor(plt.cm.viridis(r / 10))
    bar.set_alpha(0.5)
```

#### [1]plt.subplot

```python
import matplotlib.pyplot as plt
help(plt.subplot)
```

## 三维图 


### 三维散点图

```python
import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

data = np.random.randint(0, 255, size=[40, 40, 40])

x, y, z = data[0], data[1], data[2]
ax = plt.subplot(111, projection='3d') # 创建一个三维绘图工具
# 将数据点分成三部分画,在颜色上有区分度
ax.scatter(x[:10], y[:10], z[:10], c='y') # 绘制数据点
ax.scatter(x[10:20], y[10:20], z[10:20], c='r')
ax.scatter(x[30:40], y[30:40], z[30:40], c='g')

ax.set_zlabel('Z')
ax.set_ylabel('Y')
ax.set_xlabel('X')
```

###  绘制三维平面图

```python
from matplotlib import pyplot as plt
import numpy as np
from mpl_toolkits.mplot3d import Axes3D

fig = plt.figure()
ax = Axes3D(fig)
X = np.arange(-4, 4, 0.25)
Y = np.arange(-4, 4, 0.25)
X, Y = np.meshgrid(X, Y)
R = np.sqrt(X**2 + Y**2)
Z = np.sin(R)
ax.plot_surface(X, Y, Z, rstride=1, cstride=1, cmap='rainbow')
```

# 绘制正弦函数


## 简单绘图

```python
from pylab import *

x = np.linspace(-np.pi, np.pi, 256,endpoint=True)
C, S = np.cos(x), np.sin(x)

plot(x,C)
plot(x, S)

show()
```

## 2.设置基本元素

```python
import numpy as np
from matplotlib import pyplot as plt

plt.figure(figsize=(10,6), dpi=80)
x = np.linspace(-np.pi, np.pi, 256,endpoint=True)
C, S = np.cos(x), np.sin(x)

# 设置线的颜色粗细线型
plt.plot(x, C, color='blue', linewidth=2.5, linestyle='-')
plt.plot(x, S, color='red', linewidth=2.5, linestyle='-')

# 如果觉得线离边界太近,可以加大距离
plt.xlim(x.min()*1.2, x.max()*1.2)
plt.ylim(C.min()*1.2, C.max()*1.2)

# 当前刻度并不清晰,需要重新设定,加上更直观的标签
plt.xticks([-np.pi ,-np.pi/2, 0, np.pi/2 ,np.pi],
           [r'$-\pi$', r'$-\pi/2$', r'$0$' , r'$\pi/2$', r'$\pi$'])
plt.yticks([-1, 0, 1],
          [r'$-1$' , r'$0$', r'$1$'])

```

## 3.移动轴线

```python
import numpy as np
from matplotlib import pyplot as plt

plt.figure(figsize=(10,6), dpi=80)
x = np.linspace(-np.pi, np.pi, 256,endpoint=True)
C, S = np.cos(x), np.sin(x)
plt.plot(x, C, color='blue', linewidth=2.5, linestyle='-')
plt.plot(x, S, color='red', linewidth=2.5, linestyle='-')
plt.xlim(x.min()*1.2, x.max()*1.2)
plt.ylim(C.min()*1.2, C.max()*1.2)
plt.xticks([-np.pi ,-np.pi/2, 0, np.pi/2 ,np.pi],
           [r'$-\pi$', r'$-\pi/2$', r'$0$' , r'$\pi/2$', r'$\pi$'])
plt.yticks([-1, 0, 1],
          [r'$-1$' , r'$0$', r'$1$'])

# plt.gca(),全称 get current axis
ax.plt.gca()
ax.spines
```
