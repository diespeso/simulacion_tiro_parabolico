#!/usr/bin/env python3

import pygame

pygame.init()

class Ventana:
	#clase de utilería para abrir una ventana y renderizar
	def __init__(self, tamano, background=(255, 255, 255)):
		self.tamano = tamano
		self.superficie = pygame.display.set_mode(tamano)
		self.background = background
		self.canvas = {}

	def get_superficie(self):
		return self.superficie

	def get_altura(self):
		return self.tamano[1]

	def get_anchura(self):
		return self.tamano[0]

	def add_canvas(self, canvas, nombre):
		canvas.pantalla = self.superficie
		self.canvas[nombre] = canvas

	def add_particula(self, particula, id):
		self.particulas[id] = particula

	def run(self):
		activo = True
		while activo:
			for evento in pygame.event.get():
				if(evento.type == pygame.QUIT):
					activo = False
			self.display()

	def display(self):
		self.superficie.fill(self.background)
		for c in self.canvas.values():
			c.update()
			self.superficie.blit(c.get_superficie(), c.origen)


		pygame.display.flip()


if __name__ == '__main__':
	ventana = Ventana((600, 400), (255, 0, 150))
	ventana.run()