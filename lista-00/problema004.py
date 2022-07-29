# blocos médios por hora
a = int(input())
l = int(input())
p = int(input())

# duracao da competicao
h = int(input())

# comparacao entre valores
n = (a + l + abs(a - l))/2
m = int((p + n + abs(p - n))/2)

# impressao do valor maximo obtido
print(m*h)