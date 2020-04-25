# Motion Heatmap Tracking

The script will read an input video and returns an output video of the heatmap.
This can be used to track movements and crowded level of an area, providing
necessary safety measurements.

## Usage Manual

**Requirements**: `python 3` and `pip`.

* Download the `.zip` file [here](https://drive.google.com/open?id=1kSEtI5MEojunHfjcPtobVMeabq6rS3MB), and extract them to your favored destination.

* `cd` to the directory that you have extracted.

* You can start running the script in the different ways:

### Manual CLI

* Add dependencies: `pip3 install -r requirements.txt`
* Run the script: `python heatmap.py -v %VideoPath$%`

### Automated Script

* **Windows**: run `run.bat`
* **Mac/Linux**:
  * Activate permission: `chmod +x run.sh`
  * Run `./run.sh`

A sample testing video is provided in `/frames/`.
