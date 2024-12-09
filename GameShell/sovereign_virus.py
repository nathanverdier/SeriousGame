# main.py

import time
import utils.clear_shell as clear
import scripts.init as init
import scripts.start as start
import utils.parchemin as parchemin

def main():
    clear.clear_screen()
    lang = init.select_language()
    clear.clear_screen()

    if lang == 'en':
        warning = "\033[1m\033[91mWARNING: FOR THE BEST EXPERIENCE, PLEASE MAXIMIZE YOUR TERMINAL WINDOW.\033[0m"
    elif lang == 'fr':
        warning = "\033[1m\033[91mATTENTION: METTEZ VOTRE TERMINAL EN PLEIN ÉCRAN POUR UNE MEILLEURE EXPÉRIENCE.\033[0m"

    parchemin.display_parchemin(warning)
    time.sleep(4)  # Délai de 8 secondes
    
    clear.clear_screen()
    init.display_welcome_scroll(lang)    
    start.game(lang)

if __name__ == "__main__":
    main()