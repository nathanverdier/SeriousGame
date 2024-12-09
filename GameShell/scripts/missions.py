# missions.py

def mission_1(lang):
    if lang == 'en':
        print("Mission 1: Navigate to the 'Cybersecurity' directory and list its contents.")
    elif lang == 'fr':
        print("Mission 1: Naviguer vers le répertoire 'Cybersecurite' et afficher son contenu.")

def mission_2(lang):
    if lang == 'en':
        print("Mission 2: Navigate to the 'Corrupted_Data' directory and display the current path.")
    elif lang == 'fr':
        print("Mission 2: Naviguer vers le répertoire 'Donnees_corrompues' et afficher le chemin actuel.")

def last_mission(lang):
    if lang == 'en':
        print("Mission 3: Solve the puzzle to proceed.")
        print("Hint: The password is the name of the virus that contaminated the AI.")
    elif lang == 'fr':
        print("Mission 3: Résolvez l'énigme pour continuer.")
        print("Indice: Le mot de passe est le nom du virus qui a contaminé l'IA.")
    
    password = "SovereignVirus"
    attempts = 3

    while attempts > 0:
        user_input = input("Enter the password: ")
        if user_input == password:
            print("Correct! Mission 3 completed!")
            return True
        else:
            attempts -= 1
            print(f"Incorrect! You have {attempts} attempts left.")
    
    print("Mission failed. Try again.")
    return False