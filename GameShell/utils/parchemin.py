# utils/parchemin.py

import re
import time
import sys

MAX_WIDTH = 100  # Définir la largeur maximale pour le texte

def strip_ansi_codes(text):
    ansi_escape = re.compile(r'\x1B[@-_][0-?]*[ -/]*[@-~]')
    return ansi_escape.sub('', text)

def wrap_text(text, width):
    words = text.split()
    lines = []
    current_line = []

    for word in words:
        stripped_line = strip_ansi_codes(' '.join(current_line))
        if len(stripped_line) + len(current_line) + len(word) <= width:
            current_line.append(word)
        else:
            lines.append(' '.join(current_line))
            current_line = [word]

    if current_line:
        lines.append(' '.join(current_line))

    return lines

def wrap_text_with_newlines(text, width):
    paragraphs = text.split('\n')
    wrapped_lines = []
    for paragraph in paragraphs:
        if paragraph.strip() == "":
            wrapped_lines.append("")
        else:
            wrapped_lines.extend(wrap_text(paragraph, width))
    return wrapped_lines

def display_parchemin(message):
    wrapped_lines = wrap_text_with_newlines(message, MAX_WIDTH)
    
    max_length = min(MAX_WIDTH, max(len(strip_ansi_codes(line)) for line in wrapped_lines))
    border = '-' * 2 + '+' + '-' * (max_length + 4) + '+' + '-' * 2
    empty_line = ' ' * 2 + '|' + ' ' * (max_length + 4) + '|'
    
    print()
    print()
    print(border)
    print(empty_line)
    for line in wrapped_lines:
        if line.strip() == "":
            print(empty_line)
        else:
            sys.stdout.write("  |  ")
            for char in line.ljust(max_length + len(line) - len(strip_ansi_codes(line))):
                sys.stdout.write(char)
                sys.stdout.flush()
                time.sleep(0.005)  # Délai de 20 millisecondes entre chaque caractère
            sys.stdout.write("  |\n")
    print(empty_line)
    print(border)
    print()
    print()


def display_help_commands_parchemin(message):    
    wrapped_lines = wrap_text_with_newlines(message, MAX_WIDTH)
    
    max_length = min(MAX_WIDTH, max(len(strip_ansi_codes(line)) for line in wrapped_lines))
    border = '-' * 2 + '+' + '-' * (max_length + 4) + '+' + '-' * 2
    empty_line = ' ' * 2 + '|' + ' ' * (max_length + 4) + '|'
    
    print()
    print()
    print(border)
    print(empty_line)
    for line in wrapped_lines:
        if line.strip() == "":
            print(empty_line)
        else:
            sys.stdout.write("  |  ")
            for char in line.ljust(max_length + len(line) - len(strip_ansi_codes(line))):
                sys.stdout.write(char)
                sys.stdout.flush()
                time.sleep(0.005)  # Délai de 20 millisecondes entre chaque caractère
            sys.stdout.write("  |\n")
    print(empty_line)
    print(border)
    print()
    print()