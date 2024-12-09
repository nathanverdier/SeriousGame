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

def mission_3(lang):
    messages = {
        'en': {
            'intro_text': "Here is the initial code of the virus. It has mutated since, but let's start with this.",
            'mission_text': "Mission 3: Identify the line with an error to proceed.",
            'hint_text': "Hint: The error is in the calculation logic.",
            'code_text': """
def calculate_sum(n):
    total = 0
    for i in range(n):
        total += i
    return total

print(calculate_sum(5))  # Expected output: 15
            """,
            'correct_text': "Correct! The error has been identified!",
            'incorrect_text': "Incorrect! Try again.",
            'error_line_index': 4,
            'input_prompt': "Enter the index of the line with the error: "
        },
        'fr': {
            'intro_text': "Voici le code initial du virus. Il a muté depuis, mais commençons par ceci.",
            'mission_text': "Mission 3: Identifiez la ligne avec une erreur pour continuer.",
            'hint_text': "Indice: L'erreur est dans la logique de calcul.",
            'code_text': """
def calculer_somme(n):
    total = 0
    for i in range(n):
        total += i
    return total

print(calculer_somme(5))  # Résultat attendu : 15
            """,
            'correct_text': "Correct! L'erreur a été identifiée!",
            'incorrect_text': "Incorrect! Réessayez.",
            'error_line_index': 4,
            'input_prompt': "Entrez l'index de la ligne avec l'erreur: "
        }
    }

    msg = messages[lang]

    print(msg['intro_text'])
    print(msg['mission_text'])
    print(msg['hint_text'])
    print(msg['code_text'])


    while 1:
        try:
            user_input = int(input(msg['input_prompt']))
            if user_input == msg['error_line_index']:
                print(msg['correct_text'])
                return True
            else:
                print(msg['incorrect_text'])
        except ValueError:
            print("Please enter a valid number.")
    return False
    

def last_mission(lang):
    messages = {
        'en': {
            'mission_text': "Mission 3: Solve the puzzle to proceed.",
            'hint_text': "Hint: The password is the name of the virus that contaminated the AI.",
            'enter_password_text': "Enter the password: ",
            'correct_text': "Correct! The virus has been defeated!",
            'incorrect_text': "Incorrect! You have {} attempts left.",
            'failed_text': "Mission failed. Try again.",
            'password': "SovereignVirus"
        },
        'fr': {
            'mission_text': "Mission 3: Résolvez l'énigme pour continuer.",
            'hint_text': "Indice: Le mot de passe est le nom du virus qui a contaminé l'IA.",
            'enter_password_text': "Entrez le mot de passe : ",
            'correct_text': "Correct! Le virus a été vaincu!",
            'incorrect_text': "Incorrect! Il vous reste {} tentatives.",
            'failed_text': "Mission échouée. Réessayez.",
            'password': "VirusSouverain"
        }
    }

    msg = messages[lang]

    print(msg['mission_text'])
    print(msg['hint_text'])
    
    password = msg['password']
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


