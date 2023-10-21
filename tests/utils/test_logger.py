import os
import logging
from src.utils.logger_setup import logger_setup
import unittest

class TestLogging(unittest.TestCase):
    def setUp(self):
        log_dir = os.path.join(os.path.dirname(__file__), '..', 'logs')
        os.makedirs(log_dir, exist_ok=True)
        self.log_file = os.path.join(log_dir, 'project_logs.log')
        self.logger = logger_setup(self.log_file)

    def tearDown(self):
        # Remove the log file after the test
        os.remove(self.log_file)

    def test_log_message(self):
        message = 'Test log message'
        self.logger.info(message)

        # Check if the log message is in the log file
        with open(self.log_file, 'r') as file:
            log_content = file.read()
            self.assertIn(message, log_content)