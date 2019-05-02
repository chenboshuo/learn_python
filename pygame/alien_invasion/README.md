# 项目1 外星人入侵
> 项目来自 `python编程从入门到实践` 12,13,14章

-   [所有版本](https://github.com/chenboshuo/python_learning/commits/35e660d951a3bee63744930a4bb24a95e70f8c4e/pygame/alien_invasion/alien_invason.py)

# 12章 武装飞船
## 12.3 开始游戏项目
### 12.3.1 创建pygame窗口以及响应用户输入
-   [code](https://github.com/chenboshuo/python_learning/commit/09c56a1399cc1c891aa743c0e0fbba9365a6eff8)

模块`sys` 用来退出游戏
```py
pygame.init()
```
初始化背景和设置, 让游戏正常工作.
```py
screen =  pygame.display.set_mode((1200, 800))
```
在这里创建了名为`screen`的显示窗口,让游戏的所有元素在其中绘制
对象`screen`是个`surface`, 在pygame中,`surface`是屏幕的一部分,用于显示游戏元素.`display.set_model((1200, 800))`返回的surface表示游戏窗口. 我们激活这个循环之后, 每一次循环都自动重绘这个`surface`

### 12.3.2 设置背景色
-   [code](https://github.com/chenboshuo/python_learning/commit/67e4a7304131e48c0551e5abc45b8b013c1d95b7)

```py
bg_color = (230, 230, 230)
```

在pygame中,颜色是RGB组成的元组

在`screen.fill()`用背景色填充屏幕; 这个方法接受一个实参: 一种颜色.

### 12.3.3 创建设置类
-   [code](https://github.com/chenboshuo/python_learning/commit/35e660d951a3bee63744930a4bb24a95e70f8c4e)

每次给游戏添加新功能时, 通常要应用一些新的设置.模块setting包含一个Setting类将所有设置存储在同一个地方,以免在代码中到处添加设置. 这样, 我们只需要传递一个设置对象. 另外, 这让函数调用更简单,在项目增大时修改外观更容易: 修改游戏只需要修改setting中的一些值,而无需查找分布在项目中的各种设置.

## 12.4 添加飞船图像

在游戏中几乎可以加载任何类型的图片文件,但使用位图(`.bmp`)最简单, 因为pygame默认加载位图.

### 12.4.1 创建ship类

-   [code](https://github.com/chenboshuo/python_learning/commit/1d1939ec17263c5f8c6d4e0924e52389fb762826#diff-9cc57e6c320f1d54eea8690342da30a7)

我们将创建一个ship的模块, 其中包含ship类,它负责飞船大部分行为.

```py
 self.imag = pygame.image.load('images/ship.bmp')
```
函数返回一个表示飞船外形的surface

```py
self.rect = self.imag.get_rect()
```
获取对象的属性rect,可以让你像处理矩形一样处理游戏元素, 提高效率.

处理rect对象时, 可以使用矩形四角和中心的x和y坐标,通过设置这些值来指定矩形的位置.

要想让游戏元素居中, 可以设置rect对象属性center,centerx, centery. 要想让游戏元素与边缘对齐,可以使用属性top, bottom, left, right; 要调整游戏元素水平或垂直位置,可以使用属性x,y,他们分别是矩形左上角的坐标值

#### 12.4.2 在屏幕上绘制飞船

通过调用方法blitme

## 12.5 重构: 模块game_functions
创建game_function 模块,存储使游戏运行的函数,防止alien_events 过长

### 12.5.1 函数 check_events()

-   [代码](https://github.com/chenboshuo/python_learning/commit/8e2aa07a52795311efa93d78a8ac74d6d1c4fc33)
函数check_events() 不需要任何形参, 其函数体复制了 alien_invasion 事件循环的

主程序中不需要导入sys, 因为当前只在game_funxtions 使用了它.
### 12.5.2 函数update_screen()
-   [代码]()
为了进一步简化代码, 将更新屏幕的代码移到名为update_screen()的函数中

两个函数让while变得简单, 让后续开发更容易: 在game_function 而不是run_game()中完成大部分工作.

我们一开始只想用一个文件, 因此没有引入模块game_function. 开发过程中, 一开始将代码写的尽可能简单, 并在项目越来越复杂是进行重构
