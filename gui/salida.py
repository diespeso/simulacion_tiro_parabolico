import pygame
import thorpy

from collections import OrderedDict

class Salida:

	def __init__(self, **args):
		COLOR = (0, 0, 0)
		TFUENTE = 10

		self._elementos = args['elementos']
		self._etiquetas = OrderedDict()
		if 'elementos' in args:
			self._elementos = args['elementos']
			for elemento in args['elementos']:
				self._etiquetas[elemento] = thorpy.make_text(elemento, TFUENTE, COLOR)

		if 'particula' in args:
			self._particula = args['particula']
		else:
			self._particula = None

		if 'posicion' in args:
			posicion = args['posicion']
		else:
			posicion = (150, 0)

		if 'tamano' in args:
			tamano = args['tamano']
		else:
			tamano = (500, 200)

		self._caja = thorpy.Box(elements=[e for e in self._etiquetas.values()],
			size=tamano)
		self._caja.set_topleft(posicion)
		self._caja.blit()
		self._caja.update()

		self._menu = thorpy.Menu()
		self._menu.add_to_population(self._caja)

	def update(self, **args):
		if 'salidas' in args:
			for etiqueta, salida in zip(self._etiquetas.keys(), args['salidas']):
				texto = etiqueta + ": {}"
				self._etiquetas[etiqueta].set_text(texto.format(str(salida)))

	def render(self):
		self._menu.refresh_population()
		self._menu.blit_and_update()



