
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
        gf.check_events(ship) # 监视键盘和鼠标事件
        ship.update()
        gf.update_screen(ai_settings, screen, ship)

run_game()
