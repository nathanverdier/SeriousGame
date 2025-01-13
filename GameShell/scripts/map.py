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
    "Firewall_Bastion": "Bastion_pare-feu",
    "Quarantine_Zone": "Zone_quarantaine",
    "System_Purge_Station": "Station_purge_systeme",
    "Corrupted_Data": "Donnees_corrompues",
    "Forge_Protocols": "Protocoles_forge",
    "Coders_Workshop": "Atelier_du_codeur",
    "Origins": "Origines",
    "Corrupted_Heart": "Cœur Corrompu",
    "Sanctuary_Relics": "Reliques_sanctuaire",
    "Gallery_of_Algorithms": "Galerie_des_Algorithmes",
    "Circuit_Labyrinth": "Labyrinthe_de_Circuits",
    "Digital_Observatory": "Observatoire_Digital",
    "Cathedral_of_Machines": "Cathedrale_des_Machines",
    "Diagnostic_Terminal": "Terminal_Diagnostique",
    "Debugging_Chamber": "Chambre_de_Debug",
    "Restoration_Passage": "Restoration_Passage",
    "Breakpoint_Zone": "Zone_de_Point_d_Arret"
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
    sec_firewall_bastion = TreeNode(translate("Firewall_Bastion"))
    sec_system_purge_station = TreeNode(translate("System_Purge_Station"))
    dep_cyber.add_child(sec_sphere)
    dep_cyber.add_child(sec_quarantine)
    dep_cyber.add_child(sec_corrupted_data_temple)
    dep_cyber.add_child(sec_system_purge_station)
    dep_cyber.add_child(sec_firewall_bastion)

    # Adding cities in IA
    ia_origins = TreeNode(translate("Origins"))
    ia_corrupted_heart = TreeNode(translate("Corrupted_Heart"))
    ia_sanctuary_relics = TreeNode(translate("Sanctuary_Relics"))
    dep_ia.add_child(ia_origins)
    dep_ia.add_child(ia_corrupted_heart)
    dep_ia.add_child(ia_sanctuary_relics)

    # Adding cities in Development
    dev_forge_protocols = TreeNode(translate("Forge_Protocols"))
    dev_coders_workshop = TreeNode(translate("Coders_Workshop"))
    dep_dev.add_child(dev_forge_protocols)
    dep_dev.add_child(dev_coders_workshop)

     # Adding Algorithm section
    gallery_of_algorithms = TreeNode(translate("Gallery_of_Algorithms"))
    circuit_labyrinth = TreeNode(translate("Circuit_Labyrinth"))
    digital_observatory = TreeNode(translate("Digital_Observatory"))
    cathedral_of_machines = TreeNode(translate("Cathedral_of_Machines"))
    dep_algo.add_child(gallery_of_algorithms)
    dep_algo.add_child(circuit_labyrinth)
    dep_algo.add_child(digital_observatory)
    dep_algo.add_child(cathedral_of_machines)

    # Adding Testing and Validation section
    diagnostic_terminal = TreeNode(translate("Diagnostic_Terminal"))
    debugging_chamber = TreeNode(translate("Debugging_Chamber"))
    restoration_passage = TreeNode(translate("Restoration_Passage"))
    breakpoint_zone = TreeNode(translate("Breakpoint_Zone"))
    dep_validation.add_child(diagnostic_terminal)
    dep_validation.add_child(debugging_chamber)
    dep_validation.add_child(restoration_passage)
    dep_validation.add_child(breakpoint_zone)
    
    return root