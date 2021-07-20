from Bots.Bot import Bot

parar = False

class SistemaChatBot:
    def __init__(self,nomeEmpresa,lista_bots):
        self.__empresa=nomeEmpresa
        qtd = 0
        for i in range(len(lista_bots)):
            if isinstance(lista_bots[i], Bot):
                qtd += 1
        if qtd == len(lista_bots):
            self.__lista_bots=lista_bots
        self.__bot = None
    
    def boas_vindas(self):
        return "Olá, esse é o sistema de chatbots da empresa " + self.__empresa

    def mostra_menu(self):
        print("Os chat bots disponíveis no momento são: ")
        for i in range(len(self.__lista_bots)):
            print(str(i) + " - " + "Bot: " + self.__lista_bots[i].nome + " - " + self.__lista_bots[i].apresentacao())
    
    def escolhe_bot(self):
        print("Digite o número do chat bot desejado: ")
        numero = int(input())
        for i in range(len(self.__lista_bots)):
            if numero == i:
                self.__bot = self.__lista_bots[i]

    def mostra_comandos_bot(self):
        for chave in self.__bot.mostra_comandos():
            print(str(chave) + " - " + self.__bot.mostra_comandos()[chave])

    def le_envia_comando(self):
        global parar
        print("Digite o comando desejado (ou -1 fechar o programa sair): ")
        comando = int(input())
        if comando == -1:
            parar = True
        else:
            print(self.__bot.executa_comando(comando))

    def inicio(self):
        global parar
        self.boas_vindas()
        print()
        self.mostra_menu()
        print()
        self.escolhe_bot()
        print()
        self.__bot.boas_vindas()
        while parar == False:
            self.mostra_comandos_bot()
            print()
            self.le_envia_comando()
            print()
        print(self.__bot.despedida())

bot1 = BotSonolento("Soneca")
bot2 = BotCuriosidade("Curioso")
lista_bots = [bot1, bot2]
sistema = SistemaChatBot("Grupo5",lista_bots)
sistema.inicio()