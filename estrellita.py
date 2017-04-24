#tablero = []

#haremos en una cuadrícula de 5 x 5 de todas las "O" es del "océano".
#agregará cinco "O"es, que es la base para crear nuestra fila. Esto lo haremos cinco veces para crear cinco filas. (Como tenemos que hacerlo cinco veces, parece que sería apropiado usar un bucle.)

#tablero.append(["O"] * 5)
#print tablero

import random

tablero = []

for x in range(0,5):
  tablero.append(["O"] * 5)

def print_tablero(tablero):
  for fila in tablero:
    print ' '.join(fila)

print "Juguemos as la batalla naval!"
print_tablero(tablero)

def fila_aleatoria(tablero):
  return random.randint(0,len(tablero)-1)

def columna_aleatoria(tablero):
  return random.randint(0,len(tablero[0])-1)

barco_fila = fila_aleatoria(tablero)
barco_columna = columna_aleatoria(tablero)

#¡De acá en adelante todo debería ir en tu ciclo for!
#¡Asegurate de indentar!
for turno in range(4):
    print 'Turno ',turno+1
    adivina_fila = input("Adivina fila: ")
    adivina_columna = input("Adivina columna: ")
    
    if adivina_fila == barco_fila and adivina_columna == barco_columna:
      print "Felicitaciones! Hundiste mi barco!"
      break
    else:
      if (adivina_fila < 0 or adivina_fila > 4) or (adivina_columna < 0 or adivina_columna > 4):
        print "Huy, eso ni siquiera esta en el oceano."
      elif(tablero[adivina_fila][adivina_columna] == "X"):
        print "Ya dijiste esa."
      else:
      	print "No tocaste mi barco!"
      	tablero[adivina_fila][adivina_columna] = "X"
      print_tablero(tablero)
      if turno == 3:
        print "Fin del juego"   