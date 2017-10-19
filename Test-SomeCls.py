import unittest

from libunittest.whatever import SomeApi


class TestSomeCls(unittest.TestCase):
    """ TestSomeCls """

    def test_some_cls_returns_true(self):
        """ test_some_cls_returns_true """
        inst_some_cls = SomeApi.SomeCls()
        self.assertTrue(inst_some_cls.returns_true())

if __name__ == '__main__':
    unittest.main()
