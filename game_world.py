from agents.dialogue_agent import DialogueAgent
from agents.task_agent import TaskAgent

class GameWorld:
    def __init__(self):
        self.dialogue_agents = [DialogueAgent("NPC1"), DialogueAgent("NPC2")]
        self.task_agent = TaskAgent("TaskMaster")

    def player_interaction(self, player_input):
        dialogue_responses = [agent.respond(player_input, None) for agent in self.dialogue_agents]
        task_hint = self.task_agent.generate_task_hint([player_input])
        return dialogue_responses, task_hint
