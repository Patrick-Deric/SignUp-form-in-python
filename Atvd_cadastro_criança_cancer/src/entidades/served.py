from .category import Category
from estrutura_ordem_nums.category_type import CategoryType
from utilidades.print_helper import list_item

class Served(Category):
    def __init__(self, salary, children_quantity, is_employed):
        super().__init__(CategoryType.SERVED)

        self._salary = salary
        self._children_quantity = children_quantity
        self._is_employed = is_employed

    def show_info(self):
        list_item("Salário", self._salary)
        list_item("Quantidade de filhos", self._children_quantity)
        list_item("Está empregado", self._is_employed)
