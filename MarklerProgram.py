//Von Nils, Sopfie und Jonathan

import os

class Room:
	def __init__(self, name, area):
		self.name = name
		self.area = area

#Global variabales
houseArea = 0
roomList = []


while (True) :
	inputQuery = input('Neuen Raum hinzufügen? [y/n]\n')
	if inputQuery == 'n':
		break

	if inputQuery == 'y':

		roomArea = 0


		inputName = input('Bitte geben Sie dem Raum einen Namen:')
		print("\n")

		inputOption = input('Hat der Raum eine Dachschräge oder ist die Fläche eine Terrasse?')
		print("\n")

		squareNumber = int(input('Teile den Raum in die kleinstmögliche Anzahl von Rechtecken. Wie viele sind es?\n'))
		print("\n")
		for i in range(squareNumber):
			sideA = float(input('Was ist die Länge deines Rechtecks in Metern?\n'))
			print("\n")
			sideB = float(input('Was ist die Breite deines Rechtecks in Metern?\n'))
			print("\n")
			roomArea += (sideA * sideB)
			print('Nächstes Rechteck!')

		print("\n")

		if inputOption == 'y':
			inputProzent = float(input('Viel viel Prozent vom Raum hat eine Dachschräge?(Terrasse = 100)\n'))
			dezProzent = inputProzent / 100


			roomArea = roomArea - ((roomArea * dezProzent) / 2)

		r1 = Room(inputName, roomArea)
		roomList.append(r1)
		print("\n")

		print('\nDieser Raum ist ' + str(roomArea) + ' m² groß.')
		houseArea += roomArea
	else:
		print('Bitte antworte mit Y oder N')


for Room in roomList:
	print('\n\n' + Room.name, str(Room.area) + ' m²')
	print("\n")

print('Die gesamte Fläche beträgt ' + str(houseArea) + 'm².')
