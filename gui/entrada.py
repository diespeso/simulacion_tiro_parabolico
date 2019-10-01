#!/usr/bin/env python3

import pygame
import thorpy

from collections import OrderedDict

class GUI:

	def __init__(self, **args):
		self._entradas = []
		self._etiquetas = []
		if 'entradas' in args:
			for entrada in args['entradas']:
				self._entradas.append(entrada)
		if 'etiquetas' in args:
			for etiqueta in args['etiquetas']:
				self._etiquetas.append(etiqueta)

	@property
	def entradas(self):
		return self._entradas

	@property
	def etiquetas(self):
		return self._etiquetas


	def add_entrada(self, entrada):
		self._entradas.append(entrada)

	def add_etiqueta(self, etiqueta):
		self._etiqueta.append(etiqueta)

	def update(self, evento):
		pass #renderizar cada entrada y cada etiqueta


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
			print(k, ": ", self._valores[k])
	
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

		if 'entradas' in args:
			for entrada in args['entradas']:
				self._inserters[entrada] = thorpy.Inserter(entrada + ": ")
				self._valores[entrada] = None

			self._boton = thorpy.make_button('Aceptar', func=self.leer)
			elementos = [ v for v in self._inserters.values()]
			print(type(elementos))
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

	ventana = Ventana((600, 400))
	canvas = Canvas((600, 300), (0, 100))
	particula = Particula()
	canvas.add_particula(particula, 0)
	ventana.add_canvas(canvas, "0")
	ventana.run()