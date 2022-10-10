break_line = "\n"
double_break_line = f"{break_line}{break_line}"
separator = ', '

def print_space():
    print("")

def print_bar():
    print("__________________________________________________________________________________")

def print_bar_top():
    print_bar()
    print_space()

def print_bar_bottom():
    print_space()
    print_bar()

def print_title(title):
    print(title)

def print_title_top(title):
    print_title(title)
    print_space()

def print_title_bottom(title):
    print_space()
    print_title(title)

def print_title_both(title):
    print_space()
    print_title(title)
    print_space()

def normal_error(title = "Digite algo válido, por favor"):
    print_title(f"* {title}")

def question(text):
    value = input(text).strip()

    if value != '': return value
    else:
        print_space()
        normal_error()
        print_space()
        return question(text)

def separate_items(items):
    return separator.join(items)

def list_item(title, text):
    print(f"- {title}: {text}")
