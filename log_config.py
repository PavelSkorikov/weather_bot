from functools import wraps
import logging

"""define classes for filtering messages by level"""

class InfoFilter(logging.Filter):
    def filter(self, rec):
        return rec.levelno == logging.INFO

class WarningFilter(logging.Filter):
    def filter(self, rec):
        return rec.levelno == logging.WARNING


"""configuring logging handlers"""
logger = logging.getLogger()
logger.setLevel(logging.DEBUG)
d_handler = logging.FileHandler('./logs/debug.log')
d_handler.setLevel(logging.DEBUG)
d_format = logging.Formatter('%(asctime)s - %(process)d-%(levelname)s-%(message)s')
d_handler.setFormatter(d_format)
logger.addHandler(d_handler)
i_handler = logging.FileHandler('./logs/info.log')
i_handler.setLevel(logging.INFO)
i_handler.addFilter(InfoFilter())
i_format = logging.Formatter('%(asctime)s - %(process)d-%(levelname)s-%(message)s')
i_handler.setFormatter(i_format)
logger.addHandler(i_handler)
w_handler = logging.FileHandler('./logs/warning.log')
w_handler.setLevel(logging.WARNING)
w_handler.addFilter(WarningFilter())
w_format = logging.Formatter('%(asctime)s - %(process)d-%(levelname)s-%(message)s')
w_handler.setFormatter(w_format)
logger.addHandler(w_handler)
e_handler = logging.FileHandler('./logs/error.log')
e_handler.setLevel(logging.ERROR)
e_format = logging.Formatter('%(asctime)s - %(process)d-%(levelname)s-%(message)s')
e_handler.setFormatter(e_format)
logger.addHandler(e_handler)

def log_error(logger):
    """decorator for logging exceptions"""
    def decorated(f):
        @wraps(f)
        def wrapped(*args, **kwargs):
            try:
                return f(*args, **kwargs)
            except Exception as e:
                if logger:
                    logger.exception(e)
        return wrapped
    return decorated
