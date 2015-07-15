#!/usr/bin/env bash
echo 'export PATH="/opt/pyenv/bin:$PATH"' >> /home/vagrant/.bash_profile
echo 'eval "$(pyenv init -)"' >> /home/vagrant/.bash_profile
echo 'eval "$(pyenv virtualenv-init -)"' >> /home/vagrant/.bash_profile

# Add aliases for students.
echo "alias dragonwarrior='cd /vagrant/trainee-area'" >> /home/vagrant/.bash_profile
echo "alias level-0='cd /vagrant/trainee-area/level-0-python-basics/trainee'" >> /home/vagrant/.bash_profile
echo "alias level-1='cd /vagrant/trainee-area/level-1-command-line-interfaces/trainee'" >> /home/vagrant/.bash_profile
echo "alias level-2='cd /vagrant/trainee-area/level-2-interacting-with-web-services/trainee'" >> /home/vagrant/.bash_profile
echo "alias level-3='cd /vagrant/trainee-area/level-3-creating-web-services/trainee'" >> /home/vagrant/.bash_profile
echo "alias level-4='cd /vagrant/trainee-area/level-4-creating-websites/trainee'" >> /home/vagrant/.bash_profile

source /home/vagrant/.bash_profile