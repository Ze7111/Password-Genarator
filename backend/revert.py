from subprocess import call
import os
def clear():
    call('cls' if os.name == 'nt' else 'clear', shell=True)
    return