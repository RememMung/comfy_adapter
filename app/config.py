import configparser

def configure_app(app):
    config = configparser.ConfigParser()
    config.read('config.ini')
    
    app.config['DEBUG'] = config.getboolean('flask', 'DEBUG')
    # app.config['SECRET_KEY'] = config.get('flask', 'SECRET_KEY')

    app.config['REDIS_HOST'] = config.get('redis', 'HOST')
    app.config['REDIS_PORT'] = config.getint('redis', 'PORT')
    app.config['REDIS_DB'] = config.getint('redis', 'DB')