# start.py
from time import sleep
import languages.english as english
import languages.french as french
import utils.parchemin as parchemin
from scripts.map import create_sample_map, TreeNode
import readline
from scripts.completer import completer
from scripts.navigation import find_node_by_path
from scripts.missions import mission_1, mission_2, mission_3, mission_4, mission_5, mission_6, mission_7, last_mission
import utils.clear_shell as clear

def game(lang):
    global current_node  # Make current_node accessible in the completer function
    global map_root  # Make map_root accessible in the completer function

    if lang == 'en':
        history_text = english.history_begin()
        commands_text = english.help_commands()
    elif lang == 'fr':
        history_text = french.history_begin()
        commands_text = french.help_commands()
    
    # Afficher le texte en utilisant display_parchemin
    parchemin.display_parchemin(history_text)
    parchemin.display_help_commands_parchemin(commands_text)

    # Créer la carte
    map_root = create_sample_map(lang)
    current_node = map_root

    readline.set_completer(lambda text, state: completer(text, state, current_node))
    readline.parse_and_bind("tab: complete")

    mission = 1
    current_mission = mission_1(lang)
    parchemin.display_parchemin(current_mission)

    while True:
        command = input(f"[mission {mission}] $ ")

        if command.startswith("cd"):
            parts = command.split(maxsplit=1)
            if len(parts) == 1 or parts[1] == "/":
                current_node = map_root
            else:
                destination = parts[1]
                next_node = find_node_by_path(current_node, destination)
                if next_node:
                    current_node = next_node
                    if mission == 1 and current_node.name == "Cybersecurity" or current_node.name == "Cybersecurite":
                        print("Mission 1 completed!")
                        current_mission = mission_2(lang)
                        parchemin.display_parchemin(current_mission)
                        mission = 2
                    elif mission == 2 and (current_node.name == "Corrupted_Data" or current_node.name == "Donnees_corrompues"): 
                        print("Mission 2 completed!")
                        print(current_node.get_path(lang))
                        mission = 3
                    # elif mission == 4 and (current_node.name == "Test_Validation" or current_node.name == "Test_Validation"): 
                    #     print("Mission 4 completed!")
                    #     print(current_node.get_path(lang))
                    #     mission = 5
                    # if mission == 5:
                    #     clear.clear_screen()
                    #     if mission_7(lang):
                    #         mission = 0
                    #         sleep(4)

        elif command == "ls":
            current_node.list_children()
        elif command == "pwd":
            print(current_node.get_path(lang))
        elif command == "help":
            parchemin.display_help_commands_parchemin(commands_text)
            parchemin.display_parchemin(current_mission)
        elif command == "exit":
            break
        else:
            if lang == 'en':
                print("Unknown command. Type 'help' for a list of commands.")
            elif lang == 'fr':
                print("Commande inconnue. Tapez 'help' pour une liste de commandes.")

        if mission == 3:
            clear.clear_screen()
            if mission_3(lang):
                mission = 4
                sleep(4)

        if mission == 4:
            clear.clear_screen()
            if mission_6(lang):
                mission = 5
                sleep(6)

        if mission == 5:
            clear.clear_screen()
            if mission_7(lang):
                mission = 0
                input("Press Enter to continue...")

        if mission == 0:
            clear.clear_screen()
            if last_mission(lang):
                if lang == 'en':
                    history_text = english.history_end()
                elif lang == 'fr':
                    history_text = french.history_end()
                parchemin.display_parchemin(history_text)
                sleep(30)
                break