class Setting():
    '''存储游戏所有设置的类'''

    def __init__(self):
        '''初始化游戏设置'''
        # 屏幕设置
        self.screen_width = 900
        self.screen_height = 600
        self.bg_color = (230, 230, 230)

        # 子弹设置
        self.bullet_speed_factor = 1
        self.bullet_width = 3
        self.bullet_height = 15
        self.bullet_color = 60, 60, 60 # 深灰色子弹
        self.bullets_allowed = 3

        # 飞船设置
        self.ship_speed_factor = 1.5

        # 外星人设置
        self.alien_speed_factor = 1