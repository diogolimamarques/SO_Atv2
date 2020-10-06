from threading import Thread
from random import randint
import random
import string
import sys
import os
import time

# Classe que extende da classe Thread.

class Th(Thread):

  def __init__ (self, num, quantum, fila):
    Thread.__init__(self)
    self.num = num
    self.countdown = randint(2000, 40000)
    self.quantum = quantum
    self.permissao = False
    self.fila = fila

  def run(self):
    sys.stdout.write("Thread de numero " + str(self.num) + " criada\n")
    sys.stdout.flush()

    while(self.countdown > 0):
      if (self.permissao == True):
        #sys.stdout.write(str(self.num) + " "+str(self.quantum)+" \n")
        #sys.stdout.flush()
        self.countdown = self.countdown - 1

    sys.stdout.write("Thread de numero " + str(self.num) + " primeiro countdown FINALIZADO... Boa noite! Z z Z z Z z\n")
    sys.stdout.flush()

    time.sleep(randint(1,10))

    self.countdown = randint(2000, 20000)

    if(self.quantum > 1):
      self.quantum = self.quantum - 1

    sys.stdout.write("Thread de numero " + str(self.num) + " retornando à fila com prioridade elevada! Novo quantum: "+str(self.quantum)+"\n")
    sys.stdout.flush()

    self.fila.insert(self, self.quantum)

    while(self.countdown > 0):
      if (self.permissao == True):
        #sys.stdout.write(str(self.num) + " "+str(self.quantum)+" \n")
        #sys.stdout.flush()
        self.countdown = self.countdown - 1

    sys.stdout.write("Thread de numero " + str(self.num) + " segundo countdown FINALIZADO COM SUCESSO :)\n")
    sys.stdout.flush()




class ThRef():
  def __init__(self, num, quantum): 
    self.num = num
    self.quantum = quantum
