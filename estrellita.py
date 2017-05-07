# Alejandra Perez
# Python 3
# Jupyter notebook 
# numpy

import sys
import time
import random
import numpy as np

from copy import deepcopy
from valor_info_perfecta import *

#Declaracion de variables globales

#se va actualizando, se inicializa con 1/25 [5x5]
#matriz_probabilidades = [[1/25 for x in range(5)] for y in range(5)]
matriz_probabilidades = [[1/25, 1/25, 1/25, 1/25, 1/25],
                         [1/25, 1/25, 1/25, 1/25, 1/25],
                         [1/25, 1/25, 1/25, 1/25, 1/25],
                         [1/25, 1/25, 1/25, 1/25, 1/25],
                         [1/25, 1/25, 1/25, 1/25, 1/25]]

#Definicion de colores del sensor
colores = {
  "verde" : 0,
  "amarillo" : 1,
  "anaranjado" : 2,
  "rojo" : 3
}

#Probabilidades del sensor
sensor = [[0.70, 0.15, 0.1, 0.05],
         [0.17, 0.6, 0.17, 0.06],
         [0.06, 0.17, 0.6, 0.17],
         [0.05, 0.12, 0.23, 0.6],
         [0.03, 0.07, 0.1, 0.8]]

#Definicion del tipo de accion que se puede realizar
DISPARAR = 1
OBSERVAR = 2
MOVER = 3

#Definicion de posibles movimientos en la accion MOVER de la estrellita
ARRIBA = 1
DERECHA = 2
ABAJO = 3
IZQUIERDA = 4

#Definicion de la puntuacion que se obtiene cuando se DISPARA
ACIERTO = 1
FALLO = 0

#variables
tipo_accion = [DISPARAR, OBSERVAR, MOVER]
accion_oponente = [[int], [int], [ARRIBA, DERECHA, ABAJO, IZQUIERDA]]
resultado = [ACIERTO, FALLO, "verde", "amarillo", "anaranjado", "rojo", none]
#va creciendo, columnas: Tipo_Accion, donde, resultado
tabla_historico_yo = [tipo_accion, parametro_accion, resultado]
#va creciendo, columnas: Tipo_Accion, resultado
tabla_historico_oponente = [tipo_accion, resultado]

self.jugador = 0
self.mi_posicion = 0 # Donde esta mi estrella

#metodo de juego del agente
def agente_jugar(self, jugador, tipo_accion, accion_oponente, resultado, mi_posicion):
  #Cuando hay un resultado anterior de la jugada de mi agente
  if resultado is None:
    #Registro el resultado en el histórico que tengo
    tabla_historico_yo[-1].resultado = resultado
  if tabla_historico_yo == [] and accion_oponente == []:
    #Primera jugada de la partida
    #Puede ser cualquier casilla
    casilla_a_censar = random.randrange(1,25)
    registrar_Historico_Usuario(tabla_historico_yo, 2, casilla_a_censar)
    #Retornar censo aleatorio
    return [2, casilla_a_censar]
  #No soy el primero
  elif accion_oponente != []:
    #Hay accion de oponente - registrar
    registrar_Historico_Oponente(tabla_historico_oponente, accion_oponente[0], accion_oponente[1], accion_oponente[2])
    #Revisar si corremos
    if estamos_en_peligro(tabla_historico_oponente): #verificar ultima jugada oponente Hard
      #Corran Corran!
      casilla_a_mover =  correr_de_aqui(mi_posicion, tabla_historico_oponente) #ML
      registrar_Historico_Usuario(tabla_historico_yo, 3, casilla_a_mover)
      return [3, casilla_a_mover]
    elif resultado == ACIERTO and accion_oponente[0] != 3:
      #Si ya le di y no se movio - como a rata - como a cajón que no cierra
      casilla_de_ataque = tabla_historico_yo[-1][1]
      registrar_Historico_Usuario(tabla_historico_yo, 1, casilla_de_ataque)
      return [1, casilla_de_ataque]
    #Reviso si puedo atacar
    elif indicio_donde_atacar(tabla_historico_yo, tabla_historico_oponente): #Hard
      #Atacar
      casilla_de_ataque = obtener_casilla_ataque(tabla_historico_yo, tabla_historico_oponente) #ML
      registrar_Historico_Usuario(tabla_historico_yo, 1, casilla_de_ataque)
      return [1, casilla_de_ataque]
    else:
      #Censar
      casilla_a_censar2 = censar(tabla_historico_yo, tabla_historico_oponente, matriz_probabilidades) #ML puede ser logica
      registrar_Historico_Usuario(tabla_historico_yo, 2, casilla_a_censar2)
      return [2, casilla_a_censar2]

    #Prioridad defensa

#Obtener casilla para censar
def censar(tabla_historico_yo, tabla_historico_oponente, matriz_probabilidades):
  #censos que me sirven para triangular
  lista_censos = obtener_lista_censos_disponibles_antes_jugada(tabla_historico_yo, tabla_historico_oponente)
  #actualizar matriz probabilidades
  for i in range(0, matriz_probabilidades.length):
    for j in range(matriz_probabilidades.length, i):
      k = 0
      continuar = True
      while k < lista_censos.length() and continuar:
        #Cuadrante donde no estan
        if lista_censos(k)[2] == "anaranjado" or lista_censos(k)[2] == "rojo":
          if esta_zona_peligro(((i*5)+j+1),lista_censos(k))
            matriz_probabilidades[i][j] = 0
            #esta cerca
            else: 
            matriz_probabilidades[i][j] = 1
            continuar = False
      ++k
    #obtener cuantos 1s hay en la matriz
    cantidad_disponibles_censo= contar_unos(matriz_probabilidades)
    #Actualizar matriz valores fraccionarios
    asignar_probabilidad_positiva(matriz_probabilidades,cantidad_disponibles_censo)

    lista_numeros = convertir_a_lista_numeros(matriz_probabilidades) #convierte los que no son 0 a numero y retorna en lista
    #un aleatorio de la lista
    return obtener_aleatorio_de_lista(lista_numeros)