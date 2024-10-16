# Ordene as cartas por naipe e, dentro de cada naipe, por número
import operator

cartas = [
    { 'numero' : 4,
      'naipe' : 'copas' },
    { 'numero' : 8,
      'naipe' : 'copas' },
    { 'numero' : 5,
      'naipe' : 'copas' },
    { 'numero' : 4,
      'naipe' : 'ouro' },
    { 'numero' : 7,
      'naipe' : 'ouro' },
    { 'numero' : 2,
      'naipe' : 'espadas' },
    { 'numero' : 3,
      'naipe' : 'paus' },
    { 'numero' : 7,
      'naipe' : 'espadas' },
    { 'numero' : 7,
      'naipe' : 'paus' },
    { 'numero' : 8,
      'naipe' : 'paus' },
]

# Implemente aqui sua ordenação

cartas_ordenadas = sorted(cartas, key=operator.itemgetter('naipe', 'numero'))

# Exibe as cartas ordenadas
for carta in cartas_ordenadas:
    print(f'{carta["numero"]} de {carta["naipe"]}')




