#!/bin/bash

echo ====INSTALLING_DEPENDENCIES====

pip3 install -r requirements.txt

read -p vid_path="Your directory to input video: "

while [ ! -d "$vid_path" ]
do
read -p vid_path="Invalid path. Try again: "
done

echo  ====PROCESSING_HEATMAP====

python heatmap.py -v "$vid_path"
