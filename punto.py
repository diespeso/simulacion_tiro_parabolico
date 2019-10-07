# -*- coding: utf-8 -*-
class Punto:
	"""Simple representación de un punto en el espacio
	Args:
		x (int): coordenada horizontal
		y (int): coordenada vertical

	Attributes:
		x (:obj:'int'): coordenada horizontal
		y (:obj:'int'): coordenada vertical
	"""

	def __init__(self, x, y):
		self.x = x
		self.y = y

	def __str__(self):
		return "(x: {0:.2f}, y: {1:.2f})".format(self.x, self.y)

	def sumar(self, punto):
		"""Suma dos puntos, devolviendo la suma
		Returns:
			Punto: la suma de los dos puntos
		"""
		return Punto(self.x + punto.x, self.y + punto.y)

	def to_tuple(self):
		"""Convierte este punto a una tupla tipo (int, int)
		Returns:
			(int, int): representación de tupla de este Punto
		"""
		return (self.x, self.y)

def from_vector_int(vector):
	"""Devuelve un Punto usando un vector como base.
	Toma un vector, saca sus representaciones en ambos ejes y hacer un punto
	con estas

	Returns:
		Punto: El punto donde está la punta del vector.
	"""
	return Punto(int(vector.get_repr_x()), int(vector.get_repr_y()))