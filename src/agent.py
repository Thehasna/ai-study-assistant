from tools.calculator import calculate
from tools.file_reader import read_file
from tools.search import search_knowledge

class Agent:
    def process(self, user_input):
        if "calculate" in user_input:
            expression = user_input.replace("calculate", "")
            return f"Result: {calculate(expression)}"

        elif "read file" in user_input:
            return read_file("data/knowledge.txt")

        elif "search" in user_input:
            query = user_input.replace("search", "").strip()
            return search_knowledge(query)

        else:
            return "I don't understand the request"