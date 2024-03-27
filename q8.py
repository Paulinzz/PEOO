emergencias = {
    '190' : 'Polícia Militar',
    '193' : 'Bombeiros',
    '197' : 'Polícia Civil',
    '192' : 'SAMU'
}

# Exiba aqui os telefones no formato:
# 190 - Polícia Militar
# 193 - Bombeiros
import time

print("="*30)
print("===Emergencias:===")
print("="*30)

for numero, servico in emergencias.items():
    time.sleep(1)    
    print(f"{numero} - {servico}")

