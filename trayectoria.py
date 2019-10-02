import pygame

from punto import Punto

from variables import (TRAYECTORIA_COLOR, TRAYECTORIA_GROSOR)

class Trayectoria:
	"""
		Representa la trayectoria de una partícula, almacenando
		los datos más relevantes de su movimiento.
	"""

	def __init__(self):
		self.puntos = {}
		self.velocidades = {}
		self.tiempos = {}

	def mostrar(self):
		for k in self.puntos.keys():
			print("Punto x: ", k)
			print("\tAltura: ", self.puntos[k])
			print("\tVelocidad: ", self.velocidades[k])
			print("\tTiempo: ", self.tiempos[k])

	def add_punto(self, punto):
		self.puntos[punto.x] = punto.y

	def registrar(self, punto, velocidad, tiempo):
		self.puntos[punto.x] = punto.y
		self.velocidades[punto.x] = velocidad
		self.tiempos[punto.x] = tiempo

	def get_punto_y(self, punto_x):
		return self.puntos[punto_x]

	def get_velocidad(self, punto_x):
		return self.velocidades[punto_x]

	def get_tiempo(self, punto_x):
		return self.tiempos[punto_x]

		
	def render(self, canvas):
		for punto_x, punto_y in self.puntos.items():
			pygame.draw.circle(canvas.superficie, TRAYECTORIA_COLOR, (punto_x, punto_y), TRAYECTORIA_GROSOR, 0)

