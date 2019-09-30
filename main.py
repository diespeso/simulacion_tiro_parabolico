#!/usr/bin/env python3

from canvas import Canvas
from ventana import Ventana 
from vector import Vector
from particula import Particula

import pygame

ventana = Ventana((600, 400))
canvas = Canvas((600, 300), (0, 100))
particula = Particula()
canvas.add_particula(particula, 0)
particula.lanzar(80, 30)
ventana.add_canvas(canvas, "0")
ventana.run()

