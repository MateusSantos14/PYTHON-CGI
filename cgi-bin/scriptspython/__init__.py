import requests
import json

class TempoCalculo():
    def calcular(self,valor,atual, novo):
        atual = self.converternames(atual)
        novo=self.converternames(novo)
        if atual == "valor invalido" or novo == "valor invalido":
            return "select invalido"
        try:
            resultado = float(valor)
        except:
            return "valor invalido"
        valores = [1,60,60,24,30,12]

        if atual==novo:
            return resultado
        elif atual>novo:
            for x in range(atual,novo-1,-1):
                resultado = resultado * valores[x]
            return round(resultado,2)
        elif atual<novo:
            for x in range(atual+1,novo+1):
                resultado = resultado / valores[x]
            return round(resultado,2) 

    def converternames(self, nome):
        if nome=="segundo":
            return 0
        elif nome=="minuto":
            return 1
        elif nome=="hora":
            return 2
        elif nome=="dia":
            return 3
        elif nome=="mes":
            return 4
        elif nome=="ano":
            return 5
        else:
            return "valor invalido"  


class MetroCalculo:
    def calcular(self,valor,atual, novo):
        atual = self.converternames(atual)
        novo = self.converternames(novo)
        if atual == "valor invalido" or novo == "valor invalido":
            return "select invalido"
        try:
            resultado = float(valor)
        except:
            return "valor invalido"
        
        
        valores = [1,10,10,10,10,10,10]

        if atual==novo:
            return resultado
        elif atual>novo:
            for x in range(atual,novo,-1):
                resultado = resultado * valores[x]
            return round(resultado,2)
        elif atual<novo:
            for x in range(atual+1,novo+1):
                resultado = resultado / valores[x]
            return round(resultado,2)
        pass

    def converternames(self, nome):
        if nome=="mm":
            return 0
        if nome=="cm":
            return 1
        if nome=="dm":
            return 2
        if nome=="m":
            return 3
        if nome=="dam":
            return 4
        if nome=="hm":
            return 5
        if nome=="km":
            return 6
        else:
            return "valor invalido"

class MonetarioCalculadora:
    def calcular(self,valor,atual, novo):
        atual = self.converternames(atual)
        novo = self.converternames(novo)
        if atual == "valor invalido" or novo == "valor invalido":
            return "select invalido"
        try:
            resultado = float(valor)
        except:
            return "valor invalido"
        
        
        valores = [[1, self.pegarcotacao()],
                   [self.pegarcotacao(),1]]

        if atual<novo:
            resultado /= valores[atual][novo] 
        elif novo>atual:
            esultado *= valores[atual][novo]
        return round(resultado,2)

    def converternames(self, nome):
        if nome=="real":
            return 0
        if nome=="dolar":
            return 1
        else:
            return "valor invalido"
        pass
    
    def pegarcotacao(self):
        requisicao = requests.get('https://economia.awesomeapi.com.br/all/USD-BRL')
        cotacao = requisicao.json()

        return float(cotacao["USD"]["bid"])
