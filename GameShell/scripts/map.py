# map.py

translations = {
    "World": "Monde",
    "Eupi": "Eupi",
    "AI": "IA",
    "Development": "Developpement",
    "Cybersecurity": "Cybersecurite",
    "Algorithm": "Algorithme",
    "Test_Validation": "Test_Validation",
    "Security_Sphere": "Sphere_securite",
    "Quarantine_Zone": "Zone_quarantaine",
    "Corrupted_Data": "Données_corrompues"
}

class TreeNode:
    def __init__(self, name, parent=None, is_directory=True):
        self.name = name
        self.children = []
        self.parent = parent
        self.is_directory = is_directory

    def add_child(self, child_node):
        child_node.parent = self
        self.children.append(child_node)

    def list_children(self):
        for child in self.children:
            if child.is_directory:
                print(f"\033[34m{child.name}\033[0m", end=' ')  # Blue for directories
            else:
                print(f"\033[32m{child.name}\033[0m", end=' ')  # Green for files
        print()

    def find_child(self, name):
        for child in self.children:
            if child.name == name:
                return child
        return None

    def get_path(self, lang):
        path = []
        node = self
        while node:
            path.append(node.name)
            node = node.parent
        path = list(reversed(path))
        
        if lang == 'fr':
            path = [translations.get(name, name) for name in path]
        
        return '/' + '/'.join(path)

def create_sample_map(lang):
    def translate(name):
        return translations.get(name, name) if lang == 'fr' else name

    root = TreeNode(translate("World"))

    eupi = TreeNode(translate("Eupi"))
    root.add_child(eupi)

    dep_ia = TreeNode(translate("AI"))
    dep_dev = TreeNode(translate("Development"))
    dep_cyber = TreeNode(translate("Cybersecurity"))
    dep_algo = TreeNode(translate("Algorithm"))
    dep_validation = TreeNode(translate("Test_Validation"))
    eupi.add_child(dep_ia)
    eupi.add_child(dep_dev)
    eupi.add_child(dep_cyber)
    eupi.add_child(dep_algo)
    eupi.add_child(dep_validation)

    # Adding cities in Cybersecurity
    sec_sphere = TreeNode(translate("Security_Sphere"))
    sec_quarantine = TreeNode(translate("Quarantine_Zone"))
    sec_corrupted_data_temple = TreeNode(translate("Corrupted_Data"))
    dep_cyber.add_child(sec_sphere)
    dep_cyber.add_child(sec_quarantine)
    dep_cyber.add_child(sec_corrupted_data_temple)
    
    return root