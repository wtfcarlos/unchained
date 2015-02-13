from __future__ import with_statement
from fabric.api import *
from fabric.context_managers import shell_env
from deploy import create_droplet


"""
Base configuration
"""

def droplet():
	create_droplet()

def deploy():
	code_dir = '/home/django/{{ project_name }}'
	with cd(code_dir):
		with(shell_env(DJANGO_SETTINGS_MODULE='{{ project_name }}.settings.production')):
			run('git pull')
			run('pip install -r requirements.txt')
			run('./manage.py migrate')
			run('./manage.py collectstatic --noinput')
			run('service gunicorn restart')