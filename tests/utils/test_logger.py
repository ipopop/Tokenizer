import os
import time
from src.utils.logger_setup import logger_setup
import unittest

class TestLogging(unittest.TestCase):
    def setUp(self):
        self.logger = logger_setup()

    def tearDown(self):
        pass  # No need to delete the log file here
            
    def test_log_message(self):
        message = 'Test log message'
        self.logger.info(message)
        self.logger.handlers[0].flush() 
        time.sleep(0.1)  # Wait for the logger to write the message
        with open(self.logger.handlers[0].baseFilename, 'r') as file:
            log_content = file.read()
            self.assertIn(message, log_content)