def read_file(path):
    try:
        with open(path, "r") as file:
            return file.read()
    except:
        return "Error reading file"