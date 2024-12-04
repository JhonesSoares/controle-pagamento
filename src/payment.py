from abc import ABC
from dataclasses import dataclass
import csv
from pathlib import Path

class Payment:

    def register_payment(self, caminho: str) -> str:
        cpf_customer: str = input('\nDigite CPF do cliente que pagou: ')
        cpf_customer = cpf_customer.replace('.', '').replace('-', '')
        
        customers = []
        paid = False

        try:
            with open(caminho, mode='r', encoding='utf8') as file:
                reader = csv.reader(file)

                for row in reader:
                    if row[1] == cpf_customer:
                        row[4] = "PAGO"
                        print(f'\nPagamento efetuado para: {row[0]}')
                        paid = True
                    customers.append(row)

            if paid:
                with open(caminho, mode="w", encoding='utf8', newline="") as file:
                    writer = csv.writer(file)
                    writer.writerows(customers)

                print("Pagamento registrado com sucesso!\n")
            
            else:
                print("\nCliente não encontrado.\n")

        except FileNotFoundError:
            print('\nNenhum cliente cadastrado.\n')


    def remove_payment(self, caminho: str) -> str:
        cpf_customer: str = input('Digite CPF do cliente que pagou: ')
        cpf_customer = cpf_customer.replace('.', '').replace('-', '')    
        customers = []
        paid = True

        try:
            with open(caminho, mode='r', encoding='utf8') as file:
                reader = csv.reader(file)

                for row in reader:
                    if row[1] == cpf_customer:
                        row[4] = "NÃO PAGO"
                        print(f'\nPagamento removido para: {row[0]}')
                        paid = False
                    customers.append(row)

            if paid == False:
                with open(caminho, mode="w", encoding='utf8', newline="") as file:
                    writer = csv.writer(file)
                    writer.writerows(customers)

                print("Pagamento removido com sucesso!\n")
            
            else:
                print("\nCliente não encontrado.\n")
        
        except FileNotFoundError:
            print('\nNenhum cliente cadastrado.\n')


    def remove_payment_customers(self, caminho: str) -> str:
        #cpf_customer: str = input('Digite CPF do cliente que pagou: ')
        customers = []

        try:
            with open(caminho, mode='r', encoding='utf8') as file:
                reader = csv.reader(file)

                for row in reader:    
                    row[4] = "NÃO PAGO"
                    customers.append(row)
            
            with open(caminho, mode="w", encoding='utf8', newline="") as file:
                writer = csv.writer(file)
                writer.writerows(customers)

            print("\nPagamentos removidos para proximas cobranças!\n")
            
        except FileNotFoundError:
            print('\nNenhum cliente cadastrado.\n')



if __name__ == '__main__':

    CAMINHO_CSV = Path(__file__).parent.parent / 'BD_clientes.csv'

    payment = Payment()

    payment.register_payment(CAMINHO_CSV)