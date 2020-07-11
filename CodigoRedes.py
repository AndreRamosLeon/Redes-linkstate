# -*- coding: utf-8 -*-
"""
Created on Wed Jul  8 18:53:08 2020

@author: Andre
"""

#Se importa la libreria heapq para utilziar una cola de prioridad
import heapq

def calcular_distancia(grafo, origen):
       
    distancias = {vertice: float('inf') for vertice in grafo}
    distancias[origen] = 0
    pq = [(0, origen)]
    
    
    #luego se esta haciendo un bucle while que permita recorrer la lista pq 
    #hasta que se hayan visitado todos los nodos del grafo
    
    while len(pq) > 0:

        distancia_actual, vertice_actual = heapq.heappop(pq)
        if distancia_actual > distancias[vertice_actual]:
            continue


        #Luego se almacena en las varaibles vecino, peso los valores del vecino del nodo actual
        # para comenzar a realizar las comparaciones, si es que encuentra que el peso del nodo vecino
        #en la lista distancias es menor al calculado, entonces lo reemplaza y se procede a insteratar los nodos manteniendo el orden de clasifiacion
        #establecido por la funcion heapqheappush
        
        for vecino, peso in grafo[vertice_actual].items():
            distancia = distancia_actual + peso
            if distancia < distancias[vecino]:
                distancias[vecino] = distancia
                heapq.heappush(pq, (distancia, vecino))

    

    return distancias
            


Grafo1 = {
    '0': {'1': 20, '3': 5, '4': 20},
    '1': {'0': 20, '2': 10},
    '2': {'4': 10, '1': 10},
    '3': {'0': 5, '4': 10},
    '4': {'0': 20, '3': 10, '2': 10}}

#print(calcular_distancia(Grafo1, '0'))



Grafo2 = {
    '0': {'2': 5, '1': 10, '9': 3, '3':6},
    '1': {'0': 10, '2': 8},
    '2': {'1': 8, '0': 5, '5':2 , '8':6 },
    '3': {'0': 6, '9': 4, '13':11 , '4': 9, '5': 2},
    '4': {'3': 9, '10': 2, '11': 4},
    '5': {'2': 2, '3': 2, '7': 1, '11': 6},
    '6': {'10': 4, '11': 3},
    '7': {'4': 10, '1': 10},
    '8': {'2': 6, '7': 7},
    '9': {'0': 3, '3': 4, '12': 3},
    '10': {'4': 2, '6': 4, '13': 4},
    '11': {'5': 6, '4': 4, '6': 3},
    '12': {'9': 3},
    '13': {'3': 11, '10': 4}}

#print(calcular_distancia(Grafo2, '0'))

Grafo3 = {
    'R0': {'SW0': 2, 'R1': 4},
    'R1': {'R2': 3, 'R0': 4, 'R3': 2},
    'R2': {'R1': 3, 'R4': 4},
    'R3': {'R1': 2, 'R4': 5, 'R10': 10},
    'R4': {'R3': 5, 'R2': 4, 'R6': 13, 'R5': 8},
    'R5': {'R4': 8, 'R6': 9},
    'R6': {'R4': 13, 'R5': 9, 'SW4': 9, 'SW13': 10, 'R14': 12},
    'R7': {'SW1': 3, 'R10': 5},
    'R8': {'SW2': 2, 'R10': 6},
    'R9': {'SW3': 3, 'R10': 4},
    'R10': {'R7': 5, 'R8': 6, 'R9': 4, 'R3': 10, 'R12': 4, 'R11': 3},
    'R11': {'SW5': 2, 'SW6': 5, 'SW7': 6, 'R10': 3, 'R13':4},
    'R12': {'R10': 4, 'R13':2},
    'R13': {'R12': 2, 'R11': 4, 'SV0':4},
    'R14': {'R6': 12, 'R15': 4, 'R17': 9},
    'R15': {'R14': 4, 'R16': 5, 'SW14': 2},
    'R16': {'R15': 5, 'SW15': 3, 'R17': 3},
    'R17': {'R16': 3, 'SW16': 3, 'R14': 9},
    'SW0': {'R0': 2},
    'SW1': {'R7':3},
    'SW2': {'R8': 2},
    'SW3': {'R9': 3 },
    'SW4': {'SW8': 4, 'SW9': 6, 'R6': 9},
    'SW5': {'R11': 2},
    'SW6': {'R11': 5},
    'SW7': {'R11': 6},
    'SW8': {'SW10': 8, 'SW11': 2},
    'SW9': {'SW11': 5, 'SW12': 3, 'SW4':6},
    'SW10': {'SW8':8},
    'SW11': {'SW8': 2, 'SW9': 5},
    'SW12': {'SW9': 3},
    'SW13': {'SV1': 8, 'R6': 10},  
    'SW14': {'R15': 2},
    'SW15': {'R16': 3},
    'SW16': {'R17': 3},
    
    'SV0': {'R13': 4},
    'SV1': {'SW13': 8}}

print(calcular_distancia(Grafo3, 'R6'))