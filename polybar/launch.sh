#!/usr/bin/env sh

# Terminate already running bar instances
killall -q polybar

# Wait until the processes have been shut down
while pgrep -x polybar >/dev/null; do sleep 1; done

# Launch bar1 and bar2
polybar -l info top &
polybar -l info bottom &
# polybar bar1 &
# polybar bar2 &

echo "Bars launched..."
