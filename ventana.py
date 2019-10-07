#!/usr/bin/env python3
#-*- coding: utf-8 -*-

import pygame

from particula import Estado
from variables import MENU_FONDO_COLOR

from gui.entrada import Entrada
from gui.salida import Salida

pygame.init()

class Ventana:
	"""
	Ventana representa el lugar donde ocurre el programa
		
		Args:
			tamano(str): tupla de (ancho, largo)

		Attributes:
			superficie (:class: pygame.Surface): La superficie donde
				ocurre el renderizado 
			background (:obj: (int, int, int)): tupla de
				(rojo, verde, azul), el color del fondo
			canvas (:dict: {:class: str, :class: Canvas}):
				Diccionario que relaciona una string,
				"0", con un único canvas.
			entrada (:class: gui.Entrada): Una Entrada para introducir
				los datos del lanzamiento.
			salida (:class: gui.Salida): Una Salida para mostrar los datos
				de la partícula según la posición en x del mouse una vez
				que hay terminado la simulación.
			salida_estatica: (:class: gui.Salida): Una Salida para 
				mostrar los datos finales estáticos de la simulación
				una vez quehaya terminado. 

	"""
	def __init__(self, tamano):
		self.tamano = tamano
		self._superficie = pygame.display.set_mode(tamano)
		self.background = MENU_FONDO_COLOR
		self.canvas = {}

		self._entrada = Entrada(entradas=["velocidad", "angulo"])
		self._salida = Salida(elementos=["distancia", "altura",
			"velocidad", "velocidad x", "velocidad y",
			"tiempo"], tamano=(300, 200), posicion=(170, 0))
		self.salida_estatica = Salida(elementos=["tiempo total",
			"desplazamiento total", "altura maxima"], posicion=(470, 0), tamano=(250, 200))

		self.salida._caja.fit_children()
		self.salida_estatica._caja.fit_children()

	@property
	def superficie(self):
		"""
		Returns:
			pygame.Surface: La superficie
		"""
		return self._superficie

	@superficie.setter
	def superficie(self, value):
		"""
		Args:
			value (pygame.Surface): La superficie sobre la cual renderizar.
		"""
		self._superficie = value

	@property
	def entrada(self):
		"""
		Returns:
			gui.Entrada: El campo GUI de entrada
		"""
		return self._entrada

	@entrada.setter
	def entrada(self, value):
		"""
		Note: No se supone que se modifique, pero se incluye.

		Args:
			value (gui.Entrada): La entrada a mostrar para capturar
		"""
		self._entrada = value

	@property
	def salida(self):
		"""
		Returns:
			gui.Salida: El campo GUI de salida
		"""
		return self._salida

	@salida.setter
	def salida(self, value):
		"""
		Note: No se supone que se modifique, pero se incluye.
		
		Args:
			value (gui.Salida): La salida a mostrar
		"""
		self._salida = value

	def get_altura(self):
		"""
		Returns:
			int: altura
		"""
		return self.tamano[1]

	def get_anchura(self):
		"""
		Returns:
			int: anchura
		"""
		return self.tamano[0]

	def add_canvas(self, canvas, nombre):
		"""Añade un Canvas al diccionario de canvas

		Args:
			canvas (:class: Canvas): El Canvas a añadir.
			nombre (str): El nombre a asignar para identificar al Canvas.

		"""
		canvas.pantalla = self.superficie
		self.canvas[nombre] = canvas

	def leer(self):
		"""Captura los valores de las entradas y los almacena en self.salida.
		Después lanza el proyectil con estos datos.
		"""
		self.salida = (int(self.inserter_velocidad.get_value()), int(self.inserter_angulo.get_value()))
		self.canvas["0"].particulas[0].lanzar(self.salida[0], self.salida[1])

	def show_position(self):
		"""Si la simulación ha terminado, consigue la posición en x del mouse,
		y a partir de ella, consigue la posición en y, para mostrar ambas
		en las salidas de posicion_x y posicion_y
		"""
		if(self.canvas["0"].particulas[0].estado == Estado.TERMINADO):
			p_x = pygame.mouse.get_pos()[0]
			if(p_x in self.canvas["0"].particulas[0].trayectoria.puntos):
				self.posicion_x.set_text("x: " + str(p_x) + "m")
				self.posicion_y.set_text("y: " + str(self.canvas["0"].particulas[0].trayectoria.puntos[p_x]) + "m")

	def run(self):
		"""El Main Loop del programa, es el programa en sí.
		"""
		activo = True
		while activo:
			for evento in pygame.event.get():
				#le manda el evento a la entrada, para que se actualize
				self.entrada.update(evento)
				if self.entrada._activado:
					#si se ha presionado el botón para enviar la entrada, almacenar sus datos
					modulo = int(self.entrada.valores['velocidad'])
					angulo = int(self.entrada.valores['angulo'])
					#reiniciar: esta parte sirve para poder lanzar varias veces sin cerrar y abrir el programa
					self.canvas["0"].particulas[0].trayectoria.clear()
					self.canvas["0"].particulas[0].clear()
					self.canvas["0"].particulas[0].lanzar(modulo, angulo)
					self.entrada._activado = False #para que vuelva a mandar los nuevos datos.

				if(evento.type == pygame.QUIT):
					activo = False
			self.superficie.fill(self.background) #pintar el fondo primero

			#si se ha terminado la simulación, comenzar a mostrar los datos de la trayectoria de forma dinámica
			if self.canvas["0"].particulas[0].estado == Estado.TERMINADO:
				particula = self.canvas["0"].particulas[0]
				pos_x = pygame.mouse.get_pos()[0]

				self.salida_estatica.update(salidas=[
					"{:.2f}s".format(particula.tiempo_total),
					"{:.2f}m".format(particula.distancia_recorrida),
					"{:.2f}m".format(particula.altura_maxima)])

				if pos_x in particula.trayectoria.puntos.keys():
					pos_y = particula.trayectoria.get_punto_y(pos_x)
					velocidad = particula.trayectoria.get_velocidad(pos_x)
					tiempo = particula.trayectoria.get_tiempo(pos_x)
					self.salida.update(salidas=[
						"{}m".format(pos_x),
						"{}m".format(pos_y),
						"{}".format(velocidad),
						"{:.2f} m/s".format(velocidad.get_vector_x().get_modulo()),
						"{:.2f} m/s".format(velocidad.get_vector_y().get_repr_y()),
						"{:.2f}s".format(tiempo)])
			
			#renderizar la GUI y a esta clase
			self.entrada.render()
			self.salida.render()
			self.salida_estatica.render()
			self.display()

	def display(self):
		"""Actualiza los canvas, los pinta en esta ventana, y lleva a cabo el flip para mostrar los cambios
		"""
		for c in self.canvas.values():
			c.update()
			self.superficie.blit(c.superficie, c.origen)
		pygame.display.flip()


if __name__ == '__main__':
	ventana = Ventana((600, 400))
	ventana.run()