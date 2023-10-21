import logging
import os

def logger_setup(logger_name=__name__, level=logging.INFO):
    # Define the log file path
    log_file = os.path.join(os.path.dirname(__file__), '..', '..', 'logs', 'project_logs.log')
    log_file = os.path.abspath(log_file)  # Convert to absolute path

    # Create a logger
    logger = logging.getLogger(logger_name)
    logger.setLevel(level)

    # If the logger has handlers, return it
    if logger.hasHandlers():
        return logger

    # Create a file handler for the logger with delay set to False
    handler = logging.FileHandler(log_file, delay=False)
    handler.setLevel(level)

    # Create a formatter and add it to the handler
    formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
    handler.setFormatter(formatter)

    # Add the handler to the logger
    logger.addHandler(handler)

    print(f'Logger setup complete. Log file: {os.path.basename(log_file)}')

    return logger