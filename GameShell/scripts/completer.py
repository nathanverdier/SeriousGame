# completer.py
def completer(text, state, current_node):
    options = [i.name for i in current_node.children if i.name.startswith(text)]
    if state < len(options):
        return options[state]
    else:
        return None