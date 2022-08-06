nome_da_musica = input()
genero = input()

if genero == 'Forró' or genero == 'Xote':
  print(f"'{nome_da_musica}' foi adicionada com sucesso na playlist 'Dandrilha'.")
else:
  print(f"Ocorreu um erro ao adicionar '{nome_da_musica}' na playlist.")