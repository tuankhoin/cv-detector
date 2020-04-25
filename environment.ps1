ECHO  ====CREATING_NEW_ENV====
pip3 install virtualenv
virtualenv env

ECHO  ====ACTIVATE_LOCAL_ENVIRONMENT====
if ($IsWindows -or $ENV:OS){
  "env\Scripts\activate.bat"
} else {
  source env/bin/activate
}

ECHO  ====INSTALLING_DEPENDENCIES====
pip3 install -r requirements.txt

ECHO  ====NOW_RUNNING_IMPLEMENTATION==== 
python app.py
