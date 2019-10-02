#!/usr/bin/evn python3

from vector import Vector
from punto import Punto
import punto
from trayectoria import Trayectoria
import math
import pygame

from vector_grafico import VectorGrafico

from variables import (PARTICULA_COLOR, PARTICULA_RADIO, PARTICULA_VECTOR_COLOR,
	PARTICULA_VECTOR_X_COLOR, PARTICULA_VECTOR_Y_COLOR, PARTICULA_VECTOR_X_GROSOR, PARTICULA_VECTOR_Y_GROSOR)

from enum import Enum 

class Estado(Enum):
	SIN_LANZAR = 0
	EN_MOVIMIENTO = 1
	TERMINADO = 2

class Particula:
	"""
		Representa a un objeto que describe una
		trayectoria parabólica
	"""

	def __init__(self):
		self.posicion = Punto(0, 0)
		self.velocidad = Vector(x=0, y=0)
		self.gravedad = Vector(modulo=9.8, angulo=270)
		self.velocidad_inicial = Vector(x=0, y=0)
		self.tiempo_transcurrido = 0
		self.tiempo_total = 0
		self.altura_maxima = 0
		self.distancia_recorrida = 0

		self.delta_tiempo = 0.02

		self.trayectoria = Trayectoria()

		self.estado = Estado.SIN_LANZAR

		self.canvas = None

		self.color = PARTICULA_COLOR
		self.radio = PARTICULA_RADIO

	def __str__(self): 
		return ("Tiempo total: {0:.2f}s, Altura máxima: {1:.2f}m").format(
			self.tiempo_total, self.altura_maxima)

	def lanzar(self, velocidad, angulo):
		if self.canvas == None:
			raise "No se asignó canvas"

		self.estado = Estado.EN_MOVIMIENTO
		self.velocidad_inicial = Vector(modulo=velocidad, angulo=angulo)
		print(self.velocidad_inicial)
		self.velocidad = self.velocidad_inicial
		self.tiempo_total = (-self.velocidad_inicial.get_vector_y().get_modulo()
			/ self.gravedad.get_repr_y()) * 2
		self.altura_maxima = (self.velocidad_inicial.get_vector_y().get_modulo()
			* self.tiempo_total / 2.0) + (self.gravedad.get_repr_y() * math.pow(self.tiempo_total / 2, 2.0)) / 2
		self.distancia_recorrida = self.velocidad_inicial.get_vector_x().escalar(self.tiempo_total).get_modulo()
		
		self.simular()

	def simular(self):

		#primero obtener las componentes de la velocidad.
		resultante_x = Vector(x=self.velocidad_inicial.get_vector_x().get_modulo(), y=0)
		cambio_y = self.gravedad.get_repr_y() * self.tiempo_transcurrido
		resultante_y = Vector(x= 0, y=cambio_y + self.velocidad_inicial.get_vector_y().get_repr_y())

		#hacer un vector con ambas componentes
		self.velocidad = resultante_x.sumar(resultante_y) #OPERACIÓN VECTORIAL: SUMA DE VECTORES

		#primero obtener las componentes de la velocidad utilizando escalamiento
		posicion_x = self.velocidad_inicial.get_vector_x().escalar(self.tiempo_transcurrido) #OPERACIÓN VECTORIAL: ESCALAMIENTO DE VECTORES
		delta_y = Vector(x=0, y = ((self.gravedad.get_repr_y() * math.pow(self.tiempo_transcurrido, 2.0)) / 2))
		#crear un vector sumando ambas componentes
		posicion_y = self.velocidad_inicial.get_vector_y().escalar(self.tiempo_transcurrido).sumar(delta_y)	

		#convertir el vector a un punto en el espacio para la trayectoria.    
		self.posicion = punto.from_vector_int(posicion_x.sumar(posicion_y))
		self.trayectoria.registrar(self.posicion, self.velocidad, self.tiempo_transcurrido)
		self.tiempo_transcurrido += self.delta_tiempo

		VectorGrafico(self.posicion, self.velocidad).render(superficie=self.canvas.superficie,
			color=PARTICULA_VECTOR_COLOR, grosor=PARTICULA_VECTOR_X_GROSOR) #usar mismo grosor que en x
		VectorGrafico(self.posicion, self.velocidad.get_vector_x()).render(superficie=self.canvas.superficie, 
			color=PARTICULA_VECTOR_X_COLOR, grosor=PARTICULA_VECTOR_X_GROSOR)
		VectorGrafico(self.posicion, self.velocidad.get_vector_y()).render(superficie=self.canvas.superficie,
			color=PARTICULA_VECTOR_Y_COLOR, grosor=PARTICULA_VECTOR_Y_GROSOR)

		if(self.tiempo_transcurrido >= self.tiempo_total):
			self.estado = Estado.TERMINADO
			#self.trayectoria.mostrar()

	def get_velocidad_actual(self, posicion_x):
		return self.velocidad

	def get_posicion_actual(self, posicion_x):
		return self.posicion

if __name__ == '__main__':
	particula = Particula()
	particula.lanzar(80, 30)
	print(particula)
