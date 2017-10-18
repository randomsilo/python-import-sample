import logging

class ExampleCls():
    """ class ExampleCls """

    def __init__(self):
        self.logger = logging.getLogger('liblogging.util.Example.ExampleCls')
        self.logger.level = logging.CRITICAL
        self.logger.addHandler(logging.NullHandler)

    def debug(self):
        """ turn on debug """
        log_handler = logging.FileHandler('UtilExample.log')
        self.logger.setLevel(logging.DEBUG)
        log_formatter = logging.Formatter('%(levelname)8s -- %(asctime)s -- %(message)s')
        log_handler.setFormatter(log_formatter)
        self.logger.handlers = []
        self.logger.addHandler(log_handler)

    def member_function(self):
        """ member_function """
        self.logger.debug("Do Stuff")

