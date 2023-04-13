import sys
import time
import os

def typingPrint(txt):
    for character in txt:

        sys.stdout.write(character)
        sys.stdout.flush()
        time.sleep(0.05)

def clearScreen():
  os.system("cls")
