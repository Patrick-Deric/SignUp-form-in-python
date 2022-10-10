import re
from estrutura_ordem_nums.category_number import CategoryNumber
from estrutura_ordem_nums.category_type import CategoryType
from utilidades.print_helper import double_break_line, break_line, question, print_space, normal_error, separator, print_title_bottom, print_title_both, separate_items
from utilidades.categories_helper import get_invalid_categories, has_conflicted_category, conflicted_category_error
from utilidades.list_helper import has_len
from entidades.employee import Employee
from entidades.voluntary import Voluntary
from entidades.donor import Donor
from entidades.served import Served
from entidades.visitor import Visitor
# from memory_profiler import profile

class Person:
    def __init__(self, full_name, birth_date, phone, email):
        self._full_name = full_name
        self._birth_date = birth_date
        self._phone = phone
        self._email = email
        self._categories = []
        self._data = {}

    @property
    def full_name(self):
        return self._full_name

    @property
    def birth_date(self):
        return self._birth_date

    @property
    def phone(self):
        return self._phone

    @property
    def email(self):
        return self._email

    @property
    def categories(self):
        return sorted(self._categories)

    @property
    def data(self):
        return self._data.items()

    # @profile
    def add_categories(self):
        print_space()

        categories = question(
            f"Agora, digite separando por vírgulas os números das categorias de seu desejo para essa nova pessoa (exemplo: {CategoryNumber.EMPLOYEE.value}{separator}{CategoryNumber.VOLUNTARY.value}{separator}{CategoryNumber.VISITOR.value}):"
            f"{double_break_line}{CategoryNumber.EMPLOYEE.value} - {CategoryType.EMPLOYEE.value};"
            f"{break_line}{CategoryNumber.VOLUNTARY.value} - {CategoryType.VOLUNTARY.value};"
            f"{break_line}{CategoryNumber.DONOR.value} - {CategoryType.DONOR.value};"
            f"{break_line}{CategoryNumber.SERVED.value} - {CategoryType.SERVED.value};"
            f"{break_line}{CategoryNumber.VISITOR.value} - {CategoryType.VISITOR.value};"
            f"{double_break_line}Resposta: "
        )

        categories = re.findall('[0-9]+', categories.strip())
        has_value = bool(categories)

        if not has_value:
            print_space()
            normal_error()
            return self.add_categories()

        categories = [category_number for category_number in categories if category_number.isnumeric()]
        categories = list(map(int, categories))
        categories = list(dict.fromkeys(categories))

        if not has_len(categories):
            print_space()
            normal_error()
            return self.add_categories()

        invalid_categories = get_invalid_categories(categories)

        if has_len(invalid_categories):
            print_space()
            normal_error(f"Tente novamente, você digitou as seguintes categorias inválidas: {separate_items(invalid_categories)}")
            return self.add_categories()

        if has_conflicted_category(categories):
            print_space()
            normal_error(conflicted_category_error)
            return self.add_categories()

        for category_number in categories:
            category = None

            if category_number == CategoryNumber.EMPLOYEE.value: category = CategoryType.EMPLOYEE.value
            elif category_number == CategoryNumber.VOLUNTARY.value: category = CategoryType.VOLUNTARY.value
            elif category_number == CategoryNumber.DONOR.value: category = CategoryType.DONOR.value
            elif category_number == CategoryNumber.SERVED.value: category = CategoryType.SERVED.value
            elif category_number == CategoryNumber.VISITOR.value: category = CategoryType.VISITOR.value

            if category is not None: self._categories.append(category)

    # @profile
    def add_data(self):
        print_title_bottom("Chegou a hora de colocar as informações referentes a cada categoria adicionada anteriormente!")

        for category_type in self._categories:
            print_title_both(f"# {category_type}")

            category_person = None

            if category_type == CategoryType.EMPLOYEE.value:
                category_person = Employee(question("Digite o RG: "), question("Digite o CPF: "), question("Digite o cargo profissional: "))
            elif category_type == CategoryType.VOLUNTARY.value:
                category_person = Voluntary(question("Digite o bairro: "), question("Digite a cidade: "), question("Digite o estado: "))
            elif category_type == CategoryType.DONOR.value:
                category_person = Donor(question("Digite o tipo sanguíneo: "), question("Digite o presente para doação: "), question("Digite a altura: "))
            elif category_type == CategoryType.SERVED.value:
                category_person = Served(question("Digite o salário: "), question("Digite a quantidade de filhos: "), question("Digite se está empregado: "))
            elif category_type == CategoryType.VISITOR.value:
                category_person = Visitor(question("Digite o gênero: "), question("Digite se tem alergia: "), question("Digite se é casado: "))

            self._data[category_type] = category_person
