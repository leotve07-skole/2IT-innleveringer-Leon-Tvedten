from colorama import Fore, Style, Back, init #For å endre terminal farger, for å dekorere den.

init(autoreset=True)

colors = {
    "background" : {
        "WHITE_BACKGROUND" : Back.LIGHTWHITE_EX
    },
    "text" : {
         "GREEN" : Style.BRIGHT + Fore.GREEN
    }
}

style = {
    "g" : colors["text"]["GREEN"],
    "w_g": colors["background"]["WHITE_BACKGROUND"] + colors["text"]["GREEN"],
    "reset": Style.RESET_ALL
}