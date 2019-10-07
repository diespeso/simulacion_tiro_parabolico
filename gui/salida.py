#!/usr/bin/env python3
#-*- coding: utf-8 -*-

import pygame
import thorpy

from collections import OrderedDict

class Salida:
	""" Una Salida es un campo de GUI donde se muestran datos
	sobre la simulación o el tiro final.

	Attributes:
		elementos (:class: [str]): arreglo de str's que representan los idenfiticadores
			de la salida  
		etiquetas (:class: collections.OrderedDict[int, thorpy.Text]): Diccionario que contiene
			a los elementos de thorpy que imprimen el texto en pantalla
		caja (:class: thorpy.Box): La caja que contiene a los elementos de salida
		menu (:class: thorpy.Menu): El menu que contiene a los elementos en pantalla
		particula (:class: Particula): La particula de la cual obtener la información para
			la salida.
	"""

	def __init__(self, **args):
		COLOR = (0, 0, 0)
		TFUENTE = 10

		self._elementos = args['elementos']
		self._etiquetas = OrderedDict()
		if 'elementos' in args:
			self._elementos = args['elementos']
			#por cada elemento en el arreglo, hacer un texto y asignarselo a ese elemento
			for elemento in args['elementos']:
				self._etiquetas[elemento] = thorpy.make_text(elemento, TFUENTE, COLOR)

		#asinaciones específicas
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
			pass#tamano = (500, 200)

		self._caja = thorpy.Box(elements=[e for e in self._etiquetas.values()],
			size=tamano)
		self._caja.set_topleft(posicion)
		self._caja.blit()
		self._caja.update()

		self._menu = thorpy.Menu()
		self._menu.add_to_population(self._caja)

	def update(self, **args):
		"""Acualiza las salidas de texto en pantalla.
		Asumiendo que se ha enviado 'salidas' como argumento, por cada
		salida en 'salidas', se modifica el valor del texto en pantalla
		para el elemento que corresponda, para que su etiqueta tenga
		el valor enviado por la salida.
		"""
		self._caja.fit_children() #el tamaño cambia dinámicamente
		if 'salidas' in args:
			for etiqueta, salida in zip(self._etiquetas.keys(), args['salidas']):
				texto = etiqueta + ": {}" #para poder usar .format()
				self._etiquetas[etiqueta].set_text(texto.format(str(salida)))

	def render(self):
		"""Renderizar los elementos gráficos
		"""
		self._menu.refresh_population()
		self._menu.blit_and_update()



