from abc import ABC, abstractmethod


class BaseProduct(ABC):

    @classmethod
    @abstractmethod
    def new_product(cls, *args, **kwargs):
        pass


class ProductMixin:
    def __init__(self):
        print(repr(self))

    def __repr__(self):
        return f"{self.__class__}({self.name}, {self.description}, {self.price}, {self.quantity})"
