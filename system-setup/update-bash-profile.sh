#!/usr/bin/env bash
echo 'export PATH="$HOME/.pyenv/bin:$PATH"' >> /home/vagrant/.bash_profile
echo 'eval "$(pyenv init -)"' >> /home/vagrant/.bash_profile
echo 'eval "$(pyenv virtualenv-init -)"' >> /home/vagrant/.bash_profile

# Add aliases for students.
echo "alias dragonwarrior='cd /vagrant/training'" >> /home/vagrant/.bash_profile
echo "alias level-0='cd /vagrant/training/level-0-python-basics/dragon-warrior'" >> /home/vagrant/.bash_profile
echo "alias level-1='cd /vagrant/training/level-1-the-zen-of-python/dragon-warrior'" >> /home/vagrant/.bash_profile
echo "alias level-2='cd /vagrant/training/level-2-command-line-interfaces/dragon-warrior'" >> /home/vagrant/.bash_profile
echo "alias level-3='cd /vagrant/training/level-3-interacting-with-web-services/dragon-warrior'" >> /home/vagrant/.bash_profile
echo "alias level-4='cd /vagrant/training/level-4-creating-web-services/dragon-warrior'" >> /home/vagrant/.bash_profile
echo "alias level-5='cd /vagrant/training/level-5-creating-websites/dragon-warrior'" >> /home/vagrant/.bash_profile

source /home/vagrant/.bash_profile
chown vagrant:vagrant /home/vagrant/.bash_profile