import cv2
import random
import numpy as np



# FER QUE PUGUI FER SUSTINGUTS I BAMOLLS (sharp i falt)

def nota_random(): # retorna una imatge amb 3 notes random i un string dient quines notes son

	notes_globals = ["do", "re", "mi", "fa", "sol", "la", "si"]

	notes_globals = notes_globals[::-1] 

	img = np.zeros((425, 750))

	img.fill(255)

	y_ini = 50

	# dibuixar les 5 linies
	for i in range(5):
		img = cv2.line(img, (50, y_ini+50*i), (700, y_ini+50*i), (0,0,0), 3)

	notes_imatge = []

	for i in range(3): # dibuixar les 3 notes
		rand_num = random.randint(0, len(notes_globals)-1)

		x_ini = 150 + i*200

		cv2.ellipse(img, (x_ini,150+rand_num*25), (20, 15), 0, 0, 360, (0,0,0), -1)
		if rand_num == 6: # si la nota es DO cal dibuixar una linia
			cv2.line(img, (x_ini-25,150+rand_num*25), (x_ini+25,150+rand_num*25), (0,0,0), 3)

		nota = notes_globals[rand_num]

		rand_num_2 = random.randint(0, 5)
		if rand_num_2 == 0 and nota != "mi" and nota != "si": # sostingut
			img = cv2.putText(img, "#", (x_ini-65, 165+rand_num*25), cv2.FONT_HERSHEY_TRIPLEX, 2, (0,0,0), 2, cv2.LINE_AA)
			nota += "+"

		elif rand_num_2 == 1 and nota != "fa" and nota != "do": # bemoll
			img = cv2.putText(img, "b", (x_ini-65, 165+rand_num*25), cv2.FONT_HERSHEY_TRIPLEX, 2, (0,0,0), 2, cv2.LINE_AA)
			nota += "-"

		notes_imatge.append(nota)


	return img, notes_imatge


def posar_nota(image, notes): # posa la nota a una imatge amb la nota donada

	for i in range(len(notes)):

		n = notes[i]

		# font 
		font = cv2.FONT_HERSHEY_SIMPLEX 
		  
		# org 
		org = (120+i*200, 375) 
		  
		# fontScale 
		fontScale = 2
		   
		# Black color in BGR 
		color = (0, 0, 0) 
		  
		# Line thickness of 2 px 
		thickness = 3
		   
		# Using cv2.putText() method 
		image = cv2.putText(image, n, org, font, fontScale, color, thickness, cv2.LINE_AA)

	return image



while False:

	img, notes = nota_random()

	cv2.imshow("nota", img)
	key = cv2.waitKey(0)
	if key == 113: # si sha clicat la lletra "q"
		break

	img = posar_nota(img, notes)

	cv2.imshow("nota", img)
	key = cv2.waitKey(0)
	if key == 113: # si sha clicat la lletra "q"
		break


