import pygame


class VectorGrafico:

	def __init__(self, origen, vector):
		#origen: Punto
		#vector: Vector
		self._origen = origen
		self._vector = vector

	@property
	def origen(self):
		return self._origen

	@property
	def vector(self):
		return self._vector

	def render(self, **args):
		if 'color' in args:
			color = args['color']
		if 'grosor' in args:
			grosor = args['grosor']
		if 'superficie' in args:
			superficie = args['superficie']
		punto_final = self.origen.sumar(self.vector.to_punto())
		pygame.draw.line(superficie, color, self.origen.to_tuple(), punto_final.to_tuple(), grosor)

if __name__ == "__main__":
	from vector import Vector
	from punto import Punto
	pygame.init()
	pantalla = pygame.display.set_mode((600, 400))

	while True:
		pantalla.fill((200, 100, 150))
		vector = Vector(x=10, y=10)
		vector_g = VectorGrafico(Punto(0, 0), vector)
		vector_g.render(pantalla)
		pygame.display.flip()
