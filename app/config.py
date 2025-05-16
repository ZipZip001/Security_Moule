from flask import Flask

class Config:
    DEBUG = True
    TESTING = False
    SECRET_KEY = 'your_secret_key_here'
    JSON_SORT_KEYS = False

class DevelopmentConfig(Config):
    ENV = 'development'
    DEBUG = True

class TestingConfig(Config):
    ENV = 'testing'
    TESTING = True

class ProductionConfig(Config):
    ENV = 'production'
    DEBUG = False
    TESTING = False

config = {
    'development': DevelopmentConfig,
    'testing': TestingConfig,
    'production': ProductionConfig,
    'default': DevelopmentConfig
}