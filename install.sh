export localdir=`pwd`

pushd ${HOME}

mkdir -p ${HOME}/.config

dots=( xinitrc xprofile compton.conf aliases Xresources)
configs=( i3 termite polybar )

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
  if [ -f "${HOME}/.config/$i" ];
  then
    echo $i already exists
  else
    ln -s $localdir/$i ${HOME}/.config/$i
  fi
done
