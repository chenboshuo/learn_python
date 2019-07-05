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
-   [代码](https://github.com/chenboshuo/python_learning/commit/331d036ccff850e8cc697ff3ac4d834dc607b55e)
为了进一步简化代码, 将更新屏幕的代码移到名为update_screen()的函数中

两个函数让while变得简单, 让后续开发更容易: 在game_function 而不是run_game()中完成大部分工作.

我们一开始只想用一个文件, 因此没有引入模块game_function. 开发过程中, 一开始将代码写的尽可能简单, 并在项目越来越复杂是进行重构

## 12.6 驾驶飞船
下面让玩家可以左右移动飞船.
首先应专注于向右移动, 再使用同样的原理向左移动

### 12.6.1 响应按键

每当用户按键时,都将在pygame注册一个事件. 事件都是通过方法`pygame.event.get()`获取的, 因此在`check_events()`中, 我们需要检查哪些类型的事件. 每次按键都被注册为`KEYDOWN`事件.

检测到`KEYDOWN`事件时, 我们检查按下的是否是特定的键. 例如, 如果按下的是右箭头, 我们就增大`rect.centerx`的值, 让飞船右移:

-   [代码](https://github.com/chenboshuo/python_learning/commit/a1d1b9cda748f8a41d9f11a9c03f0512250bf0a8)

函数 `check_events()` 包含形参`ship`, 因为需要对飞船进行操作

### 12.6.2 允许不断移动

玩家按住右箭头不放时, 我们希望飞船不断向右移动, 直到玩家松开为止.我们让游戏检测`pygame.KEYUP`事件, 以便玩家松开右箭头我们能够知道这一点; 然后, 我们结合使用`KEYDOWN`和`KEYUP`事件,以及一个`moving_right`的标志来实现持续移动.

飞船的属性由Ship类操控, 因此我们给这个类添加一个名为moving_right的属性和一个名为update()的方法. 方法update()检查标志moving_right的状态, 如果标志为True,就调整位置:
-   [代码](https://github.com/chenboshuo/python_learning/commit/40d5199c4bbe2b2416f783988e9aedae69c8cb44)

玩家按下右箭头之后不直接调整位置, 而是修改标志

修改`alien_invasion.py`中while循环以便玩家输入后, 飞船位置将更新

### 12.6.3 左右移动
和向右运动同理
-   [代码](https://github.com/chenboshuo/python_learning/commit/74d6926c49c6178d47c4aeff280007615994840c)

### 12.6.4 调整飞船速度
当前, 执行while循环时, 飞船最多移动1像素, 但我们可以添加设置控制移动距离:
-   [代码](https://github.com/chenboshuo/python_learning/commit/8377c7be2f4692b9fecd90db30c080cc68a59f2c)

我们设置ship_speed_factor 的值为1.5, 可以加快游戏节奏, 然而, rect的`centerx`等属性只能存储整数值, 因此还要进行修改,(创建一个ship.center存储 float 的中间变量再取整)

同时在ship的`__init__()`的形参列表添加了`ai_settings`让飞船可以快速读取设置

### 12.6.5 限制飞船的移动范围
当前, 如果玩家按住箭头的时间足够长, 飞船将飞到屏幕外边, 下面来修复这个问题:

-[代码](https://github.com/chenboshuo/python_learning/commit/b14b5661653868a6139e34e15e8a3e3d25bab423)

上述代码在修改self.center的值之前检查飞船位置. `self.rect.right`返回飞船外接矩形右边缘的坐标, 如果这个值小于self.screen_rect.right的值, 说明未触及右边缘, 左边缘同理

### 12.6.6 重构check_events()

随着游戏开发的进行, check_events()将越来越长, 我们将部分代码放在两个函数中, 一个处理KEYDOWN,另一个处理KEYUP:

-   [代码](https://github.com/chenboshuo/python_learning/commit/2eeecf7ab0e6d674c13c9db5e45e971f2570ddeb)

创建两个函数, 都包含形参event和ship, 这两个代码是从check_events()中复制过来的, 因此可以代替这些代码

> 12.7 是回顾部分, 略

## 12.8 射击

### 12.8.1 添加子弹设置
更新`settings.py`在__init__()末尾存储设置

### 12.8.2 创建`Bullet`类

通过使用精灵, 可以将游戏中相关的元素编组, 进而同时操作编组中的所有元素.

### 12.8.3 将子弹存到编组中

我们在`alien_invason.py`中创建一个编组(Group), 用于存储所有有效子弹, 以便能够管理发射出去的所有子弹. 这个编组是pygame.sprite.Group 类的实例; pygame.sprite.Group 类似于列表, 但提供了有助于游戏开发的额外功能. 在主循环中, 我们将使用这个编组在屏幕上绘制子弹, 以更新每颗子弹的位置

### 12.8.4 开火
修改`check_keydown_events()` 以便玩家按空格的时候发射一颗子弹, 无需修改`check_keyup_events()`因为玩家松开空格的时候什么都不会发生. 我们还要修改update_screen(), 确保在调用flip()的时候重绘每颗子弹

-   [1-4 的代码](https://github.com/chenboshuo/python_learning/commit/e8617ef84edb19adb684047e3b191ec4fb02a171)

### 12.8.5 删除已消失的子弹
当前, 子弹到达屏幕顶端之后消失, 仅仅因为pygame无法在屏幕之外绘制他们, 这些子弹其实一直存在, 他们的y为负数, 且越来越小, 他们将继续消耗内存和处理能力

如果代码没问题, 将print语句删除. 如果留下这条语句, 游戏的速度大大降低, 因为输出写入终端而花费的事件比图形绘制到游戏窗口的时间还多.

-   [相关代码](https://github.com/chenboshuo/python_learning/commit/538fc6356b159606eaca2eb88844fed10a9b186b)

### 12.8.6 限制子弹数量
很多射击游戏都限制同时出现的子弹数量, 来鼓励玩家有目标的射击.

首先在`setting.py`中存储允许的最大子弹数

在`game_functions.py`的`check_keydown_events()`中, 创建子弹前检查未消失的子弹是否小于该设置

-   [相关修改](https://github.com/chenboshuo/python_learning/commit/09e23a53d5d72a00f81cb91b1fb94a40ea426a81)

### 12.8.7 创建函数 update_bullets()

编写并管理代码后, 可以将其移到`game_functions`中, 以让主程序尽可能简单. 我们创建一个`update_bullets()`的新函数,将他添加到`game_functions.py`的末尾.

我们让主循环包含尽可能少的代码, 这样只需要看函数名就迅速知道游戏中发生的情况.

-   [相关修改](https://github.com/chenboshuo/python_learning/commit/daca8676c19e77453d7424282ab2076a500e7d21)

### 12.8.8 创建函数 fire_bullet()

下面将发射子弹的代码移到一个独立的函数中, 这样, `check_keydown_events` 只需要一行代码发射子弹, 让`elif`代码块变得简洁

函数`fire_bullet()`只包含玩家按空格时用于发射子弹的代码; 在`check_keydown_events()`中, 玩家按空格的时候调用`fire_bullet()`

-   [相关修改](https://github.com/chenboshuo/python_learning/commit/32fc2546765139c44513f15cc5e0abbb495e7a6a)

# 13 外星人
## 13.1 设置快速退出快捷键
-   [相关修改](https://github.com/chenboshuo/python_learning/commit/22eb4fd5549b5b74a9448803c819fa7226202766)
## 13.2 创建第一个外星人
-   [相关修改](https://github.com/chenboshuo/python_learning/commit/dd2e550dcea0ffb24aabf664384c76352521432c)
### 31.2.1 创建Alien类
除了位置不同之外, 大多数代码与ship类似. 每个外星人都在屏幕左上角附近, 我们将每个外星人左边距设为外星人的宽度,并将上边距设为外星人的高度.
### 12.2.3 让外星人出现在屏幕上
利用update_screen 调用方法 blitme

## 13.3 创建一群外星人
### 13.3.1 确定一行可容纳多少外星人

可以用于放置外星人的水平空间设为屏幕宽度减去外星人宽度的两倍:
```py
avaiable_space_x = as_settings.screen_width - (2*alien_width)
```
我们还要在外星人之间留出一定空间, 即外星人的宽度. 因此, 显示一个外星人所需要的水平空间为外星人宽度的两倍.
```py
number_alien_x = available_space_x / (2*alien_width)
```

### 13.3.2 创建多行外星人
```py
aliens.draw(screen)
```
对编组调用draw()时, pygame会自动绘制编组的每一个元素, 绘制位置由元素属性rect决定.

### 13.3.3 创建外星人群
-   [修改](https://github.com/chenboshuo/python_learning/commit/7253965ad2c1d88f96dee618e9608d753e604541)

### 13.3.4 重构create_fleet()
-   [我们清理一下creat_fleet()](https://github.com/chenboshuo/python_learning/commit/036b901f6fcee08b88313fe5daf7f9efed1febaf)

### 13.3.5 添加行
垂直空间可以这样计算, 将屏幕高度减去第一行外星人的上边距(外星人高度), 飞船高度加上外星人边距(外星人高度的两倍):
```py
available_space_y = ai_settings.screenheight - 3 * alien_height - ship_height.
```
这将在飞船上方留出一定空白区域,给玩家留出射杀外星人的时间.
-   [相关修改](https://github.com/chenboshuo/python_learning/commit/1536124c4adbbc81987ee267aea980bb6a24f888)

## 13.4 让外星人群移动
下面让外星人在屏幕上向右移动, 撞到屏幕边缘之后下移一定距离, 再沿相反的方向移动. 我们将不断移动外星人, 直到所有外星人都被消灭,有外星人装上飞船, 或者有外星人到达屏幕底端.

### 13.4.1 向右移动外星人
-   [相关修改](https://github.com/chenboshuo/python_learning/commit/e87a3d9ebfec4dc15c959d7dc422adc271f6db78)

### 13.4.2 创建表示外星人移动方向的设置
下面创建外星人撞到屏幕右边缘后向下移动, 再向左移动的设置. 实现该功能的代码如下:
```py
self.alien_speed_factor = 1
self.fleet_drop_speed = 10
self.fleet_direction = 1 # 1表示右移, -1表示左移
```
因为`leet_direction`只有两个方向, 可以用1,-1表示,并在外星人改变方向时切换.

### 13.4.3 检查外星人是否撞到了屏幕边缘
### 13.4.4 向下移动外星人并改变移动方向
  -[相关修改](https://github.com/chenboshuo/python_learning/commit/f41bb684875b8d61adff3d070f57e71cf374a46d)
