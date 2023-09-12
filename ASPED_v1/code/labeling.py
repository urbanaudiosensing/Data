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

from defining_ellipse import create_ellipse
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
config_file = '../../../chan/mmdetection/configs/mask2former/mask2former_swin-s-p4-w7-224_8xb2-lsj-50e_coco.py'
checkpoint_file = './checkpoints/mask2former_swin-s-p4-w7-224_8xb2-lsj-50e_coco_20220504_001756-c9d0c4f2.pth'

# Build the model from a config file and a checkpoint file
model = init_detector(config_file, checkpoint_file, device = "cuda:0")

# Init visualizer
visualizer = VISUALIZERS.build(model.cfg.visualizer)
visualizer.dataset_meta = model.dataset_meta

########################## MODIFY HERE ##############################
# Defining Buffers
session = "Test_6282023"
station = "cadell"
camera = "GTgopro05"
num_recorder = 6
buffer_list = ['1m', '3m', '6m', '9m']
filenames = ["GH010001", "GH020001", "GH030001", "GH040001", "GH050001", "GH060001", "GH070001", "GH080001", "GH090001", "GH100001", "GH110010"]

# ---------------------------------------------
# Prediction + CSV function
def create_label(filenames, station = "techway4"):
  # ----------------------------------------
  EXTRACT_DIR = "./output_csv/" + session + "/" + camera

  # Create ellipses
  ells = create_ellipse(station)

  # video to capture
  for video in filenames:
    os.system("ffmpeg -i '/media/chan/{p}/{s}/{c}/{v}.MP4' -an -c:v copy './video/{s}/{c}/{v}_MUTED.MP4'".format(p = "My Passport", s = session, c = camera, v=video))
    vidcap = cv2.VideoCapture("./video/{s}/{c}/{v}_MUTED.MP4".format(s = session, c = camera, v= video))

    # -----------------------------
    # initialize starting frame number
    frameNum = 1

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

    # detect pedestrians within buffer
    while frameNum < 15901: # max = 86399
      # start_time = time.time()
      vidcap.set(1, frameNum)
      success, image = vidcap.read()

      if not success:
        print("Could not read video.")
        break

      # print("frame{:d} detected.".format(frameNum))
      # if frameNum == 100:
      #  break

      # 1. run mmdetect
      result = inference_detector(model, image)

      # 2. make list of detected persons above accuracy threshold
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

        # save bbox point if it intersects
        for j in range(4*num_recorder):
          if ells[j].contains(foot_bbox)[0]:
            intersect[j].append(foot_bbox)

      # 5. count the number of intersecting people for each buffer
      for i in range(4*num_recorder):
        intersect_counts[i] = len(intersect[i])

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
