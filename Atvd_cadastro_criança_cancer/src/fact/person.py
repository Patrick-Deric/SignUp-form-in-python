from utilidades.print_helper import question, print_title_both, print_bar_bottom, print_bar_top
from entidades.person import Person

def create_person():
    print_bar_bottom()
    print_title_both(" Cadastro de nova pessoa")

    person = Person(
        question("- Nome completo: "),
        question("- Data de nascimento: "),
        question("- Telefone: "),
        question("- Email: ")
    )

    person.add_categories()
    person.add_data()

    print_title_both("Pessoa cadastrada com sucesso! Você voltará para o menu agora.")
    print_bar_top()

    return person
