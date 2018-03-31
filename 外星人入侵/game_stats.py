import string

class GameStats():

    """跟踪游戏的统计信息"""

    def __init__(self,ai_settings):
        with open("high_score.txt") as file_object:
            self.contents = file_object.read()
            self.high_score = int(self.contents)
        """初始化统计信息"""
        self.ai_settings = ai_settings
        self.reset_stats()
        #游戏一开始时处于非活动状态
        self.game_active = False




    def reset_stats(self):
        """初始化在游戏运行期间可能变化的统计信息"""
        self.ship_left = self.ai_settings.ship_limit
        self.score = 0
        self.level = 1

