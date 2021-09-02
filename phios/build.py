import os
import colorama
from colorama import Fore

print(Fore.GREEN+'Converting .asm file to .bin _________ ')
try:
    os.system('nasm -f bin boot.asm -o boot.bin')#Turns .asm to .bin
    print(Fore.GREEN+'Sucess _________ ')
    print('')
    try:
        os.system('qemu-system-x86_64 boot.bin')#Runs a vm for boot.bin
        print('')
    except Exception as error:
        print(Fore.RED+'Starting vm failed!')
        print(Fore.RED+ error)
        print(Fore.RED+'Program exiting!')
        quit()
except Exception as error:
    print(Fore.RED+'Converting into .bin failed!')
    print(Fore.RED+ error)
    print(Fore.RED+ 'Program exiting!')
    quit()

