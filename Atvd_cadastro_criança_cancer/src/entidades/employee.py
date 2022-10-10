from .category import Category
from estrutura_ordem_nums.category_type import CategoryType
from utilidades.print_helper import list_item

class Employee(Category):
    def __init__(self, rg, cpf, cargo):
        super().__init__(CategoryType.EMPLOYEE)

        self._rg = rg
        self._cpf = cpf
        self._cargo = cargo

    def show_info(self):
        list_item("Cargo profissional", self._cargo)
        list_item("RG", self._rg)
        list_item("CPF", self._cpf)
        
