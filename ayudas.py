
def traducir_posicion(i, j):
  return i*5+j+1

def traducir_posicion(num):
  num -= 1
  j = (num%5)
  i = num//5
  return (i,j)

def imprimir_matriz(matriz):
  for x in matriz:
    for y in x:
      print(y, end=" ")
      print("")

#PRINCIPAL
class Agente_AlejandraPerez_YeisonOsorio(object):

  def __init__(self, jugador):
    super(Agente_AlejandraPerez_YeisonOsorio, self).__init__()
    self.jugador = jugador
    self.tableroPropio = [[0 for x in range(5)] for y in range (5)]
    self.tableroOponente = [[1/25 for x in range(5)] for y in range(5)]
    self.ultimaAccion = None

  def jugar(self, resultado_accion, accion_oponente, estrellita):
    self.colocar_estrellita(estrellita)
    self.actualizar_datos(resultado_accion)
    self.actualizar_oponente(accion_oponente)

  def jugar_sensor(self, sensor):
    pass

  def colocar_estrellita(self, estrellita):
    i, j = traducir_posicion(estrellita)
    self.tableroPropio[i][j] = 1

  def actualizar_oponente(accion_oponente):
    tipoAccion, parametroAccion, resultado = accion_oponente
    if tipoAccion == DISPARAR:
      pass
    elif tipoAccion == OBSERVAR:
      pass
    elif tipoAccion == MOVER:
      pass

  def actualizar_datos(self.resultado_accion):
    if self.ultimaAccion == DISPARAR:
      if resultado_accion == ACIERTO: # Se reestablecen las probabilidades
        self.tableroOponente = [[1/25 for x in range(5)] for y in range(5)]
      elif resultado_accion == FALLO: #Bajar las probabilidades a cero
        i,j = self.ultimoAtaque
        self.tableroOponente[i][j] = 0

    elif self.ultimaAccion == OBSERVAR:
      self.actualizar_probabilidades(resultado_accion)

    elif self.ultimaAccion == MOVER:
      pass

  def actualizar_probabilidades(self, resultado_accion):
      pass
      
if __name__ == '__main__':
  a = Agente_AlejandraPerez_YeisonOsorio(1)
  a.jugar(None,[1,24,3],12)
  imprimir_matriz(a.tableroPropio)

#Hallar el tiempo de ejecucion
start = time.time()
cont = 0
for i in range(0,1000000):
    cont += 1
end = time.time()
print(end-start)