#!/usr/bin/env python3
#-*- coding: utf-8 -*-

import pygame

from punto import Punto

from variables import (TRAYECTORIA_COLOR, TRAYECTORIA_GROSOR)

class Trayectoria:
	"""Una Trayectoria representa la trayectoria de una partícula, almacenando
		los datos más relevantes de su movimiento: puntos en x e y, velocidades en esos puntos,
		y el tiempo en esos puntos.

	Attributes:
		puntos (:class: Dict[int, int]): las alturas registradas en la trayectoria.
		velocidades (:class: Dict[int, Vector]): las velocidades registradas en la trayectoria.
		tiempos: (:class: Dict[int, double]): Los tiempos regisrados en la trayectoria.
	"""

	def __init__(self):
		self._puntos = {}
		self._velocidades = {}
		self._tiempos = {}

	@property
	def puntos(self):
		return self._puntos

	@puntos.setter
	def puntos(self, value):
		self._puntos = value

	@property
	def velocidades(self):
		return self._velocidades

	@velocidades.setter
	def velocidades(self, value):
		self._velocidades = value

	@property
	def tiempos(self):
		return self._tiempos

	@tiempos.setter
	def tiempos(self, value):
		self._tiempos = value

	def mostrar(self):
		"""Imprime a el registro de todos los datos capturados en la trayectoria
		"""
		for k in self.puntos.keys():
			print("Punto x: ", k)
			print("\tAltura: ", self.puntos[k])
			print("\tVelocidad: ", self.velocidades[k])
			print("\tTiempo: ", self.tiempos[k])

	def add_punto(self, punto):
		"""Añade un punto a la trayectoria.
		Separa el punto en su coordenada en x y usa esta coordenada como la llave
		para el valor de su coordenada en y.

		Args:
			punto (:class: Punto): un punto para añadir a la trayectoria
		"""
		self.puntos[punto.x] = punto.y

	def registrar(self, punto, velocidad, tiempo):
		"""Registra un conjunto de variables a un punto en x específico.

		Args:
			punto (:class: Punto): un punto para añadir a la trayectoria.
			velocidad (:class: Vector): Una velocidad para añadir a la trayectoria.
			tiempo (:obj:double): Un tiempo para añadir a la trayectoria.

		"""
		self.puntos[punto.x] = punto.y
		self.velocidades[punto.x] = velocidad
		self.tiempos[punto.x] = tiempo

	def get_punto_y(self, punto_x):
		return self.puntos[punto_x]

	def get_velocidad(self, punto_x):
		return self.velocidades[punto_x]

	def get_tiempo(self, punto_x):
		return self.tiempos[punto_x]

	def clear(self):
		"""Borra todos los registros de la trayectoria
		"""
		self.puntos = {}
		self.velocidades = {}
		self.tiempos = {}

		
	def render(self, canvas):
		"""Renderiza cada punto en pantalla.
		Si la cantidad de puntos es grande, los puntos estarán tan juntos
		que parecerá una línea continua

		Args:
			canvas (:class: Canvas): El canvas donde dibujar la trayectoria.
		"""
		for punto_x, punto_y in self.puntos.items():
			pygame.draw.circle(canvas.superficie, TRAYECTORIA_COLOR, (punto_x, punto_y), TRAYECTORIA_GROSOR, 0)

