def read_text_file(path):
    with open(path, "r", encoding="utf-8") as file:
        content = file.read()
    return content
