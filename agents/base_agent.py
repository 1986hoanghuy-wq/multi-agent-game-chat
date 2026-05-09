class BaseAgent:
    def __init__(self, name):
        self.name = name
        self.memory = []

    def remember(self, info):
        """存储对话历史或玩家行为"""
        self.memory.append(info)

    def respond(self, player_input, context):
        """子类实现具体生成逻辑"""
        raise NotImplementedError
