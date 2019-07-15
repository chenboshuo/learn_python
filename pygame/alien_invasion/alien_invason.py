
import pygame
from pygame.sprite import Group

from settings import Setting
from game_stats import GameStats
from ship import Ship
from alien import Alien
import game_functions as gf

def run_game():
    # 初始化游戏并创建一个屏幕对象
    pygame.init() # 初始化背景设置,让pygame能正常工作
    ai_settings = Setting()
    screen =  pygame.display.set_mode(
        (ai_settings.screen_width, ai_settings.screen_height)
    ) # 创建(1200, 800)的窗口
    pygame.display.set_caption("Alien Invasion")

    # 创建一个用于存储游戏统计信息的实例
    stats = GameStats(ai_settings)

    # 创建一艘飞船,一个子弹编组和一个外星人编组
    ship = Ship(ai_settings, screen)
    bullets = Group()
    aliens = Group()

    # 创建外星人群
    gf.create_fleet(ai_settings, screen, ship, aliens)

    # 创建一个外星人
    alien = Alien(ai_settings, screen)

    # 开始游戏主循环
    while True:
        gf.check_events(ai_settings, screen, ship, bullets) # 监视键盘和鼠标事件
        ship.update()
        gf.update_bullets(ai_settings, screen, ship, aliens, bullets)
        gf.update_aliens(ai_settings, stats, screen, ship, aliens, bullets)
        gf.update_screen(ai_settings, screen, ship, aliens, bullets)

run_game()
