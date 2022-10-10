from .category import Category
from estrutura_ordem_nums.category_type import CategoryType
from utilidades.print_helper import list_item

class Donor(Category):
    def __init__(self, metodo_pagamento, quantidade_a_doar, permissao):
        super().__init__(CategoryType.DONOR)

        self.metodo_pagamento = metodo_pagamento
        self._quantidade_a_doar = quantidade_a_doar
        self._permissao = permissao

    def show_info(self):
        list_item("Metodo de pagamento", self.metodo_pagamento)
        list_item("Quantidade que queira doar", self._quantidade_a_doar)
        list_item("Temos permissão para incluir seu nome na lista de doadores em nosso website? Sim ou Não? ", self._permissao)
