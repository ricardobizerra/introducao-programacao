nome_do_fogo = input()
db_felipe = int(input())
db_caruaru = int(input())
db_campina_grande = int(input())

if (db_felipe < db_caruaru) and (db_felipe < db_campina_grande):
  print(f'Boa Felipe, o {nome_do_fogo} será um sucesso em Campina Grande e Caruaru!')
elif (db_felipe < db_caruaru) and not (db_felipe < db_campina_grande):
  print(f'Infelizmente em Campina Grande não vai rolar, mas em Caruaru o {nome_do_fogo} vai ser extouro!')
elif not (db_felipe < db_caruaru) and (db_felipe < db_campina_grande):
  print(f'Infelizmente em Caruaru não vai rolar, mas em Campina Grande o {nome_do_fogo} vai ser extouro!')
else:
  print(f'Poxa Felipe, não vai ser dessa vez que {nome_do_fogo} fará um sucesso pelas festas juninas do Brasil')