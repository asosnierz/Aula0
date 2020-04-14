#!/usr/bin/python
# -*- coding: utf-8 -*-

# @author Anderson Sosnierz 2020-02-25
# Vermelho e branco -> ('\033[0;30;41m'+' o texto'+'\033[0;0m] ])



import os

############
def sim_nao():
pergunta = input('Você que saber o Seu Ip do Wi-fi?: (S/N)')
if pergunta == "s":
    wifi = 'ifconfig wlan0'
    print ('\033[0;30;41m'+'O IP DO SEU WI-FI É :'+'\033[0;0m')
    os.system(wifi)
    print('\033[0;30;41m'+'FIM DE DADOS'+'\033[0;0m')
else:
    print('\033[0;30;43m'+'FIM DE DADOS'+'\033[0;0m') 

if __name__=='__main__':
sim_nao()