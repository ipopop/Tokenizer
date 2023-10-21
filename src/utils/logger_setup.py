import logging

def logger_setup(log_file, logger_name=__name__, level=logging.INFO):
    # Create a logger
    logger = logging.getLogger(logger_name)
    logger.setLevel(level)

    # If the logger has handlers, return it
    if logger.hasHandlers():
        return logger

    # Create a file handler for the logger
    handler = logging.FileHandler(log_file)
    handler.setLevel(level)

    # Create a formatter and add it to the handler
    formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
    handler.setFormatter(formatter)

    # Add the handler to the logger
    logger.addHandler(handler)

    print(f'Logger setup complete. Log file: {log_file}')  # Add this line

    return logger