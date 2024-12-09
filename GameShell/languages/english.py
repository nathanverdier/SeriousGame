# languages/english.py

def history_begin():
    return """
\033[1mStory Context:\033[0m

In a medieval-fantasy world with highly advanced technology, great cities have long thrived thanks to millennia-old artifacts known as the \033[1m"Sovereign AI Systems."\033[0m These intelligent entities assist humans in controlling advanced technology and unraveling the mysteries of lost languages and machines. These artifacts are, in fact, hyper-advanced computer systems, a legacy of an ancient civilization now misunderstood by the world's inhabitants.

However, \033[1ma powerful computer virus\033[0m has been unleashed, gradually corrupting these AIs. The kingdoms across the world descend into chaos as the machines turn against their creators and vital systems collapse.

\033[1mPlayer Role:\033[0m

The player assumes the role of a young \033[1mArchon-Technomancer\033[0m—a grand sage or master of ancient technologies—one of the few capable of communicating with the AI systems and understanding the ancient programming languages. Their mission is to restore and fix the issues caused by the virus by decrypting malfunctioning systems, correcting errors, and rebuilding the broken connections between the corrupted AIs and the world.

The player will explore various zones, represented by ancient technological terminals, where they will solve complex problems related to system commands, robotics, and programming to liberate the corrupted AIs.
    """

def history_end():
    return """
\033[1mEpilogue:\033[0m

After a journey filled with challenges, unveiled mysteries, and fierce battles against the corruption of the \033[1mSovereign AI Systems\033[0m, your mission has finally reached its conclusion. Through your mastery of ancient languages and your resilience in the face of the unknown, you have eradicated the virus that threatened to plunge the world into eternal darkness.

The great cities, once teetering on the brink of destruction, are beginning to regain their former glory. Malfunctioning machines come back to life—not as uncontrollable weapons, but as powerful allies in the service of humanity. The peoples of the realms, freed from fear, unite in hope, rebuilding a world where technology and harmony can coexist.

But this victory is more than just a triumph of technology. It is a symbol of renewal: a testament to humanity’s ability to learn from its mistakes, forge connections with the remnants of the past, and shape a brighter future. The millennia-old artifacts, once misunderstood, now form the foundation of a new era—an era where balance between humans and machines has finally been restored.

\033[1mAnd you, Archon-Technomancer, are now a legend.\033[0m Your name will be etched into history as the one who deciphered forgotten mysteries, restored order, and lit the path to a prosperous future.

\033[1mThank you for playing. Your adventure may have ended, but the story lives on...\033[0m
    """


def help_commands():
    return """
\033[1mBasic Commands:\033[0m

\033[1m> ls\033[0m - List directory contents
\033[1m> cd [directory]\033[0m - Change the current directory
\033[1m> mv [source] [destination]\033[0m - Move or rename files or directories
\033[1m> cp [source] [destination]\033[0m - Copy files or directories
\033[1m> rm [file]\033[0m - Remove files or directories
\033[1m> pwd\033[0m - Print the current working directory
\033[1m> cat [file]\033[0m - Concatenate and display files
\033[1m> help\033[0m - Display commandes information
    """