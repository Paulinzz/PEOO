class Pessoa():
    def __init__(self, nome, pai, mãe, filhos):
        self.__nome = nome
        self.__pai = None
        self.__mãe = None
        self.__filhos = []

    @property
    def nome(self):
        return self.__nome
    
    @nome.setter
    def nome(self, nome):
        if nome != "" and nome != None:
            self.__nome = nome

    @property
    def pai(self):
        return self.__pai
    
    @pai.setter
    def pai(self, pai):
        if pai != "" and pai != None:
            self.__pai = pai

    @property
    def mãe(self):
        return self.__mãe
    
    @mãe.setter
    def mãe(self, mãe):
        if mãe != "" and mãe != None:
            self.__mãe = mãe

    @property
    def filhos(self):
        return self.__filhos
    
    @filhos.setter
    def filhos(self, filhos):
        if filhos != "" and filhos != None:
            self.__filhos = filhos

    def add_filho(self, filho):
        if isinstance(filho, Pessoa) and filho != None:
            self.__filhos.append(filho)

    
viuvo = Pessoa("Marcos")
filhoV = Pessoa("José")
viuva = Pessoa("Maria")
filhaV = Pessoa("Eduarda")

filhoV.pai = viuvo 
filhoV.mãe = filhaV

filhaV.mãe = viuva
filhaV.pai = filhoV

filhoMJ = Pessoa("Michael Jordan")
filhoMJ.pai = filhoV
filhoMJ.mãe = viuva

if filhoMJ.pai == filhaV.pai and filhoMJ.mãe == filhaV.mãe:
    print("irmãos")

print(f"A avó de Michael Jordan é {filhoMJ.pai.mãe.nome}")

filhoBH = Pessoa("bRUNO HENRIQUE")
filhoBH.pai = viuva
filhoBH.mãe = filhaV

if filhoBH.mãe.pai == filhoV:
    print("sou avô de mim mesmo")

    