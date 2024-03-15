from lib3 import *
import sys

diccRel = {}

grafoTest = grafo()
grafoTest.addArista('A', 'B', 5)
grafoTest.addArista('A', 'C', 3)

grafoTest.addArista('B', 'A', 5)
grafoTest.addArista('B', 'C', 2)
grafoTest.addArista('B', 'D', 4)

grafoTest.addArista('C', 'A', 3)
grafoTest.addArista('C', 'B', 2)
grafoTest.addArista('C', 'D', 6)
grafoTest.addArista('C', 'E', 7)

grafoTest.addArista('D', 'B', 4)
grafoTest.addArista('D', 'C', 6)
grafoTest.addArista('D', 'E', 8)

grafoTest.addArista('E', 'C', 7)
grafoTest.addArista('E', 'D', 8)

origen = 'A'
destino = 'E'
__path__[origen] = {'-':0}
llaves = grafoTest.aristas['A'].keys()
print(llaves)
for i in llaves:
    __path__[i]={origen: grafoTest.aristas}
   
print(grafoTest.aristas[origen])

