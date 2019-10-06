#!/usr/bin/env python3
#-*- coding: utf-8 -*-

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
	"""Estado representa el estado de una partícula, los valores posibles son:
		SIN_LANZAR
		EN_MOVIMIENTO
		TERMINADO
	"""
	SIN_LANZAR = 0
	EN_MOVIMIENTO = 1
	TERMINADO = 2

class Particula:
	"""Representa un proyectil que describe una trayectoria parabólica.

	Attributes:
		posicion (:class: Punto): Representa el punto donde se encuentra
		velocidad (:class: Vector): El vector de la velocidad que la está
			moviendo
		gravedad (:class: Vector): El vector de la aceleración que ejerce
			la fuerza de gravedad.
		velocidad_inicial (:class: Vector): La velocidad de lanzamiento
		tiempo_transcurrido (:obj: int): El tiempo que lleva desde el lanzamiento
		tiempo_total (:obj: int): el tiempo que tomará en caer al suelo.
		altura_maxima (:obj: int): la altura máxima que alcanzará.
		distancia_recorrida (:obj: int): La disntancia horizontal total que recorrerá.
		delta_tiempo (:obj: int): El tiempo que transcurre entre cada vez que se registran
			los datos de la partícula en su trayectoria.
		trayectoria (:class: Trayectoria): La trayectoria que describe la simulación
			del tiro de esta partícula.
		estado (:class: Estado): el estado de la partícula.
		canvas (:class: Canvas): el canvas donde ocurre y se dibuja la simulación del
			tiro.
		color (:obj: (int, int, int)): El color del círculo que representa a la partícula.
		radio (:obj: int): El radio del círculo que representa a la partícula.
	"""

	def __init__(self):
		self._posicion = Punto(0, 0)
		self._velocidad = Vector(x=0, y=0)
		self._gravedad = Vector(modulo=9.8, angulo=270)
		self._velocidad_inicial = Vector(x=0, y=0)
		self._tiempo_transcurrido = 0
		self._tiempo_total = 0
		self._altura_maxima = 0
		self._distancia_recorrida = 0

		self._delta_tiempo = 0.02

		self._trayectoria = Trayectoria()

		self._estado = Estado.SIN_LANZAR

		self._canvas = None

		self._color = PARTICULA_COLOR
		self._radio = PARTICULA_RADIO

	@property
	def posicion(self):
		return self._posicion

	@posicion.setter
	def posicion(self, value):
		self._posicion = value

	@property
	def velocidad(self):
		return self._velocidad

	@velocidad.setter
	def velocidad(self, value):
		self._velocidad = value

	@property
	def gravedad(self):
		return self._gravedad

	@gravedad.setter
	def gravedad(self, value):
		self._gravedad = value

	@property
	def velocidad_inicial(self):
		return self._velocidad_inicial

	@velocidad_inicial.setter
	def velocidad_inicial(self, value):
		self._velocidad_inicial = value

	@property
	def tiempo_transcurrido(self):
		return self._tiempo_transcurrido

	@tiempo_transcurrido.setter
	def tiempo_transcurrido(self, value):
		self._tiempo_transcurrido = value

	@property
	def tiempo_total(self):
		return self._tiempo_total

	@tiempo_total.setter
	def tiempo_total(self, value):
		self._tiempo_total = value

	@property
	def altura_maxima(self):
		return self._altura_maxima

	@altura_maxima.setter
	def altura_maxima(self, value):
		self._altura_maxima = value

	@property
	def distancia_recorrida(self):
		return self._distancia_recorrida

	@distancia_recorrida.setter
	def distancia_recorrida(self, value):
		self._distancia_recorrida = value

	@property
	def delta_tiempo(self):
		return self._delta_tiempo

	@delta_tiempo.setter
	def delta_tiempo(self, value):
		self._delta_tiempo = value

	@property
	def trayectoria(self):
		return self._trayectoria

	@trayectoria.setter
	def trayectoria(self, value):
		self._trayectoria = value

	@property
	def estado(self):
		return self._estado

	@estado.setter
	def estado(self, value):
		self._estado = value

	@property
	def canvas(self):
		return self._canvas

	@canvas.setter
	def canvas(self, value):
		self._canvas = value

	@property
	def color(self):
		return self._color

	@color.setter
	def color(self, value):
		self._color = value

	@property
	def radio(self):
		return self._radio

	@radio.setter
	def radio(self, value):
		self._value = value

	def __str__(self): 
		return ("Tiempo total: {0:.2f}s, Altura máxima: {1:.2f}m").format(
			self.tiempo_total, self.altura_maxima)

	def lanzar(self, velocidad, angulo):
		"""Comienza la simulación, lanzando esta partícula con la velocidad y ángulo dados.
		"""
		if self.canvas == None:
			raise "No se asignó canvas"


		self.estado = Estado.EN_MOVIMIENTO
		self.velocidad_inicial = Vector(modulo=velocidad, angulo=angulo)
		self.velocidad = self.velocidad_inicial
		self.tiempo_total = (-self.velocidad_inicial.get_vector_y().get_modulo()
			/ self.gravedad.get_repr_y()) * 2
		#calcula las variables finales del tiro desde el principio
		self.altura_maxima = (self.velocidad_inicial.get_vector_y().get_modulo()
			* self.tiempo_total / 2.0) + (self.gravedad.get_repr_y() * math.pow(self.tiempo_total / 2, 2.0)) / 2
		self.distancia_recorrida = self.velocidad_inicial.get_vector_x().escalar(self.tiempo_total).get_modulo()
		
		self.simular()

	def simular(self):
		"""Cada vez que se llama, actualiza el estado de la partícula, usando las fórmulas
		del movimiento parabólico
		"""

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

		#grafica los vectores que componen el movimiento de la partícula
		VectorGrafico(self.posicion, self.velocidad).render(superficie=self.canvas.superficie,
			color=PARTICULA_VECTOR_COLOR, grosor=PARTICULA_VECTOR_X_GROSOR) #usar mismo grosor que en x
		VectorGrafico(self.posicion, self.velocidad.get_vector_x()).render(superficie=self.canvas.superficie, 
			color=PARTICULA_VECTOR_X_COLOR, grosor=PARTICULA_VECTOR_X_GROSOR)
		VectorGrafico(self.posicion, self.velocidad.get_vector_y()).render(superficie=self.canvas.superficie,
			color=PARTICULA_VECTOR_Y_COLOR, grosor=PARTICULA_VECTOR_Y_GROSOR)

		if(self.tiempo_transcurrido >= self.tiempo_total):
			self.estado = Estado.TERMINADO

	def clear(self):
		"""Reinicia las propiedades que pueden cambiar, es decir, las que son relevantes a la simulación.
		por lo que no reinicia el canvas. Sirve para poder volver a lanzar la partícula varias veces en
		la misma corrida del programa.
		"""
		self.posicion = Punto(0, 0)
		self.velocidad = Vector(x=0, y=0)
		self.gravedad = Vector(modulo=9.8, angulo=270)
		self.velocidad_inicial = Vector(x=0, y=0)
		self.tiempo_transcurrido = 0
		self.tiempo_total = 0
		self.altura_maxima = 0
		self.distancia_recorrida = 0
		self.estado = Estado.SIN_LANZAR

if __name__ == '__main__':
	particula = Particula()
	particula.lanzar(80, 30)
	print(particula)
