# coordenada atual de Tantan
x = int(input())
z = int(input())

# calculo da distancia
dist_h = ((x-34)**2 + (z-220)**2)**(1/2)
dist_k = (x**2 + z**2)**(1/2)
dist_s = ((x-140)**2 + (z-456)**2)**(1/2)

# impressao das distancias
print(f'Distancia para Hogsmeade: {dist_h:.2f}')
print(f'Distancia para Kakariko: {dist_k:.2f}')
print(f'Distancia para Solitude: {dist_s:.2f}')