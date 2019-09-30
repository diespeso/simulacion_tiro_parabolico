import pygame

from punto import Punto

class Trayectoria:

	def __init__(self):
		self.puntos = {}

	def add_punto(self, punto):
		self.puntos[punto.x] = punto.y
		
	def render(self, canvas):
		for punto_x, punto_y in self.puntos.items():
			pygame.draw.circle(canvas.superficie, (100, 50, 250), (punto_x, punto_y), 1, 0)

