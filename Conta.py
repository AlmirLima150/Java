class Conta:
    def __init__(self, nome, numero_conta, saldo):
        self.nome = nome
        self.numero_conta = numero_conta
        self.saldo = saldo  
        
    def deposito(self, valor_deposito):
        self.saldo += valor_deposito
        print('Deposito realizado!')

    def saque(self, valor_saque):
        if self.cont > 3: 
            print('O limite de saques no dia foi atingido!')
        else:
            if valor_saque > self.saldo or valor_saque > 500:  
                print('Não é possível sacar o valor')
            else:
                self.saldo -= valor_saque
                self.cont += 1  
                print('Saque realizado!')
    
    def extrato(self):
        print(self.saldo)

class main:
    def __init__(self):
        self.conta1 = Conta('Almir', 1450, 0)

    def run(self):
        while True:
            print("\nMenu:")
            print("1. Deposito")
            print("2. Saque")
            print("3. Extrato")
            print("4. Sair")

            operacao = int(input("Escolha uma operação: "))

            if operacao == 1:
                valor_deposito = float(input('Digite o valor do depósito: '))
                self.conta1.deposito(valor_deposito)
            elif operacao == 2:
                valor_saque = float(input('Digite o valor do saque: '))
                self.conta1.saque(valor_saque)
            elif operacao == 3:
                self.conta1.extrato()
            elif operacao == 4:
                print("Encerrando o programa.")
                break
            else:
                print("Opção inválida.")

if __name__ == "__main__":
    main_program = main()
    main_program.run()
