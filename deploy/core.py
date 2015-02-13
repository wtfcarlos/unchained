from __future__ import unicode_literals
from __future__ import with_statement
import digitalocean
from . import settings

def create_droplet():

	ssh_keys = []

	if settings.ADD_SSH_KEYS:
		for path in settings.SSH_KEYPATHS:
			with open('path', 'r') as f:
				ssh_keys.append(f.read())

	print ssh_keys

	droplet = digitalocean.Droplet(
		token=settings.DIGITALOCEAN_TOKEN,
		name=settings.DROPLET_NAME,
		region=settings.DROPLET_REGION,
		image='django',
		size_slug=settings.DROPLET_SIZE_SLUG,
		backups=settings.ENABLE_BACKUPS
	)

	print droplet
