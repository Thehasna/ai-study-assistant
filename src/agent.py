from tools.calculator import calculate

class Agent:
    def process(self, user_input):
        if "calculate" in user_input:
            expression = user_input.replace("calculate", "").strip()
            result = calculate(expression)
            return f"Result: {result}"
        else:
            return "I don't understand the request."