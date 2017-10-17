from libproj.backend.interfaces import Api

class MockClientApi(Api.IClientApi):
    """ class MockClientApi """

    def __init__(self):
        Api.IClientApi.__init__(self)
        print("init: MockClientApi")

    def mock_member_function(self):
        """ mock_member_function """
        print("mock_member_function: MockClientApi")

    def inherited_function2(self):
        """ inherited_function2 """
        print("inherited_function2: MockClientApi OVERRIDE")

    def must_implement_abs_method1(self):
        """ must_implement_abs_method1 """
        print("must_implement_abs_method1: MockClientApi IMPLEMENTED")