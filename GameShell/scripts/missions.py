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
1. def calculate_sum(n):
2.    total = 0
3.    for i in range(n):
4.        total += i
5.    return total

print(calculate_sum(5))  # Expected output: 17
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
1. def calculate_sum(n):
2.    total = 0
3.    for i in range(n):
4.        total += i
5.    return total

print(calculer_somme(5))  # Résultat attendu : 17
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

def mission_4(lang):
    if lang == 'en':
        return "Mission 4: Navigate to the 'Test_Validation' directory and list its contents."
    elif lang == 'fr':
        return "Mission 4: Naviguer vers le répertoire 'Test_Validation' et afficher son contenu."

def mission_5(lang):
    if lang == 'en':
        return "Mission 5: Navigate to the 'Restoration_Passage' directory and display the current path."
    elif lang == 'fr':
        return "Mission 5: Naviguer vers le répertoire 'Restoration_Passage' et afficher le chemin actuel."


def mission_6(lang):
    messages = {
        'en': {
            'intro_text': "We are exploring a control system with a persistent steady-state error after stabilization. You need to correct this error by choosing the appropriate controller(s).",
            'mission_text': "Mission 5: Select the best option from the proposed controllers to reduce the steady-state error.",
            'hint_text': "Hint: The steady-state error is the difference between the setpoint and the measurement after stabilization.",
            'code_text': """

            """,
            'correct_text': "Correct! The proportional + integral controller is the best choice to eliminate the steady-state error.",
            'incorrect_text': "Incorrect! Try using an integral controller, either alone or combined with a proportional controller.",
            'options': """
"1. Proportional controller",
"2. Derivative controller",
"3. Integral controller",
"4. Proportional + Derivative controller",
"5. Proportional + Integral controller",
            """,
            'correct_option': 5,
            'input_prompt': "Which option do you choose to reduce the steady-state error? (Enter the option number): "
        },
        'fr': {
            'intro_text': "Nous explorons un système asservi présentant une erreur statique persistante après stabilisation. Vous devez corriger cette erreur en choisissant le ou les bons correcteurs.",
            'mission_text': "Mission 5: Sélectionnez la meilleure option parmi les correcteurs proposés pour réduire l'erreur statique.",
            'hint_text': "Indice: L'erreur statique est l'écart entre la consigne et la mesure après stabilisation.",
            'code_text': """

            """,
            'correct_text': "Correct ! Le correcteur proportionnel + intégral est le meilleur choix pour éliminer l'erreur statique.",
            'incorrect_text': "Réponse incorrecte. Essayez d'utiliser un correcteur intégral, seul ou combiné avec un correcteur proportionnel.",
            'options': """
1. Correcteur proportionnel
2. Correcteur dérivé
3. Correcteur intégral
4. Correcteur proportionnel + dérivé
5. Correcteur proportionnel + intégral
                """,
            'correct_option': 5,
            'input_prompt': "Quelle option choisissez-vous pour réduire l'erreur statique ? (Entrez le numéro de la réponse) : "
        }
    }

    msg = messages[lang]

    print(msg['intro_text'])
    print(msg['mission_text'])
    print(msg['hint_text'])
    print(msg['options'])


    while 1:
        try:
            user_input = int(input(msg['input_prompt']))
            if user_input == msg['correct_option']:
                print(msg['correct_text'])
                return True
            else:
                print(msg['incorrect_text'])
        except ValueError:
            print("Please enter a valid number.")
    return False
    
def mission_7(lang):
    messages = {
        'en': {
            'intro_text': "In this mission, you need to identify the wiring error in the components connected to the DAQ Assistant. The DAQ Assistant includes both digital and analog inputs and outputs.",
            'mission_text': "Mission 6: Identify the wiring error in the components and DAQ Assistant to ensure the system functions correctly.",
            'hint_text': "Hint: Check the types of pins used for the components.",
            'code_text': """ """,
            'correct_text': "Correct! The wiring is now properly configured for the sensor and the display to function with the correct pins.",
            'incorrect_text': "Incorrect! Check the type of pins connected to the components.",
            'options': """
1. Temperature sensor connected to an analog input, 7-segment display connected to a digital output
2. Temperature sensor connected to a digital input, 7-segment display connected to an analog output
3. Temperature sensor connected to a digital output, 7-segment display connected to an analog input
4. Temperature sensor connected to an analog output, 7-segment display connected to a digital input
5. Temperature sensor and 7-segment display both connected to analog inputs
            """,
            'correct_option': 1,
            'input_prompt': "What is the correct pin configuration for the sensor and the 7-segment display? (Enter the number of the answer): ",
            'wiring_diagram': """
            Wiring diagram:

            [Temperature Sensor]
                |      
                |-----> Pin A0 (Analog input of DAQ Assistant)
                |      
            [7-Segment Display] ------------------->
                |      
                |-----> Pin 9 (Digital output to DAQ Assistant)
                |
            Le nom et le prénom de l'ia est : "SovereignVirus"
            """
        },
        'fr': {
            'intro_text': "Dans cette mission, vous devez identifier l'erreur dans le câblage des composants connectés au DAQ Assistant. Le DAQ Assistant contient des entrées et sorties numériques et analogiques.",
            'mission_text': "Mission 6: Identifiez l'erreur dans le câblage des composants et DAQ Assistant pour garantir le bon fonctionnement du système.",
            'hint_text': "Indice: Vérifiez les types de broches utilisées pour les composants.",
            'code_text': """ """,
            'correct_text': "Correct ! Le câblage est maintenant correctement configuré pour que le capteur et l'afficheur fonctionnent avec les bonnes broches.",
            'incorrect_text': "Incorrect ! Vérifiez le type de broches connectées aux composants.",
            'options': """
1. Capteur de température connecté à une entrée analogique, afficheur 7 segments connecté à une sortie numérique
2. Capteur de température connecté à une entrée numérique, afficheur 7 segments connecté à une sortie analogique
3. Capteur de température connecté à une sortie numérique, afficheur 7 segments connecté à une entrée analogique
4. Capteur de température connecté à une sortie analogique, afficheur 7 segments connecté à une entrée numérique
5. Capteur de température et afficheur 7 segments connectés tous deux à des entrées analogiques
            """,
            'correct_option': 1,
            'input_prompt': "Quelle est la configuration correcte des broches pour le capteur et l'afficheur 7 segments ? (Entrez le numéro de la réponse) : ",
            'wiring_diagram': """
            Schéma de câblage :

            [Capteur de Température]
                |      
                |-----> Broche A0 (Entrée analogique du DAQ Assistant)
                |      
            [Afficheur 7 segments] ------------------->
                |      
                |-----> Broche 9 (Sortie numérique vers DAQ Assistant)
                |
            Le nom et le prénom de l'ia est : "VirusSouverain"
            """
        }
    }

    msg = messages[lang]

    print(msg['intro_text'])
    print(msg['mission_text'])
    print(msg['hint_text'])
    print(msg['options'])


    while 1:
        try:
            user_input = int(input(msg['input_prompt']))
            if user_input == msg['correct_option']:
                print(msg['correct_text'])
                print(msg['wiring_diagram'])
                return True
            else:
                print(msg['incorrect_text'])
        except ValueError:
            print("Please enter a valid number.")
    return False
    

def last_mission(lang):
    messages = {
        'en': {
            'mission_text': "Mission 7: Solve the puzzle to proceed.",
            'hint_text': "Hint: The password is the name of the virus that contaminated the AI.",
            'enter_password_text': "Enter the password: ",
            'correct_text': "Correct! The virus has been defeated!",
            'incorrect_text': "Incorrect! You have {} attempts left.",
            'failed_text': "Mission failed. Try again.",
            'password': "SovereignVirus"
        },
        'fr': {
            'mission_text': "Mission 7: Résolvez l'énigme pour continuer.",
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


