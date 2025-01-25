class Agent:
    agents = []

    def __init__(self, name, role):
        self.name = name
        self.role = role
        Agent.agents.append(self)

    def display_info(self):
        print(f"Agent Name: {self.name}")
        print(f"Agent Role: {self.role}")

    @classmethod
    def create_agent(cls, name, role):
        return cls(name, role)

    @classmethod
    def list_agents(cls):
        for agent in cls.agents:
            agent.display_info()

# Example usage
if __name__ == "__main__":
    agent1 = Agent.create_agent("Alice", "Developer")
    agent2 = Agent.create_agent("Bob", "Designer")
    Agent.list_agents()
