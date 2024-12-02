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
    europe = TreeNode("Eupi")
    asia = TreeNode("Asia")
    root.add_child(europe)
    root.add_child(asia)

    # Adding countries in Europe
    france = TreeNode("IA")
    germany = TreeNode("Developpement")
    germany = TreeNode("Cybersecurite") 
    germany = TreeNode("Algorithme") 
    germany = TreeNode("Test_Validation") 
    europe.add_child(france)
    europe.add_child(germany)

    # Adding cities in France
    sphere = TreeNode("Sphere_securite")
    quaranaine = TreeNode("Zone_quarantaine")
    lyon = TreeNode("Temple_données_corrompues")
    cyber.add_child(paris)
    cyber.add_child(lyon)

    # Adding countries in Asia
    china = TreeNode("Omega")
    india = TreeNode("India")
    asia.add_child(china)
    asia.add_child(india)

    # Adding cities in China
    beijing = TreeNode("Beijing")
    shanghai = TreeNode("Shanghai")
    china.add_child(beijing)
    china.add_child(shanghai)

    return root