from google.colab import drive
drive.mount ("/content/drive")




!git clone https://github.com/RizwanMunawar/yolov7-object-tracking.git





%cd "yolov7-object-tracking"






!pip install -r requirements.txt








with open("/content/custom_detect_and_track.py", 'r') as file:
    modified_code = file.read()

# Save the modified code back to the 'detect_and_track.py' file
with open("/content/yolov7-object-tracking/detect_and_track.py", 'w') as file:
    file.write(modified_code)

print("Code saved back to detect_and_track.py.")

with open("/content/custom_sort.py", 'r') as file:
    modified_code2 = file.read()

# Save the modified code back to the 'detect_and_track.py' file
with open("/content/yolov7-object-tracking/sort.py", 'w') as file:
    file.write(modified_code2)

print("Code saved back to sort.py.")








# seatOccupancyDetectionMiniTrainVideo
!python detect_and_track.py \
--weights yolov7.pt \
--source "/content/drive/MyDrive/ImageProcessing/seatOccupancyDetectionMiniTrainVideo.mp4" \
--conf-thres 0.4 \
--classes 0 56 \
--name "YOLOV7_Object_Tracking"







path = "/content/yolov7-object-tracking/runs/detect/YOLOV7_Object_Tracking16/"
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













