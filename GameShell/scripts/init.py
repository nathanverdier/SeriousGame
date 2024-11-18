# init.py

import utils.parchemin as parchemin

def select_language():
    print("Select your language / Sélectionnez votre langue:")
    print("1. English")
    print("2. Français")
    
    choice = input("Enter the number of your choice / Entrez le numéro de votre choix: ")
    
    if choice == '1':
        return 'en'
    elif choice == '2':
        return 'fr'
    else:
        print("Invalid choice / Choix invalide")
        return select_language()

def display_welcome_scroll(lang):
    if lang == 'en':
        message = "\033[1mWelcome to The Sovereign Virus!\033[0m"
    elif lang == 'fr':
        message = "\033[1mBienvenue dans Le Virus Souverain!\033[0m"
    parchemin.display_parchemin(message)
   