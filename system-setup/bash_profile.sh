#!/usr/bin/env bash
echo 'export PATH="$HOME/.pyenv/bin:$PATH"' >> /home/vagrant/.bash_profile
echo 'eval "$(pyenv init -)"' >> /home/vagrant/.bash_profile
echo 'eval "$(pyenv virtualenv-init -)"' >> /home/vagrant/.bash_profile

# Add aliases for students.
echo "alias dragonwarrior='cd /vagrant/trainee-area'" >> /home/vagrant/.bash_profile
echo "alias level-0='cd /vagrant/trainee-area/level-0-example'" >> /home/vagrant/.bash_profile
echo "alias level-1='cd /vagrant/trainee-area/level-1'" >> /home/vagrant/.bash_profile
echo "alias level-2='cd /vagrant/trainee-area/level-2'" >> /home/vagrant/.bash_profile
echo "alias level-3='cd /vagrant/trainee-area/level-3-creating-web-services/trainee-friends-api'" >> /home/vagrant/.bash_profile
echo "alias level-4='cd /vagrant/trainee-area/level-4'" >> /home/vagrant/.bash_profile
echo "alias level-5='cd /vagrant/trainee-area/level-5'" >> /home/vagrant/.bash_profile

source /home/vagrant/.bash_profile