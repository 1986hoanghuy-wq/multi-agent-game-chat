from game_world import GameWorld

def main():
    world = GameWorld()
    print("欢迎来到多 Agent 游戏聊天模拟！输入 'exit' 结束。")
    
    while True:
        player_input = input("玩家: ")
        if player_input.lower() == "exit":
            break
        dialogue_responses, task_hint = world.player_interaction(player_input)
        for resp in dialogue_responses:
            print(resp)
        print(f"任务提示: {task_hint}")

if __name__ == "__main__":
    main()
