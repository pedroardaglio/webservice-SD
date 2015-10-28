#!/usr/bin/env python
# -*- coding: utf-8 -*-
import web
import json
import sys
from Conta import Conta


class Banco():
    def __init__(self):
        self._contas = []
        # Cria contas com ids de 1 ate 10, com saldo 1000
        for i in range(10):
            self._contas.append(Conta(i, 1000))

    def buscar_conta(self, conta):
        for i in self._contas:
            if i.get_id() == conta:
                return i

    def saldo(self, conta):
        return self.buscar_conta(conta).get_saldo()

    def saque(self, conta, valor):
        conta_temp = self.buscar_conta(conta)
        conta_temp.set_saldo(conta_temp.get_saldo() - valor)

    def deposito(self, conta, valor):
        conta_temp = self.buscar_conta(conta)
        conta_temp.set_saldo(conta_temp.get_saldo() + valor)

    def transferencia(self, conta_orig, conta_dest, valor):
        conta_orig_temp = self.buscar_conta(conta_orig)
        conta_dest_temp = self.buscar_conta(conta_dest)

        conta_orig_temp.set_saldo(conta_orig_temp.get_saldo() - valor)
        conta_dest_temp.set_saldo(conta_dest_temp.get_saldo() + valor)

# Padrao usado pela modulo importado web (ou web.py, como e' conhecido)
# Ele usa uma tupla para mapear as urls com classes, e verifica a url e a
# classe a chamar em pares.
# Usei regex para identificar a entrada.
urls = (
    '/saldo/([0-9]+)', 'saldo',

    '/saque/([0-9]+)/([0-9]+)', 'saque',

    '/deposito/([0-9]+)/([0-9]+)', 'deposito',

    '/transferencia/([0-9]+)/([0-9]+)/([0-9]+)', 'transferencia'
)
# Criando um banco "global"
banco = Banco()


class saldo:
    def GET(self, conta):
        conta = int(conta)
        saldo = banco.saldo(conta)
        return json.dumps({"saldo": saldo})


class saque:
    def GET(self, conta, valor):
        conta = int(conta)
        valor = int(valor)
        banco.saque(conta, valor)


class deposito:
    def GET(self, conta, valor):
        conta = int(conta)
        valor = int(valor)
        banco.deposito(conta, valor)


class transferencia:
    def GET(self, conta_orig, conta_dest, valor):
        conta_orig = int(conta_orig)
        conta_dest = int(conta_dest)
        valor = int(valor)
        banco.transferencia(conta_orig, conta_dest, valor)


class AppHostPorta(web.application):
    """ Sobrescrita para poder editar a porta. Veja documentacao do web.py
        para entender melhor """

    def run(self, host='127.0.0.1', porta=8080, *middleware):
        func = self.wsgifunc(*middleware)
        return web.httpserver.runsimple(func, (host, porta))

# Se o programa tiver sendo rodado por um interpretador
if __name__ == "__main__":
    host = "127.0.0.1"  # Padrao. Eh o localhost
    porta = None

    # Verificando se recebeu porta de entrada ou se usa a padrao do projeto
    if len(sys.argv) == 1:
        porta = int("8542")
    else:
        porta = int(sys.argv[1])

    app = AppHostPorta(urls, globals())
    app.run(host=host, porta=porta)
