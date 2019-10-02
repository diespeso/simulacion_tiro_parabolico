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

		#NEWCODE
		"""
		import thorpy
		self.inserter_angulo = thorpy.Inserter("angulo: ")
		self.inserter_velocidad = thorpy.Inserter("velocidad: ")
		self.boton = thorpy.make_button("Ok", func=self.leer)
		self.posicion_x = thorpy.make_text("posicion_x", 12, (0, 0, 0))
		self.posicion_y = thorpy.make_text("posicion_y", 12, (0, 0, 0))
		caja = thorpy.Box(elements=[self.inserter_velocidad, self.inserter_angulo, self.boton])
		caja_dos = thorpy.Box(elements=[self.posicion_x, self.posicion_y])
		caja_dos.set_topleft((250, 0))
		menu = thorpy.Menu()
		menu_dos = thorpy.Menu()
		menu.add_to_population(caja)
		menu_dos.add_to_population(caja_dos)

		for elemento in menu.get_population():
			elemento.surface = self.superficie

		for elemento in menu_dos.get_population():
			elemento.surface = self.superficie
		

		caja.blit()
		caja.update()
		caja_dos.blit()
		caja_dos.blit()
		"""
		#NEWCODE


		#NEWCODE2
		from gui.entrada import Entrada
		from gui.salida import Salida
		entrada = Entrada(entradas=["velocidad", "angulo"])
		salida = Salida(elementos=["distancia", "altura",
			"velocidad", "velocidad x", "velocidad y",
			"tiempo"])

		#NEWCODE2

		while activo:
			for evento in pygame.event.get():

				#NEWCODE2
				entrada.update(evento)
				if entrada._activado:
					modulo = int(entrada.valores['velocidad'])
					angulo = int(entrada.valores['angulo'])
					self.canvas["0"].particulas[0]	.lanzar(modulo, angulo)
					entrada._activado = False
				#NEWCODE2

				#NEWCODE
				#menu.react(evento)
				#menu_dos.react(evento)
				#NEWCODE
				if(evento.type == pygame.QUIT):
					activo = False
			#NEWCODE
			self.superficie.fill(self.background)

			if self.canvas["0"].particulas[0].estado == Estado.TERMINADO:
				particula = self.canvas["0"].particulas[0]
				pos_x = pygame.mouse.get_pos()[0]

				if pos_x in particula.trayectoria.puntos.keys():
					pos_y = particula.trayectoria.get_punto_y(pos_x)
					velocidad = particula.trayectoria.get_velocidad(pos_x)
					tiempo = particula.trayectoria.get_tiempo(pos_x)
					salida.update(salidas=[
						pos_x,
						pos_y,
						velocidad,
						velocidad.get_vector_x(),
						velocidad.get_vector_y(),
						"{:.2f}".format(tiempo)])
			
			"""
			menu.refresh_population()
			menu.blit_and_update()
			menu_dos.refresh_population()
			menu_dos.blit_and_update()
			self.show_position()
			"""
			#NEWCODE
			entrada.render()
			salida.render()
			self.display()

	def display(self):
		for c in self.canvas.values():
			c.update()
			self.superficie.blit(c.get_superficie(), c.origen)
		pygame.display.flip()


if __name__ == '__main__':
	ventana = Ventana((600, 400), (255, 0, 150))
	ventana.run()