# navigation.py
def find_node_by_path(current_node, path):
    parts = path.split('/')
    node = current_node
    for part in parts:
        if part == "..":
            if node.parent:
                node = node.parent
            else:
                print("Error: Already at the root.")
                return None
        else:
            next_node = node.find_child(part)
            if next_node:
                node = next_node
            else:
                print(f"Error: '{part}' not found.")
                return None
    return node