import sys

import pygame

def check_events(ship):
    '''响应按键和鼠标事件'''
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()

        elif event.type == pygame.KEYDOWN:
            # 读取属性event.key, 检查按下的键是否为右箭头( pygame.K_RIGHT)
            if event.key == pygame.K_RIGHT:
                # 修改移动标志,在ship.update()向右移动飞船
                ship.moving_right = True

        elif event.type == pygame.KEYUP:
            if event.key == pygame.K_RIGHT:
                ship.moving_right = False

def update_screen(ai_settings, screen, ship):
    '''更新屏幕上的图像,并切换到新屏幕'''
    # 每次循环都重新绘制屏幕
    screen.fill(ai_settings.bg_color)  # 这个方法只接受一种实参: 一种颜色
    ship.biltme()

    # 让最近的屏幕可见
    pygame.display.flip()