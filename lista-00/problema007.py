d = int(input())

oferta_arthur = 10
oferta_luiz = 30
oferta_pedro = 100

if d > oferta_pedro:
  print('Nenhum')
elif oferta_pedro >= d > oferta_luiz:
  print('Pedro')
elif oferta_luiz >= d > oferta_arthur:
  print('Luiz')
else:
  print('Arthur')
