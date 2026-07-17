import sys
from swarm.swarm_orchestrator import create_swarm
from config import MOCK_MODE

def main():
    if len(sys.argv) < 2:
        print("Usage: python main.py \"Your goal here\"")
        return
    
    goal = sys.argv[1]
    print(f"🚀 Starting Super Agent Swarm for: {goal}\n")
    
    swarm = create_swarm()
    result = swarm.process(goal)
    
    print("\n✅ Final Result:")
    print(result)

if __name__ == "__main__":
    main()
