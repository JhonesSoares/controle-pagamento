from abc import ABC



class Person(ABC):
    def __init__(self, *args, **kwargs) -> None:
        self.__name: str = args[0]
        self.__cpf: str = args[1]
        self.__phone: str = args[2]
        self.__email: str = args[3]

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




if __name__ == '__main__':

    cliente = Person('jhones', '123', '321', 'jhones@gmail')  
    cliente.set_cpf = 'marias'
    print(cliente.set_cpf)