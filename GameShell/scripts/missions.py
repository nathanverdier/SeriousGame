# missions.py

def mission_1(lang):
    if lang == 'en':
        return "Mission 1: Navigate to the 'Cybersecurity' directory and list its contents."
    elif lang == 'fr':
        return "Mission 1: Naviguer vers le répertoire 'Cybersecurite' et afficher son contenu."

def mission_2(lang):
    if lang == 'en':
        return "Mission 2: Navigate to the 'Corrupted_Data' directory and display the current path."
    elif lang == 'fr':
        return "Mission 2: Naviguer vers le répertoire 'Donnees_corrompues' et afficher le chemin actuel."

def last_mission(lang):
    messages = {
        'en': {
            'mission_text': "Mission 3: Solve the puzzle to proceed.",
            'hint_text': "Hint: The password is the name of the virus that contaminated the AI.",
            'enter_password_text': "Enter the password: ",
            'correct_text': "Correct! The virus has been defeated!",
            'incorrect_text': "Incorrect! You have {} attempts left.",
            'failed_text': "Mission failed. Try again."
        },
        'fr': {
            'mission_text': "Mission 3: Résolvez l'énigme pour continuer.",
            'hint_text': "Indice: Le mot de passe est le nom du virus qui a contaminé l'IA.",
            'enter_password_text': "Entrez le mot de passe : ",
            'correct_text': "Correct! Le virus a été vaincu!",
            'incorrect_text': "Incorrect! Il vous reste {} tentatives.",
            'failed_text': "Mission échouée. Réessayez."
        }
    }

    msg = messages[lang]

    print(msg['mission_text'])
    print(msg['hint_text'])
    
    password = "SovereignVirus"
    attempts = 3

    while attempts > 0:
        user_input = input(msg['enter_password_text'])
        if user_input == password:
            print(msg['correct_text'])
            return True
        else:
            attempts -= 1
            print(msg['incorrect_text'].format(attempts))
    
    print(msg['failed_text'])
    return False