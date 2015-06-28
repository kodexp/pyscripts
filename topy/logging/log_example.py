__author__ = 'fzhang'
import logging

logging.basicConfig(level=logging.DEBUG,
                    format='%(asctime)s %(name)-12s %(levelname)-8s %(message)s',
                    datefmt='%m-%d %H:%M')
logging.warning('Watch out!') # will print a message to the console
logging.info('I told you so') # will not print anything
logging.debug("debug msg")