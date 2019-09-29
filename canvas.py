#!/usr/bin/env python3

import pygame

class Canvas:
	"""
		una subventana para renderizar lo que se quiera
		un canvas no sirve de nada hasta que se añade
		a una ventana.
	"""

	def __init__(self, tamano, origen, background=(0,255,0)):
		self.tamano = tamano
		self.origen = origen
		self.pantalla = None
		self.superficie = pygame.Surface(tamano)
		self.ratio_vertical = 0.60 #ajusta la proporción vertical
		self.ratio_horizontal = 0.5 #no es relevante al final
		self.background = background

	def get_superficie(self):
		return self.superficie

	def update(self):
		"""
			renderiza el canvas, coloreando el fondo
			y renderizando en sí mismo a la superficie
			que tenga.
		"""
		self.superficie.fill(self.background)
		self.pantalla.blit(self.superficie, self.origen)

	def get_tamano_lista(self):
		#muestra el tamano en forma de array []
		width, height = self.tamano
		return [width, height]



#----PRUEBAS
if __name__ == '__main__':
	from ventana import Ventana
	v = Ventana((600, 400))
	canvas = Canvas((600, 200), (0, 10))
	v.add_canvas(canvas, "0")
	v.run()

