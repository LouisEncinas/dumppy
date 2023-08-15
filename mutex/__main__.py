import os

def clear() -> None:
    os.system('cls' if os.name == 'nt' else 'clear')

def writer() -> None:
    print("Ongoing treatment (enter to end)")
    with open("mutex\\file_to_check", "r"):
        input()

def checker() -> bool:
    try:
        os.remove(os.path.abspath("mutex\\file_to_check"))
    except PermissionError:
        print("Treatment already running in another process")
        return False
    else:
        with open("mutex\\file_to_check", "w"): pass
        return True

clear()

inp:str = ""
while inp != "exit":

    print("Start data treatment ('ok' to start, 'exit' to exit)")
    inp = input()

    if inp == "ok":
        if checker(): writer()