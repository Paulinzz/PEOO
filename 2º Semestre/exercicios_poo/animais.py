from datetime import date

class Animal():
    def __init__(self, nome: str, ano: int, castrado: bool, vacinas: list[str] = None):
        self.nome = nome
        self.ano = ano
        self.idade = date.today().year - ano
        self.castrado = castrado
        self.vacinas = vacinas if vacinas is not None else [] 

    def vacinar(self, vacina):
        self.vacinas.append(vacina)


a = Animal("lula", 17, True, ["raiva", "tetano"] )

print("Antes", a.vacinas)
 
a.vacinar("anti-roubo")

print("depois", a.vacinas)

b = Animal("Sauan", 17, True)
b.vacinar("macaco")
print(f"Vacinas do b:", b.vacinas)