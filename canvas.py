#!/usr/bin/env python3

import pygame

from particula import Particula

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
		self.particulas = {}

	def get_superficie(self):
		return self.superficie

	def add_particula(self, particula, id):
		particula.canvas = self
		self.particulas[id] = particula

	def update(self):
		"""
			renderiza el canvas, coloreando el fondo
			y renderizando en sí mismo a la superficie
			que tenga.
		"""
		self.superficie.fill(self.background)
		self.pantalla.blit(self.superficie, self.origen)
		for particula in self.particulas.values():
			if particula.tiempo_transcurrido < particula.tiempo_total:
				particula.simular()
			pygame.draw.circle(self.superficie, (255, 100, 50), (int(particula.posicion.x), int(particula.posicion.y)), 4, 0)
			particula.trayectoria.render(self)
			if(not particula.is_simulando):
				self.render_trayectoria(0)
				pos_x = pygame.mouse.get_pos()[0]
				
	

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

