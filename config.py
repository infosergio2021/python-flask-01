class Config:
    SECRET_KEY='mIeyq-%ShCw4MbN~'

class DevelopmentConfig(Config):
    DEBUG = True

#diccionario con entornos de configuracion
config = {
    'development': DevelopmentConfig,
    'default': DevelopmentConfig
}