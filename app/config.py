import configparser

def configure_app(app):
    config = configparser.ConfigParser()
    config.read('config.ini')
    
    app.config['DEBUG'] = config.getboolean('flask', 'DEBUG')
    # app.config['SECRET_KEY'] = config.get('flask', 'SECRET_KEY')
