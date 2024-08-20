#codigo 1:
#def somar(a: int, b: int) -> int:
#    return a + b
#res: int = somar(2, 3)
#print(res)

#codigo 2 
#a: int = 'Eu não sou um int'
#print(a, type(a))

# codigo 3
#a: int | str = 'Eu não sou um int'
#a = 10  # Mas posso ser :)
#print(a, type(a))

#codigo 4

def atribuir_notas(alunos: list[str],
                  notas: list[int]) -> list[dict[str, int]]:
  atribuicao: list[dict[str, int]] = []
  for i in range(len(alunos)):
      d = {'aluno': alunos[i], 'nota': notas[i]}
      atribuicao.append(d)
  return atribuicao


alunos = ['Adriana', 'Bárbara', 'Caio', 'Dênis']
notas = [89, 57, 60, 28]
print(atribuir_notas(alunos, notas))