@echo off

pip3 install -r requirements.txt

set /p VideoPath="Your directory to input video. Incorrect path will result in attribute error: "
:: if !EXIST %VideoPath set /p VideoPath="Invalid path. Try again: "

python heatmap.py -v %VideoPath
