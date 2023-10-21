import logging

def logger_setup(log_file):
    # Create a logger
    logger = logging.getLogger(__name__)
    logger.setLevel(logging.INFO)

    # Create a file handler for the logger
    handler = logging.FileHandler(log_file)
    handler.setLevel(logging.INFO)

    # Add the handler to the logger
    logger.addHandler(handler)

    return logger