# Covy Detector
<a name="web"></a>Website:  https://7e3fd93c.ngrok.io
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

## How to run different models implemented

### `face-mask-detection` model

* Change directory: `cd to dir`

* Run the following command: `python3 keras_infer.py --img-mode 0 --video-path 0`


### Motion heatmap tracking

* Change directory:  `cd to dir` 

* Add all necessary dependencies: `pip install -r requirements.txt`

* Run the script: `python heatmap.py -v %videopath%` 

### Social distancing tracking

* First, for the script to run successfully, `yolo3.weights` has to be downloaded and added to the `yolov3` directory. The file can be found [here](https://pjreddie.com/darknet/yolo/)

* Change directory `cd to dir`

* Add all necessary dependencies

* Change the respective directories for images and videos in the `SD_Alert_Image.py` and `SD_Alert_Video.py` if new images and videos are tested.

* Deploy the algorithm by either `python SD_Alert_Image.py`,  `python SD_Alert_Video.py` or `python SD_Alert_Camera.py`.

## Author: Couch Potatoes

* Tuan Khoi Nguyen
* Hoang Anh Ngo
* Thai Nam Hoang
* Le Ngoc Ha Vu
