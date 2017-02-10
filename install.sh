export localdir=`pwd`

pushd ${HOME}

mkdir -p ${HOME}/.config

dots=( xinitrc compton.conf i3blocks.conf )
configs=( i3 i3blocks termite polybar mpd )

for i in "${dots[@]}";
do
  if [ -f "$localdir/.$i" ];
  then
    echo $i already exists
  else
    ln -s $localdir/$i ${HOME}/.$i
  fi
done

for i in "${configs[@]}";
do
  if [ -f "$localdir/.config/$i" ];
  then
    echo $i already exists
  else
    ln -s $localdir/$i ${HOME}/.config/$i
  fi
done
