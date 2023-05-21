import keyboard
import random
import time

num = int(input("quante belle parole vuoi dire? "))
time.sleep(5)
i = 0
while(i <= num):
    file = open("lista_badwords.txt","r")
    testo = random.choice(file.readlines())
    keyboard.write(testo)
    keyboard.press_and_release("enter")
    i+=1