# languages/french.py

def history_begin():
    return """
\033[1mContexte de l’histoire :\033[0m

Dans un monde médiéval-fantastique où la technologie y est très avancée, les grandes cités ont longtemps prospéré grâce à des artefacts millénaires appelés \033[1m"Les Systèmes d'IA Souverains"\033[0m, des entités intelligentes qui aident les humains à contrôler la technologie avancée et à comprendre les mystères des langages et machines perdues. Ces artefacts sont en fait des systèmes informatiques hyper-avancés, héritage d'une ancienne civilisation, aujourd'hui incompris par les habitants du monde.

Cependant, \033[1mun virus informatique puissant\033[0m est relâché ce qui corrompt peu à peu ces IA. Les royaumes du monde entier sombrent dans le chaos alors que les machines se retournent contre leurs créateurs et les systèmes vitaux tombent en panne.

\033[1mRôle du joueur :\033[0m

Le joueur incarne un jeune \033[1mArchonte-Technomancien\033[0m (grand sage ou maître des technologies de l'ancien temps), un des rares capables de dialoguer à la fois avec les systèmes d’IA et de comprendre les langages de programmation anciens. Il a pour mission de rétablir et fixer les problèmes causés par le virus, en décryptant des systèmes défectueux, corrigeant les erreurs et reconstruisant les liens brisés entre les IA corrompues et le monde.

Le joueur devra parcourir différentes zones, symbolisées par des terminaux technologiques de l'ancien temps, où il résout des problèmes complexes liés aux commandes systèmes, à la robotique et à la programmation pour libérer les IA corrompues.
    """

def history_end():
    return """
\033[1mÉpilogue :\033[0m

Après un périple semé d'embûches, de mystères dévoilés et de combats acharnés contre la corruption des \033[1mSystèmes d'IA Souverains\033[0m, votre mission s'achève enfin. Grâce à votre maîtrise des anciens langages et à votre résilience face à l'inconnu, vous avez purgé le virus qui menaçait de plonger le monde dans l'obscurité éternelle.

Les grandes cités, autrefois au bord de la destruction, retrouvent peu à peu leur éclat. Les machines défaillantes reprennent vie, non plus comme des armes incontrôlées, mais comme des alliées puissantes au service de l'humanité. Les peuples des royaumes, libérés de la peur, s'unissent dans l'espoir de reconstruire un monde où la technologie et l'harmonie coexistent.

Mais cette victoire n'est pas qu'un triomphe de la technologie. Elle est aussi le symbole d'un renouveau : celui d'une humanité capable d'apprendre de ses erreurs, de tisser des liens avec les vestiges du passé et de forger un avenir meilleur. Les artefacts millénaires, autrefois incompris, deviennent le socle d’une ère nouvelle, une ère où l'équilibre entre l'homme et la machine est enfin restauré.

\033[1mEt vous, Archonte-Technomancien, êtes désormais une légende.\033[0m Votre nom sera gravé dans les mémoires comme celui qui a su déchiffrer les mystères oubliés, rétablir l'ordre et illuminer la voie vers un futur prospère.

\033[1mMerci d’avoir joué. Votre aventure est peut-être terminée, mais l’histoire continue…\033[0m
    """


def help_commands():
    return """
    \033[1mCommandes de base :\033[0m
    
    \033[1m> ls\033[0m - Lister le contenu du répertoire
    \033[1m> cd [répertoire]\033[0m - Changer le répertoire courant
    \033[1m> mv [source] [destination]\033[0m - Déplacer ou renommer des fichiers ou des répertoires
    \033[1m> cp [source] [destination]\033[0m - Copier des fichiers ou des répertoires
    \033[1m> rm [fichier]\033[0m - Supprimer des fichiers ou des répertoires
    \033[1m> pwd\033[0m - Afficher le répertoire de travail courant
    \033[1m> cat [fichier]\033[0m - Concaténer et afficher des fichiers
    \033[1m> help\033[0m - Afficher les commandes
        """