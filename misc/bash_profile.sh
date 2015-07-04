#!/usr/bin/env bash
echo 'export PATH="$HOME/.pyenv/bin:$PATH"' >> /home/vagrant/.bash_profile
echo 'eval "$(pyenv init -)"' >> /home/vagrant/.bash_profile
echo 'eval "$(pyenv virtualenv-init -)"' >> /home/vagrant/.bash_profile
source /home/vagrant/.bash_profile