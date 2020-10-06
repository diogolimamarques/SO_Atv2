from threading import Thread
from random import randint
import random
import string
import sys
import os
import time

# Classe que extende da classe Thread.

class escalonador(Thread):

  def __init__ (self, fila):
    Thread.__init__(self)
    self.fila = fila

    sys.stdout.write("ESCALONADOR DE PROCESSOS INICIADO...\n")
    sys.stdout.flush()

  def run(self):
    count = 0
    while(True):
      #sys.stdout.write("a\n")
      #sys.stdout.flush()
      if (self.fila.isEmpty() == False):
        sys.stdout.flush()
        proximo = self.fila.retornaProximo()
        quantum = proximo.quantum
        proximo.permissao = True

        #sys.stdout.write("Thread de numero " + str(proximo.num) + " em execução... Quantum: "+str(proximo.quantum)+"\n")
        sys.stdout.flush()

        time.sleep(quantum*0.001)
        
        proximo.permissao = False
        if(proximo.countdown != 0):
          proximo.quantum = quantum+1
          self.fila.deletaElemento()
          self.fila.insert(proximo, proximo.quantum)
        else:
          self.fila.deletaElemento()
      elif (count < 200):
        time.sleep(0.05)
        count = count + 1
      elif (count == 200):
        sys.stdout.write("Todos os processos foram escalonados e executados com sucesso!\n")
        sys.stdout.flush()
        count = count + 1

 
class ThRef():
  def __init__(self, num, quantum): 
    self.num = num
    self.quantum = quantum
