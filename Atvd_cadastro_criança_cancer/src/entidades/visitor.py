from .category import Category
from estrutura_ordem_nums.category_type import CategoryType
from utilidades.print_helper import list_item

class Visitor(Category):
    def __init__(self, genero, idade, encontrou):
        super().__init__(CategoryType.VISITOR)

        self.genero = genero
        self.idade = idade
        self.encontrou = encontrou

    def show_info(self):
        list_item("Gênero", self.genero)
        list_item("idade", self.idade)
        list_item("De onde que você ouviu falar da instiutição da casa da criança com cancer? ", self.encontrou)
        
