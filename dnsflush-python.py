from os import system
from time import sleep

hour = [0,0,0]
while True:
    system("ipconfig /flushdns")
    system('cls')
    hour[2] += 1
    if hour[2] == 60:
        hour[1] += 1
        hour[1] = 0
    if hour[1] == 60:
        hour[0] += 1
        hour[0] = 0
    print('\nTime Running yet:')
    print(hour[0],hour[1],hour[2],sep = ' : ')
    sleep(1)
