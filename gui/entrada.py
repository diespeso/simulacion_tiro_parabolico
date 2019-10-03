#!/usr/bin/env python3

import pygame
import thorpy

from collections import OrderedDict

class Salida:
	"""
		Clase para mostrar las características de una partícula
	"""

	def __init__(self, particula):
		self._particula = particula
		self.distancia = "Distancia: {}m"
		self.altura = "Altura: {}m"
		self.velocidad = "Velocidad: {}"
		self.velocidad_x = "Velocidad horizontal: {}"
		self.velocidad_y = "Velocidad vertical: {}"
		self.tiempo = "Tiempo {:.2f}"

		COLOR = (0, 0, 0)
		TFUENTE = 10

		self.distancia_et = thorpy.make_text("Distancia: ", TFUENTE, COLOR)
		self.altura_et = thorpy.make_text("Altura: ", TFUENTE, COLOR)
		self.velocidad_et = thorpy.make_text("Velocidad: ", TFUENTE, COLOR)
		self.velocidad_x_et = thorpy.make_text("Velocidad h: ", TFUENTE, COLOR)
		self.velocidad_y_et = thorpy.make_text("Velocidad v: ", TFUENTE, COLOR)
		self.tiempo_et = thorpy.make_text("Tiempo: ", TFUENTE, COLOR)

		self.caja = thorpy.Box(elements=[self.distancia_et, self.altura_et, self.velocidad_et,
			self.velocidad_x_et, self.velocidad_y_et, self.tiempo_et], size=(500, 200))
		self.caja.set_topleft((200, 0))

		self.caja.blit()
		self.caja.update()

		self.menu = thorpy.Menu()
		self.menu.add_to_population(self.caja)

	def update(self):
		pos_x = pygame.mouse.get_pos()[0]
		if(pos_x in self._particula.trayectoria.puntos.keys()):
			self.distancia_et.set_text(self.distancia.format(pos_x))
			self.altura_et.set_text(self.altura.format(self._particula.trayectoria.get_punto_y(pos_x)))
			self.velocidad_et.set_text(self.velocidad.format(self._particula.trayectoria.get_velocidad(pos_x)))
			self.tiempo_et.set_text(self.tiempo.format(self._particula.trayectoria.get_tiempo(pos_x)))
			self.velocidad_x_et.set_text(self.velocidad_x.format(self._particula.trayectoria.get_velocidad(pos_x).get_vector_x()))
			self.velocidad_y_et.set_text(self.velocidad_y.format(self._particula.trayectoria.get_velocidad(pos_x).get_vector_y()))

	def render(self):
		self.menu.refresh_population()
		self.menu.blit_and_update()



class Entrada:
	"""
		Un conjunto de Inserters para realizar entrada
		con un sólo boton para obtener todas las entradas.
	"""

	def leer(self):
		"""
			Lee todas las entradas y asigna los valores al dicionario de valores
		"""
		for k in self._inserters.keys():
			self._valores[k] = self._inserters[k].get_value()
		self._activado = True
	
	def __init__(self, **args):
		"""
			crea los campos de inserción, el botón y el menú que los agrupa
		"""
		self._inserters = OrderedDict()
		self._boton = None
		self._valores = OrderedDict()
		self._superficie = None
		self._menu = thorpy.Menu()
		self._caja = None
		self._activado = False

		if 'entradas' in args:
			for entrada in args['entradas']:
				self._inserters[entrada] = thorpy.Inserter(entrada + ": ")
				self._valores[entrada] = None

			self._boton = thorpy.make_button('Aceptar', func=self.leer)
			elementos = [ v for v in self._inserters.values()]
			elementos.append(self._boton)
			self._caja = thorpy.Box(elements=elementos)
			self._boton.set_topleft((50, 50))
			#self._caja.add_elements([self._boton])
			self._caja.blit()
			self._caja.update()
			self._menu.add_to_population(self._caja)
				

		if 'func' in args:
			 # mejor usa mi propia función
			 pass


	@property
	def valores(self):
		return self._valores

	@property
	def superficie(self):
		return self._superficie

	@superficie.setter
	def superficie(self, value):
		for v in self._inserters.values:
			v.surface = value
		self._superficie = superficie
		self._boton.surface = superficie

	def update(self, event):
		self._menu.react(event)

	def render(self):
		self._menu.refresh_population()
		self._menu.blit_and_update()


if __name__ == '__main__':
	from canvas import Canvas
	from ventana import Ventana 
	from vector import Vector
	from particula import Particula

	import pygame

	ventana = Ventana((800, 600))
	canvas = Canvas((800, 400), (0, 200))
	particula = Particula()
	canvas.add_particula(particula, 0)
	ventana.add_canvas(canvas, "0")

	salida = Salida(particula)
	ventana.run()