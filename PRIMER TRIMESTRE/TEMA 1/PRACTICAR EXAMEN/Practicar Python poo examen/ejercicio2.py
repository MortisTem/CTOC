#Mini ejercicio 2.
#Crear una clase CuentaBancaria con atributos privados __titular y __saldo. 
#Si el saldo inicial es negativo, se pondrá a 0 y se mostrará un aviso.
#Crear una cuenta con saldo inicial negativo y luego realizar un depósito, un retiro y mostrar el saldo final.

class CuentaBancaria:
    def __init__(self, titular, saldo):
        self.__titular = titular
        self.__saldo = saldo
        if saldo < 0:
            self.__saldo = 0
            print("El saldo es negativo, tu saldo se ha modificado a 0.")

    def depositar(self, cantidad):
        self.__saldo += cantidad

    def retirar(self, cantidad):
        self.__saldo -= cantidad

cuenta1 = CuentaBancaria("Leo Messi", -2000)
cuenta1.depositar(1500)