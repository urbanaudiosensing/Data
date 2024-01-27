# Check PyTorch Installation
import torch, torchvision
print("PyTorch Version: ",torch.__version__, "CUDA Available?: ",torch.cuda.is_available())

# Check MMDetection Installation
import mmdet
from mmdet.apis import inference_detector
from mmdet.models.detectors import BaseDetector
from mmdet.apis import init_detector, inference_detector, DetInferencer
from mmdet.registry import VISUALIZERS
print("mmdet Version: ",mmdet.__version__)

# Check mmcv Installation
from mmcv.ops import get_compiling_cuda_version, get_compiler_version
import mmcv
from mmengine.runner import load_checkpoint
import cv2
print(get_compiling_cuda_version())
print(get_compiler_version)

# Buffers
from shapely.geometry import Polygon, Point
from matplotlib.patches import Ellipse
import matplotlib.pyplot as plt
from matplotlib import patches, lines
import skimage.io
import copy
from array import *
import numpy as np
import os
import csv
import time

####################### Change the buffer file ########################
from defining_ellipse_0621 import create_ellipse
#######################################################################

from defining_csvformat import create_header

# get index of currently selected device
print("--------- Checking Torch GPU ---------")
print("Current device: ", torch.cuda.current_device()) # returns 0 in my case
# get number of GPUs available
print("Device count: ", torch.cuda.device_count())
# get the name of the device
print("Device name", torch.cuda.get_device_name(0))
print("--------- Checking Torch GPU ---------")

# Config & checkpoint
config_file = '../../../mmdetection/configs/mask2former/mask2former_swin-s-p4-w7-224_8xb2-lsj-50e_coco.py'
checkpoint_file = '../checkpoints/mask2former_swin-s-p4-w7-224_8xb2-lsj-50e_coco_20220504_001756-c9d0c4f2.pth'

# Build the model from a config file and a checkpoint file
model = init_detector(config_file, checkpoint_file, device = "cuda:0")

# Init visualizer
visualizer = VISUALIZERS.build(model.cfg.visualizer)
visualizer.dataset_meta = model.dataset_meta


########################## MODIFY HERE ##############################
# Defining Buffers
session = "Session_6212023"
station = "TechwayD"
camera = "Camera1_GTgopro04"
num_recorder = 2
buffer_list = ['1m', '3m', '6m', '9m']
#first_date = "6282023"
#number_of_videos = 11
filenames = ["GH010005", "GH020005", "GH030005", "GH040005", "GH050005", "GH060005", "GH070005", "GH080005", "GH090005"]

#for i in range(1, number_of_videos+1):
# filename = first_date + '_video' + str(i)
# filenames.append(filename)

#print(filenames)
#######################################################################

# Defining file format

# ---------------------------------------------
# Prediction + CSV function
def create_label(filenames, station = "techway4"):
  # ----------------------------------------
  EXTRACT_DIR = "../output_csv/" + session + "/" + camera
  
  # Create ellipses
  ells = create_ellipse(station)

  # video to capture
  for video in filenames:
    os.system("ffmpeg -i '/media/backup_SSD/ASPEDv1_Video/{s1}/{s2}/Video/{c}/{v}.MP4' -an -c:v copy '../video/{s1}/{c}/{v}_MUTED.MP4'".format(p = "My Passport", s1 = session, s2 = station, c = camera, v=video))
    #os.system("ffmpeg -i '/media/pavans/{p}/{s}/{c}/{v}.MP4' -an -c:v copy '/media/pavans/{p}/{s}/{c}/{v}_MUTED.MP4'".format(p = "My Passport1", s = session, c = camera, v = video))
    vidcap = cv2.VideoCapture("../video/{s}/{c}/{v}_MUTED.MP4".format(s = session, c = camera, v= video)) 

    # -----------------------------
    # initialize starting frame number
    frameNum = 0

    # detection threshold
    threshold = 0.7
    print("Current detection threshold: ", threshold)

    # Define Output File 
    output_file = os.path.join(EXTRACT_DIR, video + "_" + str(threshold) + ".csv")
    header = create_header(num_recorder, buffer_list)
    f = open(output_file, 'w', newline='')
    wr = csv.writer(f)
    wr.writerow(header)

    start_time = time.time()

    # define blue error screen color range
    lower_blue = np.array([110, 60, 0], dtype = "uint8") 
    upper_blue = np.array([130, 80, 0], dtype = "uint8") 

    # detect pedestrians within buffer
    while frameNum < 15901: # max = 86399
      # start_time = time.time()
      vidcap.set(1, frameNum)
      success, image = vidcap.read()
      
      if not success:
        print("Could not read video.")
        break

      # if frameNum == 100:
      #  break

      # 1. run mmdetect 
      result = inference_detector(model, image)
      #show_result_pyplot(model, image, result, score_thr=0.4)
      
      # 2. make list of detected persons
      # Filtering out unnecessary predictions
      # Filter based on scores
      pred_thr = result.pred_instances.scores.cpu().numpy() >= threshold

      # Filter out non-persons
      coco_person = 0
      person_thr = result.pred_instances.labels.cpu().numpy() == 0
      thr_person_filter = pred_thr*person_thr

      # Parse the result so that 
      # it contains only 'person' and 'thr >= 0.7'
      parser = ["bboxes", "labels", "scores"]

      result_thr = {}
      for x in parser:
          result_thr[x] = result.pred_instances[x][thr_person_filter].cpu().numpy()
      
      # print("frame{:d} detected.".format(frameNum))

      # 3. initiate lists of number of detected for each buffer
      intersect = [[0]*4*num_recorder for i in range(4*num_recorder)]
      intersect_counts = [[0]*4*num_recorder for i in range(4*num_recorder)]
      for i in range(4*num_recorder):
        intersect[i] = []
        intersect_counts[i] = []

      # 4. save list of bbox points
      detected_n = len(result_thr["bboxes"])

      for x in range(detected_n):
        foot_loc_x = (result_thr["bboxes"][x][0] + result_thr["bboxes"][x][2])//2
        foot_loc_y = max(result_thr["bboxes"][x][1], result_thr["bboxes"][x][3])
        foot_bbox = Point(foot_loc_x, foot_loc_y)
        # print(foot_bbox)

        # save bbox point if it intersects
        for j in range(4*num_recorder): 
          if ells[j].contains(foot_bbox)[0]:
            intersect[j].append(foot_bbox)

      # print("detected", detected)
      # print("intersect", intersect)

      # 5. count the number of intersecting people for each buffer
      for i in range(4*num_recorder):
        intersect_counts[i] = len(intersect[i])

      # 6. detect error screen
      # Create a binary mask of blue pixels
      mask = cv2.inRange(image, lower_blue, upper_blue)
      num_blue_pixels = cv2.countNonZero(mask)

      if num_blue_pixels > 150000:
        error = 1
      else:
        error = 0
      
      # 7. export to csv
      intersect_counts.insert(0, frameNum)
      intersect_counts.insert(1, error) 
      wr.writerow(intersect_counts)

      # 8. save some as images for testing purpose
      if not frameNum%1000:
        cv2.imwrite(os.path.join(EXTRACT_DIR,video + "_frame{:d}.jpg".format(frameNum)), image)     # save frame as JPEG file

      frameNum += 1

      current_time = time.time()
      print("Current Frame:", frameNum)
    
      # if (current_time - start_time) > (60*60*23):
      #   print("[INFO] Current time difference: ", current_time - start_time)
      #   break

    f.close()
    torch.cuda.empty_cache()

# Run
if __name__ == "__main__":
  torch.cuda.empty_cache()
  create_label(filenames, station = station)
