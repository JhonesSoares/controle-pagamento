from abc import ABC
from dataclasses import dataclass
import csv
from pathlib import Path



@dataclass
class Person(ABC):
    __name: str
    __cpf: str
    __phone: str
    __email: str
    __status: str = 'NÃO PAGO'

    @property
    def set_cpf(self):
        return self.__name
    @set_cpf.setter
    def set_cpf(self, value):
        self.__name = value

    @property
    def set_cpf(self):
        return self.__cpf
    @set_cpf.setter
    def set_cpf(self, value):
        self.__cpf = value

    @property
    def set_phone(self):
        return self.__phone
    @set_phone.setter
    def set_phone(self, value):
        self.__phone = value

    @property
    def set_email(self):
        return self.__email
    @set_email.setter
    def set_email(self, value):
        self.__email = value    

    @property
    def set_status(self):
        return self.__status
    @set_status.setter
    def set_email(self, value):
        self.__status = value


class Customers(Person):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

    def find_client(self, file_path: str) -> str:
        cpf_name: str = input('\nDigite CPF ou Nome cliente: ')
        cpf_name = cpf_name.replace('.', '').replace('-', '')

        try:
            with open(file_path, mode="r", encoding='utf8') as file:
                reader = csv.reader(file)
        
                for row in reader:
                    
                    if row[0].lower() in cpf_name.lower() or row[1] == cpf_name:
                        print(f"\nNome: {row[0]}, CPF: {row[1]}, Telefone: {row[2]}, Email: {row[3]}, Status: {row[4]}\n")
                        return

        except FileNotFoundError:
            print("\nNenhum cliente cadastrado.\n")

    def paid_customer(self, file_path: str) -> str:
        try:
            with open(file_path, mode="r", encoding='utf8') as file:
                reader = csv.reader(file)
                num = 0
                for row in reader:
                    if row[4] == 'PAGO':
                        #print(f"\nNome: {row[0]}, CPF: {row[1]}, Telefone: {row[2]}, Email: {row[3]}, Status: {row[4]}\n")
                        num += 1
                        
                print(f'\n{num} Clientes PAGOS.\n')

        except FileNotFoundError:
            print("\nNenhum cliente cadastrado.\n")

    def no_paid_customer(self, file_path: str) -> str:
        try:
            with open(file_path, mode="r", encoding='utf8') as file:
                reader = csv.reader(file)
                num = 0
                for row in reader:
                    if row[4] == 'NÃO PAGO':
                        #print(f"\nNome: {row[0]}, CPF: {row[1]}, Telefone: {row[2]}, Email: {row[3]}, Status: {row[4]}\n")
                        num += 1
                print(f'\n{num} Clientes NÃO PAGOS.\n')

        except FileNotFoundError:
            print("\nNenhum cliente cadastrado.\n")

    def number_customers(self, file_path: str) -> str:
        try:
            with open(file_path, mode="r", encoding='utf8') as file:
                reader = csv.reader(file)

                for i, row in enumerate(reader):
                    i += 1

                print(f'\n{i} Clientes Cadastrados.\n')

        except FileNotFoundError:
            print("\nNenhum cliente cadastrado.\n")

    def delete_customers(self, file_path: str, removed_file_path: str) -> str:
        cpf_customer: str = input('Digite CPF do cliente: ')
        cpf_customer = cpf_customer.replace('.', '').replace('-', '')
            
        customers = []
        removed = []

        try:
            with open(file_path, mode="r", encoding='utf8') as file:
                reader = csv.reader(file)
                #reader = list(reader)

                for row in reader:

                    if row[1] == cpf_customer:
                        print(f"\nNome: {row[0]}, CPF: {row[1]}, Telefone: {row[2]}, Email: {row[3]}, Status: {row[4]}\n")
                        delete = input('Deletar cliente? [s]sim [n]não: ')
                        
                        if delete in 's':
                            removed.append(row)
                            with open(removed_file_path, mode="a", encoding='utf8', newline="") as file:
                                    writer = csv.writer(file)
                                    writer.writerows(removed)
                                                
                            del row
                            print("Cliente removido com sucesso!\n")
                            continue

                    customers.append(row) 

                    with open(file_path, mode="w", encoding='utf8', newline="") as file:
                        writer = csv.writer(file)
                        writer.writerows(customers)

        except FileNotFoundError:
            print("\nNenhum cliente cadastrado.\n")





if __name__ == '__main__':

    CAMINHO_CSV = Path(__file__).parent.parent / 'BD_clientes.csv'
    CAMINHO_CLIENTES_RMOVIDOS = Path(__file__).parent / 'clientes_removidos.csv'
    CAMINHO_ERRO = Path(__file__).parent / 'erro_menssage.csv'

    cliente = Customers('', '', '', '')  
    #cliente.set_cpf = 'marias'
    #cliente.find_client(CAMINHO_CSV)