# -*- coding: utf-8 -*-

"""
Programa para la simulación del tiro parabólico de una partícula.
La simulación se dibuja en una ventana, la cual se puede divirir
en dos partes: la interfaz de usuario (GUI) y el canvas.

En la GUI se recibe entrada del usuario: una velocidad inicial y
un ángulo para llevar a cabo un tiro.

En el canvas se renderiza y simula el tiro.

Una vez terminada la simulación, el usuario puede mover su cursor
por la trayectoria, y en la GUI se mostrarán los datos de la partí
cula lanzada en la posición exacta donde esté el cursor en el eje x.

"""

import sys

sys.path.insert(0, '/home/radge/Escritorio/pycode/proyecto_final')

import pdoc

import gui.entrada
import gui.salida
import particula
import vector
import canvas
import main
import punto
import ventana
import vector_grafico
import trayectoria

import variables