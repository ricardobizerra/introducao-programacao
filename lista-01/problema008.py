cidade1 = input()
nota1 = float(input())
distancia1 = int(input())

cidade2 = input()
nota2 = float(input())
distancia2 = int(input())

cidade3 = input()
nota3 = float(input())
distancia3 = int(input())

if nota1 < 4.0 and nota2 < 4.0 and nota3 < 4.0:
    print('Nota mínima não atingida')
else:
    if (nota1 > nota2) and (nota1 > nota3):
        melhor_cidade = cidade1
    elif (nota2 > nota3):
        melhor_cidade = cidade2
    elif (nota3 > nota2):
        melhor_cidade = cidade3
    elif (nota1 == nota2 == nota3):
        if (distancia1 < distancia2) and (distancia1 < distancia3):
            melhor_cidade = cidade1
        elif (distancia2 < distancia3):
            melhor_cidade = cidade2
        else:
            melhor_cidade = cidade3
    elif (nota1 == nota2):
        if (distancia1 < distancia2):
            melhor_cidade = cidade1
        else:
            melhor_cidade = cidade2
    elif (nota1 == nota3):
        if (distancia1 < distancia3):
            melhor_cidade = cidade1
        else:
            melhor_cidade = cidade3
    elif (nota2 == nota3):
        if (distancia2 < distancia3):
            melhor_cidade = cidade2
        else:
            melhor_cidade = cidade3
    print(melhor_cidade)
