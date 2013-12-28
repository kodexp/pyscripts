"""
fabric is a system admin tool for sending commands to multiple hosts

fabfile.py for
cmd> fab memory_usage

must install fabric first
sudo apt-get install fabric
"""

from fabric.api import cd, env, prefix, run, task

env.hosts = ['localhost', '127.0.0.1']  # password ssh-able to these hosts

@task
def memory_usage():
    run('free -m')

@task
def deploy():
    with cd('/var/www/project-env/project'):
        with prefix('. ../bin/activate'):
            run('git pull')
            run('touch app.wsgi')