"""
    Use this file to fill-in your specific DigitalOcean deploy settings.

	It is very important that you DO NOT DISPLAY your DIGITALOCEAN_TOKEN publicly!
	
	PLEASE edit it out before uploading to a public repository.

"""

# Your DigitalOcean Personal Access Token. (Write permissions needed)
# You can get one at https://cloud.digitalocean.com/settings/applications
DIGITALOCEAN_TOKEN = 'Enter your token here.'

# The name your droplet will have (by default, the project's name)
DROPLET_NAME = '{{ project_name }}'

# The droplet's region. This string can be one of:
# NYC
# 'nyc1', 'nyc2', 'nyc3'
# AMSTERDAM
# 'ams1', 'ams2', 'ams3'
# SAN FRANCISCO
# 'sfo1'
# OTHERS
# 'sgp1', 'lon1'

DROPLET_REGION = 'nyc2'

# Your droplet's size. This string can be one of:
# '512mb', '1gb', '2gb', '4gb', '8gb', '16gb', '32gb', '48gb', '64gb'
DROPLET_SIZE_SLUG = '512mb'

# Enable weekly droplet backups - has an additional cost!
ENABLE_BACKUPS = False

# If enabled, the script goes through all the paths in SSH_KEYPATHS and adds them to the droplet
ADD_SSH_KEYS = False

# List of paths to any SSH Keys you would like to add to your droplet.
SSH_KEYPATHS = ['/path/to/ssh_key', ]

