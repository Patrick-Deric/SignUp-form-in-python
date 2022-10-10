from abc import ABC, abstractmethod

class Category(ABC):
    def __init__(self, category_name):
        self._category_name = category_name

    @abstractmethod
    def show_info(self):
        print("Esse método deve ser implementado!")
