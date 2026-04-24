from agent import Agent

agent = Agent()

while True:
    user_input = input("Enter your request (or type 'exit'): ")

    if user_input.lower() == "exit":
        break

    response = agent.process(user_input)
    print(response)