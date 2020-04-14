#!/usr/bin/python
# -*- coding: utf-8 -*-

# @author Anderson Sosnierz 2020-02-25
# Cor \033[style; text; back m \033[m


############

answer = input("Are you over 16?")
if answer == "Yes":
   print("You can take driving lessons to prepare for your driving test.")
elif answer == "No":
   print("You are too young to learn how to drive a car.")