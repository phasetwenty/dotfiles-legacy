#!/usr/bin/env python
#
# public-key.py: Puts your public key up on a remote host.
from getpass import getuser
from os import getenv, path
from socket import gethostname
import sys

try:
    from fabric.api import abort, cd, env, hide, puts, run
    from fabric.decorators import task
    from paramiko.rsakey import RSAKey
    from paramiko.ssh_exception import PasswordRequiredException
except ImportError:
    # Needed to pacify the IDE linter.
    PasswordRequiredException = None
    abort = cd = env = hide = puts = run = task = RSAKey = None

    sys.stderr.write('fabric is required to run this script. Install it with `pip install fabric`.')
    sys.exit(1)

KEY_FILENAME = 'id_rsa'
PATH_TO_KEYFILE = path.join('{}/.ssh/{}'.format(getenv('HOME'), KEY_FILENAME))


@task
def public_key():
    if not path.exists(PATH_TO_KEYFILE):
        abort('Required public key file does not exist. Create it with ssh-keygen.')

    comment = '{}@{}'.format(getuser(), gethostname().split('.')[0])
    pkey = None
    try:
        pkey = RSAKey.from_private_key_file(PATH_TO_KEYFILE)
    except PasswordRequiredException:
        abort('Keys with passphrases are not supported.')

    grep_cmd = 'grep {} "$HOME"/{}'.format(pkey.get_base64(), path.join('.ssh', 'authorized_keys'))
    grep = None
    with hide('everything'):
        grep = run(grep_cmd, warn_only=True)
    if grep.failed:
        with cd('"$HOME"'), hide('everything'):
            run('[ -d .ssh ] || (mkdir -p .ssh; chmod 700 .ssh)')
            key_entry = ' '.join((pkey.get_name(), pkey.get_base64(), comment))
            run('touch .ssh/authorized_keys')
            run('chmod 600 .ssh/authorized_keys')
            run('echo {} >> .ssh/authorized_keys'.format(key_entry))
    puts('Your public key is set up on {}.'.format(env.host_string))
