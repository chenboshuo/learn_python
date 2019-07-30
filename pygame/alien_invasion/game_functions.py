import sys
from time import sleep

import pygame

from bullet import Bullet
from alien import Alien

def check_keydown_events(event,ai_settings, screen,ship, bullets):
    '''响应按键'''
    # 读取属性event.key, 检查按下的键是否为右箭头( pygame.K_RIGHT)
    if event.key == pygame.K_RIGHT:
        # 修改移动标志,在ship.update()向右移动飞船
        ship.moving_right = True
    elif event.key == pygame.K_LEFT:
        ship.moving_left = True
    elif event.key == pygame.K_SPACE:
        fire_bullet(ai_settings, screen, ship, bullets)

def fire_bullet(ai_settings, screen, ship, bullets):
    '''如果没有达到限制, 就发射一颗子弹'''
    if len(bullets) < ai_settings.bullets_allowed:
        # 新建一颗子弹, 并将其加入到编组bullets 中
        new_bullet = Bullet(ai_settings, screen, ship)
        bullets.add(new_bullet)


def check_keyup_events(event, ship):
    if event.key == pygame.K_RIGHT:
        ship.moving_right = False
    if event.key == pygame.K_LEFT:
        ship.moving_left = False
    elif event.key == pygame.K_w and  pygame.key.get_mods() & pygame.KMOD_CTRL : # and 前后交换次序好像不可以,
        # reference:　https://stackoverflow.com/questions/24923078/python-keydown-combinations-ctrl-key-or-shift-key
        sys.exit()

def check_events(ai_settings, screen, ship, bullets):
    '''响应按键和鼠标事件'''
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
        elif event.type == pygame.KEYDOWN:
            check_keydown_events(event,ai_settings, screen,ship, bullets)
        elif event.type == pygame.KEYUP:
            check_keyup_events(event, ship)

def update_screen(ai_settings, screen, ship, aliens, bullets):
    '''更新屏幕上的图像,并切换到新屏幕'''
    # 每次循环都重新绘制屏幕
    screen.fill(ai_settings.bg_color)  # 这个方法只接受一种实参: 一种颜色
    # 在飞船和外星人后面重绘所有子弹
    for bullet in bullets.sprites():
        bullet.draw_bullet()
    ship.blitme()
    aliens.draw(screen)

    # 让最近的屏幕可见
    pygame.display.flip()

def update_bullets(ai_settings, screen, ship, aliens, bullets):
    '''更新子弹位置, 删除已经消失的子弹    '''
    # 更新子弹位置
    bullets.update()

    # 删除已消失的子弹(不应从列表或编组中删除条目)
    for bullet in bullets.copy():
        if bullet.rect.bottom <= 0:
            bullets.remove(bullet)
            # print(len(bullets))

    check_bullet_alien_collisions(ai_settings, screen, ship, aliens, bullets)

def check_bullet_alien_collisions(ai_settings, screen, ship, aliens, bullets):
    '''响应子弹和外星人碰撞'''
    # 检查是否有子弹击中了外星人
    # 如果这样, 就删除子弹和外星人
    collisions = pygame.sprite.groupcollide(bullets, aliens, True, True)
    # 新增的这行代码遍历编组bullets中的每颗子弹,再遍历编组aliens中的每个外星人.
    # 每当有子弹和外星人的rect重叠时, groupcollide()就在它返回的字典中添加一个键-值对.
    # 两个实参True告诉pygame要删除发生碰撞的子弹和外星人.
    # (要模拟能穿行到屏幕顶端的高能子弹--消灭它击中的每一个外星人,可将第一个布尔参数设为False.
    #  这样被他击中的外星人将消失,所有子弹始终有效, 直到抵达屏幕顶端后消失.)

    if len(aliens) == 0:
        # 删除现有子弹并创建一群新的外星人
        bullets.empty()
        create_fleet(ai_settings, screen, ship, aliens)

def get_number_aliens_x(ai_settings, alien_width):
    '''计算每一行可以容纳多少外星人'''
    available_space_x = ai_settings.screen_width - 2 * alien_width
    number_aliens_x = int(available_space_x / (2 * alien_width))
    return number_aliens_x

def get_number_rows(ai_settings, ship_height, alien_height):
    '''计算屏幕可以容纳多少行外星人'''
    available_space_y = ai_settings.screen_height - (3 * alien_height) - ship_height
    number_rows = int(available_space_y / (2 * alien_height))
    return number_rows

def create_alien(ai_settings, screen, aliens, alien_number, row_number):
    '''创建一个外星人并加入当前行'''
    alien = Alien(ai_settings, screen)
    alien_width = alien.rect.width
    alien.x = alien_width + 2 * alien_width * alien_number
    alien.rect.x = alien.x
    alien.rect.y = alien.rect.height + 2 * alien.rect.height * row_number
    aliens.add(alien)

def create_fleet(ai_settings, screen, ship, aliens):
    '''创建外星人群'''
    # 创建一个外星人, 并计算可以容纳多少外星人
    # 外星人间距为外星人宽度
    alien = Alien(ai_settings, screen)
    number_aliens_x = get_number_aliens_x(ai_settings, alien.rect.width)
    number_rows = get_number_rows(ai_settings, ship.rect.height, alien.rect.height)

    # 创建外星人群
    for row_number in range(number_rows):
        for alien_number in range(number_aliens_x):
            create_alien(ai_settings, screen, aliens, alien_number, row_number)

def ship_hit(ai_settings, stats, screen, ship, aliens, bullets):
    '''响应被外星人撞到的飞船'''
    if stats.ships_left > 0:
        # 将ship_left减1
        stats.ships_left -= 1

        # 清空外星人和子弹列表
        aliens.empty()
        bullets.empty()

        # 创建一群新的外星人, 并将飞船放到底端中央
        create_fleet(ai_settings, screen, ship, aliens)
        ship.center_ship()

        # 暂停
        sleep(0.5)
    else:
        stats.game_active = False


def check_aliens_bottom(ai_settings, stats, screen, ship, aliens, bullets):
    '''检查是不是有外星人到达屏幕底端'''
    screen_rect = screen.get_rect()
    for alien in aliens.sprites():
        if alien.rect.bottom >= screen_rect.bottom:
            # 像飞船被撞到一样处理
            ship_hit(ai_settings, stats, screen, ship, aliens, bullets)
            break

def update_aliens(ai_settings, stats, screen, ship, aliens, bullets):
    '''
    检查外星人是否位于屏幕边缘, 并更新外星人位置
    '''
    check_fleet_edges(ai_settings, aliens)
    aliens.update()

    # 检测外星人和飞船之间的碰撞
    if pygame.sprite.spritecollideany(ship, aliens):
        '''
        方法spritecollideany()接受两个实参:一个精灵和一个编组.
        它检查精灵和编组是否发生碰撞, 找到与精灵发生了碰撞的成员后停止遍历编组.
        在这里, 它遍历编组aliens, 返回它找到的第一个与飞船发生碰撞的外星人.
        '''
        ship_hit(ai_settings, stats, screen, ship, aliens, bullets)

    # 检查外星人是否到达屏幕底端
    check_aliens_bottom(ai_settings, stats, screen, ship, aliens, bullets)

def check_fleet_edges(ai_settings, aliens):
    '''有外星人到达边缘时采取的相应的措施'''
    for alien in aliens.sprites():
        if alien.check_ages():
            change_fleet_direction(ai_settings, aliens)
            break

def change_fleet_direction(ai_settings, aliens):
    '''将整群外星人下移,并改变他们的方向'''
    for alien in aliens.sprites():
        alien.rect.y += ai_settings.fleet_drop_speed
    ai_settings.fleet_direction *= -1

