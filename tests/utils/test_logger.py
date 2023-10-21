import unittest
import os
from src.utils.logger_setup import logger_setup

class TestLogging(unittest.TestCase):
    def test_log_message(self):
        # Setup
        log_file = 'test_log.log'
        logger = logger_setup(log_file)

        # Log a message
        logger.info('Test message')

        # Check that the log file contains the message
        with open(log_file, 'r') as file:
            log_content = file.read()
        self.assertIn('Test message', log_content)

        # Remove log file if it exists
        if os.path.exists(log_file):
            os.remove(log_file)

        # Setup logger again for a new log file
        logger = logger_setup(log_file)

        # Log another message
        logger.info('Test message 2')

        # Check that the new log file contains the second message
        with open(log_file, 'r') as file:
            log_content = file.read()
        self.assertIn('Test message 2', log_content)

        # Remove log file if it exists
        if os.path.exists(log_file):
            os.remove(log_file)

if __name__ == '__main__':
    unittest.main()
