class Eletro:
    def ligar(self):
        return "Ligando..."
    
class Camera:
    def bater_foto(self):
        return "Foto tirada!!"
    
class Celular(Eletro, Camera):
    pass

s =Celular()
print(s.ligar())
print(s.bater_foto())




    