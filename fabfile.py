from __future__ import with_statement
from fabric.api import *
from fabric.context_managers import shell_env
from deploy import *

import time


"""
Base configuration
"""

def droplet_list():
	print get_all_droplets()

def droplet():
	code_dir = '/home/django/test'
	print "Creating Droplet..."
	droplet = create_droplet()
	print "Initializing Droplet with id %d..." % droplet.id
	
	while droplet.status != 'active':
		droplet = get_droplet_with_id(droplet.id)
		time.sleep(3)

	time.sleep(10)
	print 'Connecting to Droplet [%s]...' % droplet.ip_address

	env.hosts = [droplet.ip_address]
	env.user = 'root'
	with cd(code_dir):
		run('touch hello.txt')




def deploy():
	code_dir = '/home/django/test'
	with cd(code_dir):
		with(shell_env(DJANGO_SETTINGS_MODULE='{{ project_name }}.settings.production')):
			run('git pull')
			run('pip install -r requirements.txt')
			run('./manage.py migrate')
			run('./manage.py collectstatic --noinput')
			run('service gunicorn restart')