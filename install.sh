export localdir=`pwd`

pushd ${HOME}

mkdir -p ${HOME}/.config

dots=( xinitrc xprofile compton.conf synergy.conf aliases Xresources)
configs=( i3 termite polybar dunst)

for i in "${dots[@]}";
do
  if [ -f "${HOME}/.$i" ];
  then
    echo $i already exists
  else
    ln -s $localdir/$i ${HOME}/.$i
  fi
done

for i in "${configs[@]}";
do
  if [ -d "${HOME}/.config/$i" ];
  then
    echo $i already exists
  else
    ln -s $localdir/$i ${HOME}/.config/$i
  fi
done

echo "source $HOME/.aliases" >> $HOME/.bashrc
