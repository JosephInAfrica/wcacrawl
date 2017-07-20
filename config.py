import os
basedir = os.path.abspath(os.path.dirname(__file__))

tempdir = {'us':basedir+'\\temp'+'\\us\\','uk':basedir+'\\temp'+'\\uk\\','canada':basedir+'\\temp'+'\\canada\\',}

class Config:
    SECRET_KEY = os.environ.get('SECRET_KEY') or 'hard to guess string'
    SQLALCHEMY_COMMIT_ON_TEARDOWN = True
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    SQLALCHEMY_DATABASE_URI = os.environ.get('DEV_DATABASE_URL') or \
        'sqlite:///' + os.path.join(basedir, 'data-dev.sqlite')

    @staticmethod
    def init_app(app):
        pass

class DefaultConfig(Config):
    pass


config={
    'default':DefaultConfig
}