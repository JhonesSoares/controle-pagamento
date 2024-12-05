import re
import csv
from pathlib import Path

class Validation:

    def validate_cpf(self, cpf: str, file_path: str) -> bool    :
        CPF = cpf.replace('.', '').replace('-', '')

        def validate_input(valor: str) -> bool: # Verifica se o valor é uma string
            if not isinstance(valor, str):
                return False
            padrao = r'^\d{11}$' # Define o padrão de regex para exatamente 11 dígitos
            if re.match(padrao, valor): # Verifica se o valor corresponde ao padrão
                return True
            return False

        def digit_iterator(digitos: str, contador: int) -> int:
            res = 0
            for digito in digitos:
                res += (int(digito) * contador)
                contador -= 1
            return int(res)
        
        def digit_calculation(iter: int) -> str:
            iter = (iter * 10) % 11
            digito = 0 if iter > 9 else iter
            return str(digito)
        
        def fist_digit(cpf: str) -> str:
            nine_digit = cpf[:9]
            countdown_timer = 10
            res = digit_iterator(nine_digit, countdown_timer)
            return digit_calculation(res)
        
        def second_digit(cpf: str) -> str:
            ten_digit = cpf[:9] + fist_digit(cpf)
            countdown_timer = 11
            res = digit_iterator(ten_digit, countdown_timer)
            return digit_calculation(res)
        
        if validate_input(CPF):
            cpf_calculation: str = f'{CPF[:9]}{fist_digit(CPF)}{second_digit(CPF)}'

            if CPF == cpf_calculation:
                try:
                    with open(file_path, mode="r", encoding='utf8') as file:
                        reader = csv.reader(file)
                        
                        for row in reader:
                            if row[1] == cpf:  # O CPF está na coluna 1 (índice 1)
                                print('\nCPF já tem cadastrado.')
                                return False
                    return True
                except FileNotFoundError:
                    return True     
            else:
                print(F'\nCPF INVÁLIDO\n')
                return False    
        else:
            print(f"\nCPF INCORRETO!\n")
            return False                


    def validate_email(self, email: str) -> bool:
        default_email = re.compile(r"^[\w\.-]+@[\w\.-]+\.\w+$")

        if default_email.match(email):
            return True
        print("\nEmail inválido! Formato esperado: exemplo@dominio.com\n")
        return False
    
    def validate_phone(self, phone: str) -> bool:
        telephone = phone.replace('+','').replace('(','').replace(')','').replace('-','').replace(' ','')
        
        # Exemplo de formato válido: 55 (11) 91234-5678 ou 5511912345678
        padrao_telefone = re.compile(r'^\+?55\s?\(?(\d{2})\)?\s?(9?\d{4})-?(\d{4})$')
        
        if padrao_telefone.match(telephone):
            return True
        
        print("\nTelefone inválido! Formato esperado: '+55 (92) 9 0000-9999'.\n")
        return False        




if __name__ == '__main__':

    CAMINHO_CSV = Path(__file__).parent.parent / 'BD_clientes.csv'

    validation = Validation()
    validation.validate_phone('5592993675964')