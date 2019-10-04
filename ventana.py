#!/usr/bin/env python3

import pygame

from particula import Estado

from variables import MENU_FONDO_COLOR

pygame.init()

class Ventana:
	#clase de utilería para abrir una ventana y renderizar
	def __init__(self, tamano):
		self.tamano = tamano
		self.superficie = pygame.display.set_mode(tamano)
		self.background = MENU_FONDO_COLOR
		self.canvas = {}

	def get_superficie(self):
		return self.superficie

	def get_altura(self):
		return self.tamano[1]

	def get_anchura(self):
		return self.tamano[0]

	def add_canvas(self, canvas, nombre):
		canvas.pantalla = self.superficie
		self.canvas[nombre] = canvas

	def add_particula(self, particula, id):
		self.particulas[id] = particula

	def leer(self):
		self.salida = (int(self.inserter_velocidad.get_value()), int(self.inserter_angulo.get_value()))
		self.canvas["0"].particulas[0].lanzar(self.salida[0], self.salida[1])

	def show_position(self):
		if(self.canvas["0"].particulas[0].estado == Estado.TERMINADO):
			p_x = pygame.mouse.get_pos()[0]
			if(p_x in self.canvas["0"].particulas[0].trayectoria.puntos):
				self.posicion_x.set_text("x: " + str(p_x) + "m")
				self.posicion_y.set_text("y: " + str(self.canvas["0"].particulas[0].trayectoria.puntos[p_x]) + "m")

	def run(self):
		activo = True

		from gui.entrada import Entrada
		from gui.salida import Salida
		entrada = Entrada(entradas=["velocidad", "angulo"])
		salida = Salida(elementos=["distancia", "altura",
			"velocidad", "velocidad x", "velocidad y",
			"tiempo"], tamano=(300, 200), posicion=(170, 0))
		salida_estatica = Salida(elementos=["tiempo total",
			"desplazamiento total", "altura maxima"], posicion=(470, 0), tamano=(250, 200))


		while activo:
			for evento in pygame.event.get():

				entrada.update(evento)
				if entrada._activado:
					modulo = int(entrada.valores['velocidad'])
					angulo = int(entrada.valores['angulo'])
					#reiniciar
					self.canvas["0"].particulas[0].trayectoria.clear()
					self.canvas["0"].particulas[0].clear()
					self.canvas["0"].particulas[0].lanzar(modulo, angulo)
					entrada._activado = False

				if(evento.type == pygame.QUIT):
					activo = False
			self.superficie.fill(self.background)

			if self.canvas["0"].particulas[0].estado == Estado.TERMINADO:
				particula = self.canvas["0"].particulas[0]
				pos_x = pygame.mouse.get_pos()[0]

				salida_estatica.update(salidas=[
					"{:.2f}s".format(particula.tiempo_total),
					"{:.2f}m".format(particula.distancia_recorrida),
					"{:.2f}m".format(particula.altura_maxima)])

				if pos_x in particula.trayectoria.puntos.keys():
					pos_y = particula.trayectoria.get_punto_y(pos_x)
					velocidad = particula.trayectoria.get_velocidad(pos_x)
					tiempo = particula.trayectoria.get_tiempo(pos_x)
					salida.update(salidas=[
						"{}m".format(pos_x),
						"{}m".format(pos_y),
						"{}".format(velocidad),
						"{:.2f} m/s".format(velocidad.get_vector_x().get_modulo()),
						"{:.2f} m/s".format(velocidad.get_vector_y().get_repr_y()),
						"{:.2f}s".format(tiempo)])
			
			entrada.render()
			salida.render()
			salida_estatica.render()
			self.display()

	def display(self):
		for c in self.canvas.values():
			c.update()
			self.superficie.blit(c.get_superficie(), c.origen)
		pygame.display.flip()


if __name__ == '__main__':
	ventana = Ventana((600, 400), (255, 0, 150))
	ventana.run()