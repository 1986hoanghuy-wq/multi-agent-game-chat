from .base_agent import BaseAgent
import random

class DialogueAgent(BaseAgent):
    def respond(self, player_input, context):
        self.remember(player_input)
        responses = [
            f"{self.name}: 我注意到你提到了 '{player_input}'，你想了解更多吗？",
            f"{self.name}: 有趣，你的选择会影响接下来的剧情。",
            f"{self.name}: 我可以给你一些建议，或者你想自己探索？"
        ]
        return random.choice(responses)
