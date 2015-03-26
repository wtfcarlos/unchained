"""
    Use this file to fill-in your specific DigitalOcean deploy settings.

	It is very important that you DO NOT DISPLAY your DIGITALOCEAN_TOKEN publicly!
	
	PLEASE edit it out before uploading to a public repository.

"""

"""

Your DigitalOcean Personal Access Token. (Write permissions needed)
You can get one at https://cloud.digitalocean.com/settings/applications

"""
DIGITALOCEAN_TOKEN = '2fe35527df5e4398b18ada0f46b861199f15a675b120f23381d34c869016ed14'

"""
The name your droplet will have (by default, the project's name)
""" 

DROPLET_NAME = 'test'

"""
The droplet's region. This string can be one of:
NYC
'nyc1', 'nyc2', 'nyc3'
AMSTERDAM
'ams1', 'ams2', 'ams3'
SAN FRANCISCO
'sfo1'
OTHERS
'sgp1', 'lon1'
"""

DROPLET_REGION = 'nyc2'

"""

Your droplet's size. This string can be one of:
'512mb', '1gb', '2gb', '4gb', '8gb', '16gb', '32gb', '48gb', '64gb'

"""
DROPLET_SIZE_SLUG = '512mb'

"""
 Enable weekly droplet backups - has an additional cost!
"""
ENABLE_BACKUPS = False

""" 

If enabled, the script goes through all the names in in SSH_KEYPATHS and adds them to the droplet. 
It will also use all the SSH keys listed by name in the SSH_KEYNAMES setting.

"""

ADD_SSH_KEYS = True

"""
 List of paths to any NEW SSH Keys you would like to add to your droplet.

 If you have already added any of these SSH keys, list them by the name they have on your DigitalOcean Control Panel in SSH_KEYNAMES

 Example:
 SSH_KEYPATHS = ['~/.ssh/id_rsa.pub']

"""
SSH_KEYPATHS = []


"""
 List of SSH Key fingerprints that you would like to add to the droplet.
 These fingerprints must be the same as shown in your DigitalOcean Control Panel.

 https://cloud.digitalocean.com/ssh_keys

 Example:
 SSH_FINGERPRINTS = ['b3:49:55:64:fa:25:90:7f:85:85:fb:c8:1a:8f:99:21']

"""

SSH_FINGERPRINTS = ['b3:49:55:64:fa:25:90:7f:85:85:fb:c8:1a:8f:99:21']

