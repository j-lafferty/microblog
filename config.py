import os

class Config(object):
	SECRET_KEY = os.envrion.get('SECRET_KEY') or 'you-will-never-guess'
	