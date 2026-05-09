from .base_agent import BaseAgent

class TaskAgent(BaseAgent):
    def generate_task_hint(self, player_memory):
        if not player_memory:
            return "尝试探索周围环境，寻找线索。"
        last_action = player_memory[-1]
        return f"你上次做了 '{last_action}'，可以尝试下一步行动。"
