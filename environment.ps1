pip3 install virtualenv

====CREATING NEW ENV====
virtualenv env

====ACTIVATE LOCAL ENVIRONMENT===
if ($IsWindows){
  "env\Scripts\activate.bat"
} else {
  source env/bin/activate
}

ECHO ====INSTALLING DEPENDENCIES====
pip3 install -r requirements.txt

ECHO ====NOW RUNNING IMPLEMENTATION====
python app.py

if ($IsWindows){
  explorer "localhost:5000"
} else {
  open "localhost:5000"
}
