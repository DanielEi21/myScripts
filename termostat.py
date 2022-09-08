#!/usr/bin/python3

'''
Läs user-input
'''
NuTemp = input('Ange temperaturen?')

'''
Evaluera 
'''
if int(NuTemp) < 25:
	print('Stäng av värme!')
elif int(NuTemp) > 24:
	print('slå på värme!')

print('Slut på program')

