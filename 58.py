# -*- coding: UTF-8
from random import randint
from time import sleep
computador = randint(0, 10)
print("Sou seu computador... Acabei de pensar em um número entre 0 e 10.")
print("Será que voce consegue adivinhar qual foi? ")
acertou = False
palpite = 0
while not acertou:
    jogador = int(input("Qual é seu palpite? "))
    print("PROCESSANDO...")
    sleep(0.5)
    palpite = palpite + 1
    if jogador == computador:
        acertou = True
    else:
        if jogador < computador:
            print("Tente um número maior.")
        elif jogador > computador:
            print("Tente um número menor.")
print("ACERTOU!!! com {} tentativas. Parabéns".format(palpite))