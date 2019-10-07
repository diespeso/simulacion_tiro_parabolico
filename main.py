#!/usr/bin/env python3
#-*- coding=utf-8 -*-

from canvas import Canvas
from ventana import Ventana 
from vector import Vector
from particula import Particula

import pygame


def main(**args):
	ventana = Ventana((800, 600))
	canvas = Canvas((800, 450), (0, 150))
	particula = Particula()
	canvas.add_particula(particula, 0)
	ventana.add_canvas(canvas, "0")
	ventana.run()

if __name__ == '__main__':
	main()




