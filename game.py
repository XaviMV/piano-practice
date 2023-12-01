import cv2
import random
import numpy as np
import pygame
from pygame import mixer
import os

import time as t

from funcs import nota_random

def dibuixar_tecles(screen, blanques_clicades, negres_clicades):

	notes_globals = ["do", "re", "mi", "fa", "sol", "la", "si"]

    # dibuixar tecles blanques
	for i in range(7):
		color = (255,255,255)

		if blanques_clicades[i] == 1:
			color = (255,0,0)
		elif blanques_clicades[i] == 2:
			color = (0,255,0)
		pygame.draw.rect(screen, color, (362+i*80,475,75,200))

		myfont = pygame.font.SysFont("monospace", 30)
		# render text
		label = myfont.render(notes_globals[i], 10, (255,255,0))
		screen.blit(label, (362+i*80+15, 700))
	
    # dibuixar tecles negres
	for i in range(6):
		color = (0,0,0)
		if i != 2:
			if negres_clicades[i]:
				color = (255,0,0)
			pygame.draw.rect(screen, color, (362+55+i*80,475,45,125))


def detect_click(nota, events):
	negres_clicades = [0,0,0,0,0,0] # el tercer element (comencant desde l'1) no representa ninguna tecla
	blanques_clicades = [0,0,0,0,0,0,0]

	notes_globals = ["do", "re", "mi", "fa", "sol", "la", "si"]

	estat = ""

	# detectar si el ratoli esta clicat
	clicat = False
	for e in events:
		if e.type == pygame.MOUSEBUTTONDOWN:
			clicat = True

	x, y = pygame.mouse.get_pos()

	for i in range(6):
		if i == 2:
			continue

		if clicat and x > 362+55+i*80 and x < 362+55+i*80+45 and y > 475 and y < 475+125:
			negres_clicades[i] = 1
			estat = "error"

	for i in range(7):
		if any(negres_clicades): # si alguna tecla negra ha sigut clicada passem de mirar les blanques
			continue

		if clicat and x > 362+i*80 and x < 362+i*80 + 75 and y > 475 and y < 475+200:
			if notes_globals[i] == nota:
				blanques_clicades[i] = 2
				estat = "correcte"
			else:
				blanques_clicades[i] = 1
				estat = "error"

	return blanques_clicades, negres_clicades, estat

def fitxer_audio_nota(nota): # nota es un numero string que representa la nota

	for a in os.listdir(os.path.join(os.getcwd(), "audio")):
		if nota in a.lower():
			return os.path.join("audio", a) 

	return -1


# pygame setup
pygame.init()
screen = pygame.display.set_mode((1280, 750))
clock = pygame.time.Clock()
running = True

notes_encertades = [1,1,1]
notes = []
nota_actual = 0
while running:

	if all(notes_encertades):
		img, notes = nota_random()
		img = cv2.flip(img, 1)
		img = np.rot90(img)
		img = pygame.surfarray.make_surface(img)
		
		notes_encertades = [0,0,0]
		nota_actual = 0

	# mirar events
	events = pygame.event.get()
	for e in events:
		if e.type == pygame.QUIT:
			running = False

	# mirar si sha clicat alguna tecla
	blanques_clicades, negres_clicades, estat = detect_click(notes[nota_actual], events)

	if estat == "correcte":
		notes_encertades[nota_actual] = 1
		nota_actual += 1

		mixer.music.load(fitxer_audio_nota(notes[nota_actual-1]))
		mixer.music.play(1)

	# pintar pantalla
	screen.fill((50,50,50))
	screen.blit(img, (265, 50)) # imatge de les notes
	pygame.draw.rect(screen, (50,50,50), (0, 400, 1280, 720))
	pygame.draw.rect(screen, (0,0,0), (352, 465, 575, 220))
	dibuixar_tecles(screen, blanques_clicades, negres_clicades)

	# update
	pygame.display.update()

	clock.tick(10)  # limits FPS to 20

pygame.quit()