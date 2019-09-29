#!/usr/bin/evn python3

from vector import Vector
from punto import Punto
import math

class Particula:
	"""
		Representa a un objeto que describe una
		trayectoria parabólica
	"""

	def __init__(self):
		self.posicion = Punto(0, 0)
		self.velocidad = Vector(x=0, y=0)
		self.gravedad = -9.8
		self.velocidad_inicial = Vector(x=0, y=0)
		self.tiempo_transcurrido = 0
		self.tiempo_total = 0
		self.altura_maxima = 0
		self.distancia_recorrida = 0

	def lanzar(self, velocidad, angulo):

		self.velocidad_inicial = Vector(modulo=velocidad, angulo=angulo)
		print(self.velocidad_inicial)
		self.velocidad = self.velocidad_inicial
		self.tiempo_total = (-self.velocidad_inicial.get_vector_y().get_modulo()
			/ self.gravedad) * 2
		self.altura_maxima = (self.velocidad_inicial.get_vector_y().get_modulo()
			* self.tiempo_total / 2.0) + (self.gravedad * math.pow(self.tiempo_total / 2, 2.0)) / 2
		
		self.simular()

	def __str__(self): 
		return ("Tiempo total: {0:.2f}s, Altura máxima: {1:.2f}m").format(
			self.tiempo_total, self.altura_maxima)

	def simular(self):
		#TODO: el ciclo no debe ir aquí adentro
		while(self.tiempo_transcurrido < self.tiempo_total):

			resultante_x = self.velocidad_inicial.get_vector_x().get_modulo()
			cambio_y = self.gravedad * self.tiempo_transcurrido
			resultante_y = cambio_y + self.velocidad_inicial.get_vector_y().get_repr_y()

			self.velocidad = Vector(x=resultante_x, y=resultante_y)

			posicion_x = self.velocidad_inicial.get_vector_x().get_modulo() * self.tiempo_transcurrido
			posicion_y = self.velocidad_inicial.get_vector_y().get_modulo() * self.tiempo_transcurrido + (self.gravedad * math.pow(self.tiempo_transcurrido, 2.0)) / 2

			self.posicion = Punto(posicion_x, posicion_y)
			print("posición: ", self.posicion)
			self.tiempo_transcurrido += 0.1

			
			#print("tiempo: {0:.2f}, x: {1}, y: {2}".format(
			#	self.tiempo_transcurrido, self.velocidad.get_vector_x(), self.velocidad.get_vector_y()))

	def get_velocidad_actual(self, posicion_x):
		return self.velocidad

	def get_posicion_actual(self, posicion_x):
		return self.posicion

if __name__ == '__main__':
	particula = Particula()
	particula.lanzar(80, 30)
	print(particula)
