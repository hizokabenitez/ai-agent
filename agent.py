class Agent:
    def __init__(self, name, role):
        self.name = name
        self.role = role

    def display_info(self):
        print(f"Agent Name: {self.name}")
        print(f"Agent Role: {self.role}")

# Example usage
if __name__ == "__main__":
    agent = Agent("Alice", "Developer")
    agent.display_info()
