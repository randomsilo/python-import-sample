import logging

# setup logging for app
logging.basicConfig(
    filename='MyApp.log',
    level=logging.DEBUG,
    format='%(levelname)8s -- %(asctime)s -- %(message)s'
)

# import library, then turn on the logging
from liblogging.util import Example



# test class 
class MyApp():
    """ MyApp will test the logging """

    def __init__(self):
        """ init MyApp """
        self.anExample = Example.ExampleCls()
        self.anExample.debug()

    def call_example(self):
        """ call example class to see if library logging works """
        logging.debug("call self.anExample.member_function!")
        self.anExample.member_function()

# runner
if __name__ == '__main__':
    MyApp().call_example()
    