from swarm.swarm_orchestrator import create_swarm

def run_example():
    swarm = create_swarm()
    result = swarm.process("Create a comprehensive marketing campaign for a new AI productivity tool targeting freelancers")
    print(result)

if __name__ == "__main__":
    run_example()
