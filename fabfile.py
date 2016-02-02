from fabric.api import cd, env, run, local, sudo, settings


env.user = 'pi'


def install_node(node_version, pi_version):
    if pi_version == '2':
        name = 'node-v{0}-linux-armv7l'.format(node_version)
    else:
        name = 'node-v{0}-linux-armv6l'.format(node_version)
    url = 'https://nodejs.org/dist/v{0}/{1}.tar.gz'.format(node_version, name)
    run('wget {0}'.format(url))
    run('tar -xvf {0}.tar.gz'.format(name))
    with cd(name):
        sudo('cp -R * /usr/local/')


def update_upgrade():
    sudo('apt-get update')
    sudo('apt-get upgrade -y')


def reboot():
    sudo('reboot')


def halt():
    sudo('halt')
