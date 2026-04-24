def search_knowledge(query):
    try:
        with open("data/knowledge.txt", "r") as file:
            lines = file.readlines()

        results = []
        for line in lines:
            if query.lower() in line.lower():
                results.append(line)

        if results:
            return "".join(results)
        else:
            return "No results found"

    except:
        return "Search error"