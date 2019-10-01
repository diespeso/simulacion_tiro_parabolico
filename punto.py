class Punto:
	"""
		Simple representación de un punto en el espacio
	"""

	def __init__(self, x, y):
		self.x = x
		self.y = y

	def __str__(self):
		return "(x: {0:.2f}, y: {1:.2f})".format(self.x, self.y)

def from_vector_int(vector):
	return Punto(int(vector.get_repr_x()), int(vector.get_repr_y()))