class ContaBancaria:
    def __init__(self, titular, tipo, agencia, conta, saldo):
        self.titular = titular
        self.tipo = tipo
        self.agencia = agencia
        self.conta = conta
        self.saldo = saldo

    def exibirDadosConta(self):
        print(f"Titular: {self.titular}")
        print(f"Tipo de conta: {self.tipo}")
        print(f"Agência: {self.agencia}")
        print(f"Conta: {self.conta}")
        print(f"Saldo: {self.saldo}")

    def saque(self, valor):
        if self.saldo < valor:
            print('Saldo insuficiente')
        else:
            print(f"Realizando saque no valor de R${valor}")
            self.saldo -= valor

    def depositar(self, valor):
        print(f'Realizando depósito no valor de R${valor}')
        self.saldo += valor


if __name__ == '__main__':
    contaFilipe = ContaBancaria("Filipe", "Conta Corrente", "0001", 203040, 100)
    contaDaniel = ContaBancaria("Daniel", "Conta Poupança", "0002", 112233, 100)

    contaFilipe.exibirDadosConta()

    valorSaque = float(input('Digite o valor que deseja sacar:'))
    contaFilipe.saque(valorSaque)

    contaFilipe.exibirDadosConta()

    contaFilipe.depositar(40)

    contaFilipe.exibirDadosConta()