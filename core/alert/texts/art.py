# ANSI escape-код для пурпурного цвета
from art import art, text2art, tprint, aprint

PURPLE = '\033[95m'
END = '\033[0m'

# ASCII-арт для "EUPHORIA ALERT"
ascii_art = """
███████╗██╗░░░██╗██████╗░██╗░░██╗░█████╗░██████╗░██╗░█████╗░  ░█████╗░██╗░░░░░███████╗██████╗░████████╗
██╔════╝██║░░░██║██╔══██╗██║░░██║██╔══██╗██╔══██╗██║██╔══██╗  ██╔══██╗██║░░░░░██╔════╝██╔══██╗╚══██╔══╝
█████╗░░██║░░░██║██████╔╝███████║██║░░██║██████╔╝██║███████║  ███████║██║░░░░░█████╗░░██████╔╝░░░██║░░░
██╔══╝░░██║░░░██║██╔═══╝░██╔══██║██║░░██║██╔══██╗██║██╔══██║  ██╔══██║██║░░░░░██╔══╝░░██╔══██╗░░░██║░░░
███████╗╚██████╔╝██║░░░░░██║░░██║╚█████╔╝██║░░██║██║██║░░██║  ██║░░██║███████╗███████╗██║░░██║░░░██║░░░
╚══════╝░╚═════╝░╚═╝░░░░░╚═╝░░╚═╝░╚════╝░╚═╝░░╚═╝╚═╝╚═╝░░╚═╝  ╚═╝░░╚═╝╚══════╝╚══════╝╚═╝░░╚═╝░░░╚═╝░░░
"""
purple_ascii_art = PURPLE + ascii_art + END

created_by_text = PURPLE + "    Created by github.com/Oldweedkeeper2" + END
