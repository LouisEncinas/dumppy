import re
import os
import sys
import datetime

CURSOR_UP = '\033[F'
ERASE_LINE = '\033[K'
TIME_PATTERN = re.compile('^[0-9]{1,2}[.,:][0-9]{2}$')

def clear() -> None:
    os.system('cls' if os.name == 'nt' else 'clear')

def get_sep(string:str) -> str:
    sep = ''
    if len(string) == 4:
        sep = string[1]
    else:
        sep = string[2]
    return sep

def time_to_tuple(time:str, sep:str) -> tuple:
    split = time.split(sep)
    return (int(split[0]), int(split[1]))

def check_time(time:str) -> bool:
    if not TIME_PATTERN.match(time):
        return False
    sep = get_sep(time)
    tpl = time_to_tuple(time, sep)
    if (tpl[0] < 0 and tpl[0] > 23) or (tpl[1] < 0 and tpl[1] > 59):
        return False
    return True
    
def ask_time(msg:str) -> datetime.timedelta:
    show_msg = f'{msg} (hh.mm) : '
    time = input(show_msg)
    while not check_time(time):
        sys.stdout.write(CURSOR_UP + ERASE_LINE)
        time = input(show_msg)
    sep = get_sep(time)
    tpl = time_to_tuple(time, sep)
    return datetime.timedelta(hours=tpl[0], minutes=tpl[1])

def main():
    clear()
    h1 = ask_time("Heure d'arrivée")
    clear()
    h2 = ask_time("Heure de départ en pause repas")
    clear()
    h3 = ask_time("Heure de retour de pause repas")
    clear()
    if not (h1 < h2 and h2 < h3):
        print("Incohérence dans les temps rentrés\n")
    else:
        tot = datetime.timedelta(hours=7, minutes=36)
        pause = datetime.timedelta(minutes=45)
        if (h3 - h2) < pause:
            print(f"Temps de pause pris inférieur à 45 minutes. L'heure de retour de repas est mise à : {h2 + pause}\n")
            h3 = h2 + pause
        print(f"Heure à partir de laquelle vous pouvez partir : {tot - (h2 - h1) + h3}\n")
    input("Appuyez sur entrée pour quitter.")

if __name__ == '__main__':
    main()