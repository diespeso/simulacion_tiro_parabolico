#!/usr/bin/env python3
#-*- coding: utf-8 -*-

import pygame

from particula import Particula
from particula import Estado
from punto import Punto

from variables import SIMULACION_FONDO_COLOR
from variables import (PARTICULA_VECTOR_X_COLOR, PARTICULA_VECTOR_Y_COLOR,
	PARTICULA_VECTOR_X_GROSOR, PARTICULA_VECTOR_COLOR,
	PARTICULA_MOVIL_COLOR)
from vector_grafico import VectorGrafico

class Canvas:
	"""Canvas representa un lienzo donde ocurre la simulación física.

	Args:
		tamano (int, int): una tupla (ancho, alto) para las
			dimensiones
		origen (int, int): una tupla (x, y) un punto x, y
			donde se posicionará la esquina superior izquierda
			del Canvas

	Attributes:
		tamano (:obj: (int, int)): dimensiones del Canvas
		origen (:obj: (int, int)): origen de la esquina superior
			izquieda del Canvas
		pantalla (:class: Ventana, optional): La Ventana donde
			vive el Canvas.
		superficie (:class: pygame.Surface): La superficie donde
			se dibuja el canvas.
		ratio_verticual (:obj: float): ajusta la propoción vertical
			(no usado)
		ratio_horizontal (:obj: float): ajusta la proporción horizontal
			(no usado)
		background: (:obj: (int, int, int)): El color de fondo.
		particulas: (:dict: {int, Particula}): La colección de partículas
			que existen en el Canvas
			Note: Para este programa solo existe una partícula
	"""

	def __init__(self, tamano, origen):
		self._tamano = tamano
		self._origen = origen
		self._pantalla = None
		self._superficie = pygame.Surface(tamano)
		self.ratio_vertical = 0.60 #ajusta la proporción vertical (no usado)
		self.ratio_horizontal = 0.5 #no es relevante al final (no usado)
		self._background = SIMULACION_FONDO_COLOR
		self._particulas = {}

	@property
	def tamano(self):
		"""
		Returns:
			(int, int): dimensiones (alto, ancho)
		"""
		return self._tamano

	@tamano.setter
	def tamano(self, value):
		"""
		Args:
			value ((int, int)): dimensiones (alto, ancho)
		"""
		self._taano = value

	@property
	def origen(self):
		"""
		Returns:
			(int, int): Posición (x, y) de la esquina superior izquierda
		"""
		return self._origen

	@origen.setter
	def origen(self, value):
		"""
		Args:
			value ((int, int)): Posición (x, y) de la esquina superior izquierda
		"""

	@property
	def pantalla(self):
		return self._pantalla

	@pantalla.setter
	def pantalla(self, value):
		self._pantalla = value

	@property
	def superficie(self):
		return self._superficie

	@superficie.setter
	def superficie(self, value):
		self._superficie = value

	@property
	def background(self):
		return self._background

	@background.setter
	def background(self, value):
		self._background = value

	@property
	def particulas(self):
		return self._particulas

	@particulas.setter
	def particulas(self, value):
		self._particulas = value

	def add_particula(self, particula, id):
		""" Añade la partícula dada al diccionario, con la llave de la id dada
		Args:
			particula (Particula): La partícula a añadir
			id (int): La llave a relacionar con la Partícula dada
		"""
		particula.canvas = self
		self.particulas[id] = particula

	def update(self):
		"""Renderiza el canvas, y avanza en la simulación.
		"""
		self.superficie.fill(self.background) #pinta el fondo
		self.pantalla.blit(self.superficie, self.origen) #pinta este canvas en la superficie de la ventana.
		for particula in self.particulas.values():
			if particula.tiempo_transcurrido < particula.tiempo_total: #si aún no ha caido al suelo
				particula.simular()
			particula.trayectoria.render(self)
			#dibuja la partícula en movimiento
			pygame.draw.circle(self.superficie, particula.color, (int(particula.posicion.x), int(particula.posicion.y)), particula.radio, 0)
			if(particula.estado == Estado.TERMINADO):		#al terminar la simulación
				
				pos_x = pygame.mouse.get_pos()[0]
				if pos_x in particula.trayectoria.puntos.keys(): #cuando termina la simulación
					pos_y = particula.trayectoria.puntos[pos_x]
					#renderizando el punto tomando x del cursor y 'y' de la trayectoria
					pygame.draw.circle(self.superficie, PARTICULA_MOVIL_COLOR, (pos_x, pos_y), 3, 0)
					#renderizado de los vectores componentes
					vector = particula.trayectoria.velocidades[pos_x]

					#se renderizan los vectores de la partícula del mouse
					VectorGrafico(Punto(pos_x, pos_y), vector.get_vector_x()).render( #velocidad x
						superficie=self.superficie,
						color=PARTICULA_VECTOR_X_COLOR,
						grosor=PARTICULA_VECTOR_X_GROSOR)

					VectorGrafico(Punto(pos_x, pos_y), vector.get_vector_y()).render( #velocidad y
						superficie=self.superficie,
						color=PARTICULA_VECTOR_Y_COLOR,
						grosor=PARTICULA_VECTOR_X_GROSOR
					)

					VectorGrafico(Punto(pos_x, pos_y), vector).render(	#velocidad resultante
						superficie=self.superficie,
						color=PARTICULA_VECTOR_COLOR,
						grosor=PARTICULA_VECTOR_X_GROSOR
					)
		
		#acomoda la pantalla para que se vea bien el tiro
		self.superficie.blit(pygame.transform.rotate(self.superficie, 180), (0, 0))
		self.superficie.blit(pygame.transform.flip(self.superficie, True, False), (0, 0))	

#----PRUEBAS
if __name__ == '__main__':
	from ventana import Ventana
	v = Ventana((600, 400))
	canvas = Canvas((600, 200), (0, 10))
	v.add_canvas(canvas, "0")
	v.run()

