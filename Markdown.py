def print_help():
    print("Available formatters: plain bold italic header link inline-code ordered-list unordered-list new-line")
    print("Special commands: !help !done")

def get_text():
    return input("Text: ")

def formatter_plain():
    return get_text()

def formatter_bold():
    return f"**{get_text()}**"

def formatter_italic():
    return f"*{get_text()}*"

def formatter_inline_code():
    return f"`{get_text()}`"

def formatter_link():
    label = input("Label: ")
    url = input("URL: ")
    return f"[{label}]({url})"

def formatter_header():
    level = int(input("Level: "))
    if 1 <= level <= 6:
        text = input("Text: ")
        return f"{'#' * level} {text}\n"
    else:
        print("The level should be within the range of 1 to 6")
        return ""

def formatter_new_line():
    return "\n"

def formatter_list(ordered):
    try:
        rows = int(input("Number of rows: "))
        if rows <= 0:
            print("The number of rows should be greater than zero")
            return ""
        result = ""
        for i in range(1, rows + 1):
            row_text = input(f"Row #{i}: ")
            prefix = f"{i}. " if ordered else "* "
            result += f"{prefix}{row_text}\n"
        return result
    except ValueError:
        print("Invalid input. Expected a number.")
        return ""

FORMATTERS = {
    "plain": formatter_plain,
    "bold": formatter_bold,
    "italic": formatter_italic,
    "inline-code": formatter_inline_code,
    "link": formatter_link,
    "header": formatter_header,
    "new-line": formatter_new_line,
    "ordered-list": lambda: formatter_list(ordered=True),
    "unordered-list": lambda: formatter_list(ordered=False),
}

def main():
    result = ""
    while True:
        user_input = input("Choose a formatter: ")
        if user_input == "!help":
            print_help()
        elif user_input == "!done":
            with open("output.md", "w", encoding="utf-8") as f:
                f.write(result)
            break
        elif user_input in FORMATTERS:
            formatted = FORMATTERS[user_input]()
            result += formatted
            print(result)
        else:
            print("Unknown formatting type or command")

if __name__ == "__main__":
    main()
