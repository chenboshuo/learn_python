import sys

import pygame

from settings import Setting
from ship import Ship
import game_functions as gf

def run_game():
    # 初始化游戏并创建一个屏幕对象
    pygame.init() # 初始化背景设置,让pygame能正常工作
    ai_settings = Setting()
    screen =  pygame.display.set_mode(
        (ai_settings.screen_width, ai_settings.screen_height)
    ) # 创建(1200, 800)的窗口
    pygame.display.set_caption("Alien Invasion")

    # 创建一艘飞船
    ship = Ship(screen)

    # 开始游戏主循环
    while True:

        # 监视键盘和鼠标事件
        gf.check_events()

        # 每次循环都重新绘制屏幕
        screen.fill(ai_settings.bg_color) # 这个方法只接受一种实参: 一种颜色
        ship.biltme()

        # 让最近的屏幕可见
        pygame.display.flip()

run_game()
