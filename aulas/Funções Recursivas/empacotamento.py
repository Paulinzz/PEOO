def func(*posicionais, **nomeados):
   print('Parâmetros posicionais:')
   for valor in posicionais:
       print(valor)
   print('Parâmetros nomeados:')
   for chave, valor in nomeados.items():
       print(chave, '=', valor)
func(1, 2, 3, a=4, b=5)
func(1, 2, 3)
func(a=4, b=5)