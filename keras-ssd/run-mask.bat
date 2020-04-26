@echo off

pip install -r requirements.txt

:choice
set /P c=Are you running on video [Y/N]?
if /I "%c%" EQU "Y" goto :somewhere
if /I "%c%" EQU "y" goto :somewhere
if /I "%c%" EQU "N" goto :somewhere_else
if /I "%c%" EQU "n" goto :somewhere_else
goto :choice

:somewhere

SET /A image=0

:somewhere_else

SET /A image=1

:choice
set /P c=Are you running on webcam [Y/N]?
if /I "%c%" EQU "Y" goto :somewhere
if /I "%c%" EQU "y" goto :somewhere
if /I "%c%" EQU "N" goto :somewhere_else
if /I "%c%" EQU "n" goto :somewhere_else
goto :choice

:somewhere

python keras_infer.py --img-mode 0 --video-path 0

:somewhere_else

set /p VideoPath="Your directory to input video. Incorrect path will result in attribute error: "
python keras_infer.py --img-mode %image% --video-path %VideoPath%

pause
