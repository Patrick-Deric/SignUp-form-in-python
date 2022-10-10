from utilidades.print_helper import print_title_top, double_break_line, break_line, print_bar_top, print_title_bottom, print_bar_bottom, print_space, normal_error
from estrutura_ordem_nums.setup_option import SetupOption
from fact.person import create_person
from estrutura_dados.people import PeopleAvlTree

def init():
    print_title_top("Seja bem-vindo ao Menu da ONG 'Casa da Criança com cancer'")
    print_bar_top()

    people = PeopleAvlTree()
    stop = False

    while not stop:
        print_title_top("Menu")

        option = input(f"Escolha alguma opção: {double_break_line}{SetupOption.STOP_SYSTEM.value}) Sair do sistema; {break_line}{SetupOption.ADD_PERSON.value}) Cadastrar individuo; {break_line}{SetupOption.LIST_PEOPLE.value}) Listar pessoas ordenadas por nome e categorias; {break_line}{SetupOption.SEARCH_PERSON.value}) Buscar individuo por nome; {double_break_line}Resposta: ").strip()

        if option.isnumeric(): option = int(option)

        if option == SetupOption.STOP_SYSTEM.value: stop = True
        elif option == SetupOption.ADD_PERSON.value: people.add(create_person())
        elif option == SetupOption.LIST_PEOPLE.value: people.list()
        elif option == SetupOption.SEARCH_PERSON.value: people.search()
        else:
            print_space()
            normal_error("Opção inválida, tente novamente.")
            print_space()
            print_bar_top()

    print_bar_bottom()
    print_title_bottom("Muito obrigado e volte sempre.")
