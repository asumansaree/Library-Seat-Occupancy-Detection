from google.colab import drive
drive.mount ("/content/drive")

!git clone https://github.com/asumansaree/Library-Seat-Occupancy-Detection.git

%cd "Library-Seat-Occupancy-Detection"

!pip install -r requirements.txt

# seatOccupancyDetectionMiniTrainVideo
# This cell runs approximately in 30-40 seconds for 21 second video: seatOccupancyDetectionMiniTrainVideo.mp4
!python detect_and_track.py \
--weights yolov7.pt \
--source "/content/drive/MyDrive/ImageProcessing/seatOccupancyDetectionMiniTrainVideo.mp4" \
--conf-thres 0.4 \
--classes 0 56 \
--name "YOLOV7_Library_Seat_Detection"


# The generated mp4 format is not as we want, we couldn't directly open it.
# So I apply a conversion, so that it can be both display in Colab and can be watch via download
# This conversion takes approximately 15 seconds for 21 second video: seatOccupancyDetectionMiniTrainVideo.mp4
path = "/content/Library-Seat-Occupancy-Detection/runs/detect/YOLOV7_Library_Seat_Detection/"
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











