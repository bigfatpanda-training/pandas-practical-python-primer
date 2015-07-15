#!/usr/bin/env bash
echo 'export PATH="/opt/pyenv/bin:$PATH"' >> /home/vagrant/.bash_profile
echo 'eval "$(pyenv init -)"' >> /home/vagrant/.bash_profile
echo 'eval "$(pyenv virtualenv-init -)"' >> /home/vagrant/.bash_profile

# Add aliases for students.
echo "alias dragonwarrior='cd /vagrant/workouts'" >> /home/vagrant/.bash_profile
echo "alias level-0='cd /vagrant/workouts/level-0-python-basics/dragon-warrior'" >> /home/vagrant/.bash_profile
echo "alias level-1='cd /vagrant/workouts/level-1-command-line-interfaces/dragon-warrior'" >> /home/vagrant/.bash_profile
echo "alias level-2='cd /vagrant/workouts/level-2-interacting-with-web-services/dragon-warrior'" >> /home/vagrant/.bash_profile
echo "alias level-3='cd /vagrant/workouts/level-3-creating-web-services/dragon-warrior'" >> /home/vagrant/.bash_profile
echo "alias level-4='cd /vagrant/workouts/level-4-creating-websites/dragon-warrior'" >> /home/vagrant/.bash_profile

source /home/vagrant/.bash_profile