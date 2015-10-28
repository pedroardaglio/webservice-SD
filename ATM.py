#!/usr/bin/env python
# -*- coding: utf-8 -*-
import urllib2
import sys
import json


class ATM():
    def __init__(self):
        self.host = None
        self.porta = None
        pass

    def checar_servico(self, servico):
        """ Verifica se o servico solicitado existe. """
        if servico in self._servicos:
            return True

        return False

    def executar_servico(self, args):
        """ Executa o servico solicitado """
        self.host = sys.argv[1]
        self.porta = sys.argv[2]
        servico = sys.argv[3]
        conta1 = int(sys.argv[4])

        if servico == "saque":
            valor = sys.argv[5]
            return self.saque(conta1, valor)
        elif servico == "deposito":
            valor = sys.argv[5]
            return self.deposito(conta1, valor)
        elif servico == "saldo":
            return self.saldo(conta1)
        elif servico == "transferencia":
            conta2 = int(sys.argv[5])
            valor = sys.argv[6]
            return self.transferencia(conta1, conta2, valor)
        else:
            return "Servico nao encontrado!"

    def saque(self, conta, valor):
        url_servico = "saque/" + str(conta) + "/" + valor
        self.realizar_requisicao(url_servico)
        return "Saque bem sucedido de RS " + valor + " na conta " + \
            str(conta) + "!"

    def deposito(self, conta, valor):
        url_servico = "deposito/" + str(conta) + "/" + valor
        self.realizar_requisicao(url_servico)
        return "Deposito bem sucedido de RS " + valor + " na conta " + \
            str(conta) + "!"

    def saldo(self, conta):
        url_servico = "saldo/" + str(conta)
        res_req = self.realizar_requisicao(url_servico)
        saldo = json.loads(res_req)["saldo"]
        return "O saldo atual do usuario " + str(conta) + " e RS " + str(saldo)

    def transferencia(self, conta_orig, conta_dest, valor):
        url_servico = "transferencia/" + str(conta_orig) + "/" + \
            str(conta_dest) + "/" + valor
        self.realizar_requisicao(url_servico)
        return "Transferencia bem sucedida de RS " + valor + " da conta " + \
            str(conta_orig) + " para a conta " + str(conta_dest) + "!"

    def realizar_requisicao(self, url_servico):
        url = ""
        if "http://" not in self.host:
            url = "http://" + self.host

        url = url + ":" + self.porta + "/" + url_servico

        requisicao = urllib2.urlopen(url)
        res = requisicao.read()
        requisicao.close()

        return res


# Se o programa tiver sendo rodado por um interpretador
if __name__ == "__main__":
    atm = ATM()
    print atm.executar_servico(sys.argv)
