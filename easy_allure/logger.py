import logging

handler = logging.StreamHandler()
msg_format = '%(asctime)s %(name)-12s %(levelname)-8s %(message)s'
formatter = logging.Formatter(msg_format)
handler.setFormatter(formatter)

root_logger = logging.getLogger()
root_logger.addHandler(handler)
root_logger.setLevel(logging.INFO)


def get_logger(module_name: str) -> logging.Logger:
    return logging.getLogger(module_name)


def set_level(level: str) -> None:
    root_logger.setLevel(level)
