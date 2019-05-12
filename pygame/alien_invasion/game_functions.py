import sys

import pygame

from bullet import Bullet

def check_keydown_events(event,ai_settings, screen,ship, bullets):
    '''响应按键'''
    # 读取属性event.key, 检查按下的键是否为右箭头( pygame.K_RIGHT)
    if event.key == pygame.K_RIGHT:
        # 修改移动标志,在ship.update()向右移动飞船
        ship.moving_right = True
    elif event.key == pygame.K_LEFT:
        ship.moving_left = True
    elif event.key == pygame.K_SPACE:
        # 新建一颗子弹, 并将其加入到编组bullets 中
        new_bullet = Bullet(ai_settings, screen, ship)
        bullets.add(new_bullet)

def check_keyup_events(event, ship):
    if event.key == pygame.K_RIGHT:
        ship.moving_right = False
    if event.key == pygame.K_LEFT:
        ship.moving_left = False

def check_events(ai_settings, screen, ship, bullets):
    '''响应按键和鼠标事件'''
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()

        elif event.type == pygame.KEYDOWN:
            check_keydown_events(event,ai_settings, screen,ship, bullets)
        elif event.type == pygame.KEYUP:
            check_keyup_events(event, ship)

def update_screen(ai_settings, screen, ship, bullets):
    '''更新屏幕上的图像,并切换到新屏幕'''
    # 每次循环都重新绘制屏幕
    screen.fill(ai_settings.bg_color)  # 这个方法只接受一种实参: 一种颜色
    # 在飞船和外星人后面重绘所有子弹
    for bullet in bullets.sprites():
        bullet.draw_bullet()
    ship.biltme()

    # 让最近的屏幕可见
    pygame.display.flip()