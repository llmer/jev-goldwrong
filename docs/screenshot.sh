#!/bin/zsh
# Render each artboard in docs/canvas/ to a 2x PNG in docs/diagrams/ with headless Chrome.
# Usage: docs/screenshot.sh            (all artboards)
#        docs/screenshot.sh Bands      (one)
set -e
cd "$(dirname "$0")"
CHROME="/Applications/Google Chrome.app/Contents/MacOS/Google Chrome"
sizes=(Cover 1600x1000 Request 1600x900 Bands 1600x900 Cascade 1600x900 Precision 1600x900 Agreement 1600x900 Share 1600x900 Guidance 1600x900 Main 1600x900)
want=${1:-}
for ((i=1; i<=${#sizes[@]}; i+=2)); do
  name=${sizes[$i]}; size=${sizes[$((i+1))]}
  [[ -n "$want" && "$want" != "$name" ]] && continue
  lower=$(echo "$name" | tr '[:upper:]' '[:lower:]')
  "$CHROME" --headless=new --disable-gpu --hide-scrollbars --force-device-scale-factor=2 \
    --window-size="$size" --virtual-time-budget=6000 \
    --screenshot="diagrams/$lower.png" "file://$PWD/canvas/$name.dc.html" 2>/dev/null
  echo "diagrams/$lower.png"
done
