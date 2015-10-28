#!/usr/bin/env python
# -*- coding: utf-8 -*-


class Conta():
    def __init__(self, conta=None, saldo=0):
        self._id = conta
        self._saldo = saldo

    def set_id(self, id):
        self._id = id

    def get_id(self):
        return self._id

    def set_saldo(self, saldo):
        self._saldo = saldo

    def get_saldo(self):
        return self._saldo
