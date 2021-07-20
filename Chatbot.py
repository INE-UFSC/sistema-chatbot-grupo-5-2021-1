from abc import ABC, abstractmethod
import random as r

class Bot(ABC):

    def __init__(self, nome, comandos: {}):
        self._nome = nome
        self._comandos = comandos

    @property
    def nome(self):
        return self._nome

    @nome.setter
    def nome(self,nome_bot):
        self._nome = nome_bot

    def mostra_comandos(self):
        pass

    @abstractmethod
    def executa_comando(self,cmd):
        pass

    @abstractmethod
    def boas_vindas(self):
        pass

    @abstractmethod
    def despedida(self):
        pass


class BotSonolento(Bot):
    def __init__(self, nome):
        self.__nome = nome
        self.__dict_comandos = {1: 'Bom dia',
                                2: 'Qual seu nome? ',
                                3: 'Como está se sentindo? ',
        4: 'Até mais'}

    @property
    def nome(self):
        return self.__nome
    @nome.setter
    def nome(self,nome):
        self.__nome = nome

    def mostra_comandos(self):
        return self.__dict_comandos

    def executa_comando(self,cmd):
        pass

    def boas_vindas(self):
        return ("Olá, eu sou o {}, e estou com bastante sono, então tenha calma".format(self.__nome))

    def despedida(self):
        return ("Até mais! Vou aproveitar para dormir ")

bot1 = BotSonolento('soneca')
print(bot1.mostra_comandos())
print(bot1.boas_vindas())
print(bot1.despedida())
