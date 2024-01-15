# Project Description
With using  YOLOv7 on video cameras detecting the occupancy time (with belongings, without human) of the seats in the library

<img src="https://github.com/asumansaree/Library-Seat-Occupancy-Detection/assets/58108789/13d2e3fe-6267-461d-a22e-45fe0fc92dcf" alt="image" width="700"/>

Detailed explanation about the project is in this document:
https://docs.google.com/document/d/1pJ2VXuCuY54If5JJqTePYmlqCHkCWHwM6suYYAaN2k4/edit?usp=sharing

Development Environment is Google Colab. Here is the ready-to use Colab Notebook
<a target="_blank" href="https://colab.research.google.com/github/asumansaree/Library-Seat-Occupancy-Detection">
  <img src="https://colab.research.google.com/assets/colab-badge.svg" alt="Open In Colab"/>
</a>

# System Architecture
<p align="center">
  <img src="https://github.com/asumansaree/Library-Seat-Occupancy-Detection/assets/58108789/be034d9b-d6bb-4861-ba98-8e97b2597222" alt="image" width="500" style="display: block; margin: 0 auto;"/>
</p>

# How to Run (Colab)
* Set your Colab environment with GPU
* Mount Google Drive (optional). Due to Colab deletes the uploaded files at some point, it is better to upload them once to the Drive and mount the Drive to Notebook.
  from google.colab import drive
  drive.mount ("/content/drive")
* Clone the repository
  $ !git clone https://github.com/asumansaree/Library-Seat-Occupancy-Detection.git
* Change the working directory
  $ %cd "Library-Seat-Occupancy-Detection"
* Install requirements
  $ !pip install -r requirements.txt
* Run the python code with optional arguments and weights. 0: class id for human, 56: class id for chair
  $ !python detect_and_track.py \
    --weights yolov7.pt \
    --source "/content/drive/MyDrive/ImageProcessing/seatOccupancyDetectionMiniTrainVideo.mp4" \
    --conf-thres 0.4 \
    --classes 0 56 \
    --name "YOLOV7_Library_Seat_Detection"
* To display the video, you have to made this conversion
  $ path = "/content/Library-Seat-Occupancy-Detection/runs/detect/YOLOV7_Library_Seat_Detection/"
    !ffmpeg -i {path + "seatOccupancyDetectionMiniTrainVideo.mp4"} -vcodec libx264 {path + "display.mp4"}
    from IPython.display import HTML
    from base64 import b64encode
    mp4 = open(path + 'display.mp4', 'rb').read()
    data_url = "data:video/mp4;base64," + b64encode(mp4).decode()
    HTML("""
    <video width=400 controls>
          <source src="%s" type="video/mp4">
    </video>
    """ % data_url)

# Sample Output
Output file will be created in the "/content/Library-Seat-Occupancy-Detection/runs/detect/YOLOV7_Library_Seat_Detection/{video.mp4}"
Output is in the mp4 format. For demonstration purposes in pdf document, it is included as image
<p align="center">
  <img src="https://github.com/asumansaree/Library-Seat-Occupancy-Detection/assets/58108789/058ee40d-9ef1-4c79-9c18-0fb316e30e46" alt="ImageProcessing_ProjectReport_AsumanSareERGUT-09" width="500" style="display: block; margin: 0 auto;"/>
</p>

# Contact
Contact me for any problem and question
asumansaree@gmail.com

# References
* https://github.com/RizwanMunawar/yolov7-object-tracking
* Anish Aralikatti et al 2020 J. Phys.: Conf. Ser. 1706 012149
* Redmon J, Divvala S, Girshick R and Farhadi A You Only Look Once: Unified, Real-Time Object 
  Detection 2016IEEE Conference on Computer Vision and Pattern Recognition (Las Vegas) pp 779-788 
* COCO 2017 dataset: http://cocodataset.org

