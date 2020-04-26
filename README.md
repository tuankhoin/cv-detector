# Covy Detector

## Usage Instruction:

Requirements: `python 3` and `pip`.

To begin, clone this repo and `cd` to it.

### Using `virtualenv`

* Install: `pip3 install virtualenv`

* Creating a new environment inside folder: `virtualenv env`

* Activate virtual environment:
  * **Linux, MacOS**: `source env/bin/activate`

  * **Windows**: `"env\Scripts\activate.bat"`

This is to ensure that your package download will only used for this repo. If steps are not made, package installment will be installed for your whole device.

* Install all necessary dependencies: `pip3 install -r requirements.txt`

* Run: `python app.py`

### Using PowerShell Automated Script (Windows)

* Install/Open PowerShell

* Change directory: `Set-Location -Path "your\path\here"`

* Set execution to unrestricted: `Set-ExecutionPolicy Unrestricted`

* Run automated script: `.\environment.ps1`

### Using bash script (Mac/Linux)

* Activate permission: `chmod +x environment.sh`

* Run `./environment.sh`

### Using `pipenv`

* Install: `pip3 install pipenv`

* Installing dependencies: `pipenv install`

* Run: `python app.py`


### How to run `face-mask-detection` model

* Change directory: `cd to dir`

* Run the following command: `python3 keras_infer.py --img-mode 0 --video-path 0`

## Author: Couch Potatoes

* Tuan Khoi Nguyen
* Hoang Anh Ngo
* Thai Nam Hoang
* Le Ngoc Ha Vu
