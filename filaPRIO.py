import sys

# Classe que imprementa uma fila PRIO

class filaPRIO(object): 

  # Inicialização da fila

  def __init__(self): 
    self.queue = [] 
  
  def __str__(self): 
    return ' '.join([str(i) for i in self.queue]) 
  
  # Checa se a fila está vazia
  def isEmpty(self): 
    return len(self.queue) == 0
  
  # Insere um elemento no fim da fila

  def insert(self, data, prio):
    i = -1
    var = 0
    pos = 0
    
    for elemento in self.queue:
      i = i + 1
      if (elemento.quantum > prio):
        pos = i
        var = 1
        break

    if (var == 1):
      self.queue.insert(pos, data)
      #sys.stdout.write("NUMERO DE ELEMENTOS NA FILA: " + str(len(self.queue))+"\n")
      #sys.stdout.flush()
      #sys.stdout.write("Inserindo elemento na fila na posicao "+str(i)+"\n")
      #sys.stdout.flush()
    if (var == 0):
      sys.stdout.flush()
      self.queue.append(data)

  def append(self, data):
    self.queue.append(data)
  
  def retornaProximo(self):
    if self.isEmpty():
      return 0
    try:
      return self.queue[0]
    except IndexError:
      sys.stdout.write("ERRO 1\n")
      sys.stdout.flush()
      return -1

  def retornaElemento(self, pos):
    if self.isEmpty():
      return 0
    try:
      return self.queue[pos]
    except IndexError:
      sys.stdout.write("ERRO 2\n")
      sys.stdout.flush()
      return -1

  def deletaElemento(self):
    del self.queue[0]

  def deletaPosicao(self, pos):
    del self.queue[pos]
