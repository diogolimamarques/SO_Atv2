import Th
import sys
import escalonadorFila
import filaPRIO
from random import randint

NUMERO_DE_THREADS = 20 # ESTE VALOR INDICA A QUANTIDADE DE THREADS QUE SERÃO GERADAS.

MODO_DE_OPERACAO = 0 

# Corpo principal do código.

fila = filaPRIO.filaPRIO()
escalonador = escalonadorFila.escalonador(fila)
escalonador.start()

for thread_number in range (NUMERO_DE_THREADS):
  quantum = 1

  thread = Th.Th(thread_number, quantum, fila)
  #threadRef = Th.ThRef(thread_number, quantum)
  fila.insert(thread, quantum)

  thread.start()

  delay = randint(0,20)
  while (delay > 0):
    delay = delay - 1

while(True):
  loop = 0
