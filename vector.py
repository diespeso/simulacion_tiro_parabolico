# -*- coding: utf-8 -*-
#!/usr/bin/env python3

import math

from punto import Punto

class Vector:
	"""Un Vector es vector matemático, representado por coordenadas polares o rectangulares

	Args:
		**args: Una lista de argumentos opcionales.
			Se puede introducir coordenadas polares: (modulo, angulo)
			o coordenadas rectangulares (x, y)
	"""

	def __init__(self, **args):
		"""
			se tiene que elegir entre uno de los dos inicializadores:
			__init__(modulo=0, angulo=0)
			__init__(x=0, y=0)
		"""
		if 'modulo' in args and 'angulo in args': #si da módulo y ángulo tomar directo
			self.modulo = args['modulo']
			self.angulo = args['angulo']
		else:
			self.modulo = math.sqrt(math.pow(args['x'], 2.0) + math.pow(args['y'], 2.0))
			if args['x'] == 0 or args['y'] == 0: #caso para vector nulo
				if(args['x'] and args['y']):
					self.modulo = 0
					self.angulo = 0
					return
				else:
					if args['x'] == 0: #caso para vector con representación en un sólo eje
						if args['y'] > 0:
							self.angulo = 90
						else:
							self.angulo = 270
					if args['y'] == 0:
						if args['x'] > 0:
							self.angulo = 0
						else:
							self.angulo = 180
			else:									#caso para vectores con ambas componentes, ajuste de cuadrantes
				angulo = math.degrees(math.atan(args['y'] / args['x']))
				if args['x'] < 0 and args['y'] > 0: #segundo cuadrante
					self.angulo = angulo + 180
				elif args['x'] < 0 and args['y'] < 0: #tercer cuadrante
					self.angulo = angulo + 180
				elif args['x'] > 0 and args['y'] < 0: #cuarto cuadrante
					self.angulo = angulo + 360
				else:
					self.angulo = math.degrees(math.atan(args['y'] / args['x']))
		

	def __str__(self):
		"""
			Muestra el vector en un par (módulo, ángulo)
			redondeando los decimales a 2 posiciones.
		"""
		return '({0:.2f}m, {1:.2f}°)'.format(self.modulo, self.angulo)


	def get_modulo(self):
		"""Regresa el módulo (tamaño del vector) en valor absoluto
		"""
		return self.modulo

	def get_repr_x(self):
		"""Regresa el valor de la representacíón (componente) en x.
		Es decir, el valor será positivo o negativo dependiendo del ángulo
		"""
		if(self.angulo > 90 and self.angulo < 270):
			return -self.get_vector_x().get_modulo();
		else:
			return self.get_vector_x().get_modulo();

	def get_repr_y(self):
		"""Regresa el valor de la representacíón (componente) en y.
		Es decir, el valor será positivo o negativo dependiendo del ángulo
		"""
		if(self.angulo > 180):
			return -self.get_vector_y().get_modulo();
		else:
			return self.get_vector_y().get_modulo();

	def get_vector_x(self):
		"""regresa un vector representación en x
		IMPORTANTE: regresa el módulo en valor absoluto
		"""
		modulo_x = self.modulo * math.cos(math.radians(self.angulo))
		if(modulo_x < 0):
			#si es negativo, toma el valor absoluto del módulo y cambia el sentido
			return Vector(modulo=-modulo_x, angulo=180)
		else:
			return Vector(modulo=modulo_x, angulo=0)

	def get_vector_y(self):
		""""regresa un vector representación en y
		IMPORTANTE: regresa el módulo en valor absoluto
		"""
		modulo_y = self.modulo * math.sin(math.radians(self.angulo))
		if(modulo_y < 0):
			return Vector(modulo=-modulo_y, angulo=270)
		else:
			return Vector(modulo=modulo_y, angulo=90)

	def sumar(self, vector):
		"""Suma dos vectores.
		Args:
			vector (:class: Vector): el vector a sumar con este.
		Returns:
			Vector: La suma de este vector más el vector dado.
		"""
		this_x = self.get_repr_x()
		this_y = self.get_repr_y()

		v_x = vector.get_repr_x()
		v_y = vector.get_repr_y()

		return Vector(x=this_x+v_x, y=this_y+v_y)

	def restar(self, vector):
		"""Resta dos vectores.
		Args:
			vector (:class: Vector): el vector a restar con este.
		Returns:
			Vector: La resta de este vector menos el vector dado.
		"""
		this_x = self.get_repr_x()
		this_y = self.get_repr_y()

		v_x = vector.get_repr_x()
		v_y = vector.get_repr_y()


		return Vector(x=this_x-v_x, y=this_y-v_y)

	def descomponer(self):
		""" Descompone el vector dado en sus componentes x, y

		Returns:
			(double, double): (componente_x, componente_y)
		"""
		return (self.get_vector_x(), self.get_vector_y())

	def escalar(self, c):
		"""Escala este vector con la constante dada
		Args:
			c (double): Una constante por la cual escalar este vector.
		Returns:
			Vector: Este vector escalado por la constante.

		"""
		return Vector(modulo=self.modulo * c, angulo= self.angulo)

	def to_punto(self):
		"""Convierte este vector al punto donde se ubica la punta de este vector.

		Returns:
			Punto: (represetacion_x, representacion_y)

		"""
		return Punto(self.get_repr_x(), self.get_repr_y())


#---PRUEBAS---
if __name__ == '__main__':
	vector = Vector(modulo=80, angulo=30)
	vector_x = vector.get_vector_x()
	vector_y = vector.get_vector_y()

	print(str(vector_x) + " + " + str(vector_y) + " = " + str(vector_x.sumar(vector_y)))
	print(str(vector.restar(vector_y)))

	print(vector_x.escalar(0.5))
