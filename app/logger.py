import logging
from logging.handlers import RotatingFileHandler
import configparser

def configure_logger(app):
    config = configparser.ConfigParser()
    config.read('config.ini')
    
    log_file = config.get('logger', 'LOG_FILE')
    log_level = config.get('logger', 'LOG_LEVEL').upper()
    
    handler = RotatingFileHandler(log_file, maxBytes=10000, backupCount=1)
    handler.setLevel(getattr(logging, log_level))
    formatter = logging.Formatter(
        '%(asctime)s %(levelname)s: %(message)s [in %(pathname)s:%(lineno)d]'
    )
    handler.setFormatter(formatter)
    app.logger.addHandler(handler)
    app.logger.setLevel(getattr(logging, log_level))
    
def get_logger():
    return logging.getLogger('flask.app')
