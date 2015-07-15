#!/usr/bin/env bash

# Add PYENV and base Python versions
"export PYENV_ROOT=/opt/pyenv && curl -L https://raw.githubusercontent.com/yyuu/pyenv-installer/master/bin/pyenv-installer | bash"
"chown -R root:vagrant /opt"
su - vagrant -c "pyenv install 3.4.3"
su - vagrant -c "pyenv install 2.7.9"

# Create VirtualEnvs for Training Levels
su - vagrant -c "pyenv virtualenv 3.4.3 dragon-warrior"
su - vagrant -c "pyenv virtualenv 3.4.3 level-0"
su - vagrant -c "pyenv virtualenv 3.4.3 level-1"
su - vagrant -c "pyenv virtualenv 3.4.3 level-2"
su - vagrant -c "pyenv virtualenv 3.4.3 level-3"
su - vagrant -c "pyenv virtualenv 3.4.3 level-4"
