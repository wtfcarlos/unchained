from fabric.api import *

"""
Base configuration
"""
env.project_name = '{{ project_name }}'
env.database_password = ''
env.path = '/home/django/{{ project_name }}' % env

def setup():
	print 'hello'