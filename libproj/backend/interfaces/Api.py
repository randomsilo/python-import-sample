from abc import ABC, abstractmethod

class IClientApi(ABC):
    """ class IClientApi """

    def __init__(self):
        print("init: IClientApi")

    def inherited_function1(self):
        """ inherited_function1 """
        print("inherited_function1: IClientApi")

    def inherited_function2(self):
        """ inherited_function2 """
        print("inherited_function2: IClientApi")

    @abstractmethod
    def must_implement_abs_method1(self):
        pass