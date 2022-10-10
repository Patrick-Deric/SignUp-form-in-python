from estrutura_ordem_nums.category_number import CategoryNumber
from estrutura_ordem_nums.category_type import CategoryType

category_numbers_list = [category_number.value for category_number in CategoryNumber]
conflicted_category_error = f"A categoria {CategoryType.EMPLOYEE.value} ou {CategoryType.DONOR.value} não pode estar junto com a categoria {CategoryType.SERVED.value}"

def is_valid_category_number(category_number):
    return category_number in category_numbers_list

def get_invalid_categories(categories):
    return list(map(str, [category_number for category_number in categories if not is_valid_category_number(category_number)]))

def has_conflicted_category(categories):
    return (CategoryNumber.SERVED.value in categories) and ((CategoryNumber.EMPLOYEE.value in categories) or (CategoryNumber.DONOR.value in categories))
