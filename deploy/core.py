from __future__ import unicode_literals
from __future__ import with_statement
import digitalocean
import os
from . import settings

def get_all_droplets():
	return digitalocean.Manager(token=settings.DIGITALOCEAN_TOKEN).get_all_droplets()

def get_droplet_with_id(droplet_id):
	return digitalocean.Droplet().get_object(settings.DIGITALOCEAN_TOKEN, droplet_id)

def create_droplet():

	ssh_keys = []

	if settings.ADD_SSH_KEYS:
		for path in settings.SSH_KEYPATHS:
			path = os.path.expanduser(path)
			with open(path, 'r') as f:
				ssh_keys.append(f.read())
		ssh_keys += settings.SSH_FINGERPRINTS

	droplet = digitalocean.Droplet(
		token=settings.DIGITALOCEAN_TOKEN,
		name=settings.DROPLET_NAME,
		region=settings.DROPLET_REGION,
		image='django',
		size_slug=settings.DROPLET_SIZE_SLUG,
		ssh_keys=ssh_keys,
		backups=settings.ENABLE_BACKUPS
	)

	droplet.create()

	return droplet
