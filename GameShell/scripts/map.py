# map.py

class TreeNode:
    def __init__(self, name, parent=None):
        self.name = name
        self.children = []
        self.parent = parent

    def add_child(self, child_node):
        child_node.parent = self
        self.children.append(child_node)

    def display(self, level=0):
        indent = " " * (level * 4)
        print(f"{indent}- {self.name}")
        for child in self.children:
            child.display(level + 1)

    def find_child(self, name):
        for child in self.children:
            if child.name == name:
                return child
        return None

def create_sample_map():
    root = TreeNode("World")

    # Adding continents
    europe = TreeNode("Europe")
    asia = TreeNode("Asia")
    root.add_child(europe)
    root.add_child(asia)

    # Adding countries in Europe
    france = TreeNode("France")
    germany = TreeNode("Germany")
    europe.add_child(france)
    europe.add_child(germany)

    # Adding cities in France
    paris = TreeNode("Paris")
    lyon = TreeNode("Lyon")
    france.add_child(paris)
    france.add_child(lyon)

    # Adding countries in Asia
    china = TreeNode("China")
    india = TreeNode("India")
    asia.add_child(china)
    asia.add_child(india)

    # Adding cities in China
    beijing = TreeNode("Beijing")
    shanghai = TreeNode("Shanghai")
    china.add_child(beijing)
    china.add_child(shanghai)

    return root