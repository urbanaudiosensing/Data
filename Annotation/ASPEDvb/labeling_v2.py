# Check PyTorch Installation
import torch, torchvision
print("PyTorch Version: ",torch.__version__, "CUDA Available?: ",torch.cuda.is_available())

# Check MMDetection Installation
import mmdet
from mmdet.apis import inference_detector, show_result_pyplot
from mmdet.models.detectors import BaseDetector
from mmdet.apis import init_detector, inference_detector, DetInferencer
from mmdet.registry import VISUALIZERS
from mmdet.visualization import *
print("mmdet Version: ",mmdet.__version__)

# Check mmcv Installation
import mmcv
from mmcv.ops import get_compiling_cuda_version, get_compiler_version
from mmcv.image import imread, imwrite
from mmengine.runner import load_checkpoint
print(get_compiling_cuda_version())
print(get_compiler_version)

# CV2
import cv2

# Buffers
from shapely.geometry import Polygon, Point, MultiPolygon
from shapely.errors import GEOSException
from shapely.validation import make_valid
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

# color
import random

####################### Change the buffer file ########################
from defining_ellipse_07262023 import create_ellipse
#######################################################################

from defining_csvformat_v2 import create_header

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

########################## MODIFY HERE #############################
# Defining Buffers
session = "Test_7262023"
station = "CamC" #CamE
camera = "gopro07" # gopro03
num_recorder = 1
buffer_list = ['1m', '3m', '6m', '9m']
#first_date = "6282023"
#number_of_videos = 11
filenames = ["GH100001"]
#filenames = ["GH010001","GH020001","GH030001", "GH040001", "GH050001", "GH060001","GH070001","GH080001", "GH090001", "GH100001", "GH110001"]

#for i in range(1, number_of_videos+1):
# filename = first_date + '_video' + str(i)
# filenames.append(filename)

#print(filenames)
#######################################################################
# ---------------------------------------------
# Prediction + CSV function
def create_label(filenames, station = "CamA"):
  # ----------------------------------------
  EXTRACT_DIR = "../output_csv/" + session + "/" + camera
  
  # Create ellipses
  ells = create_ellipse(station)

  # video to capture
  for video in filenames:
    os.system("ffmpeg -i '/media/backup_SSD/ASPEDv2/{s}/Videos/{c}/{v}.MP4' -an -c:v copy '../video/{s}/{c}/{v}_MUTED.MP4'".format(p = "My Passport3", s = session, c = camera, v=video))
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

      ##########  1. run mmdetect 
      result = inference_detector(model, image)
      
      ##########  2. make list of detected persons 
      pred_thr = result.pred_instances.scores.cpu().numpy() >= threshold

      # Filter persons
      coco_person = 0
      person_thr = result.pred_instances.labels.cpu().numpy() == 0
      thr_person_filter = pred_thr*person_thr

      # Parse the persons result 
      parser = ["bboxes", "labels", "scores"]

      result_thr = {}
      for x in parser:
          result_thr[x] = result.pred_instances[x][thr_person_filter].cpu().numpy()

      ##########  3. initiate lists of number of detected person/car&bus for each buffer
      intersect = [[0]*4*num_recorder for i in range(4*num_recorder)]
      intersect_counts = [[0]*4*num_recorder for i in range(4*num_recorder)]
      view_list = [[0]*4*num_recorder for i in range(4*num_recorder)]

      for i in range(4*num_recorder):
        intersect[i] = []
        intersect_counts[i] = []
        view_list[i] = 0

      ##########  4. LABELING: save list of persons' bbox points & count ppl within buffer
      detected_person_n = len(result_thr["bboxes"])

      for x in range(detected_person_n):
        foot_loc_x = (result_thr["bboxes"][x][0] + result_thr["bboxes"][x][2])//2
        foot_loc_y = max(result_thr["bboxes"][x][1], result_thr["bboxes"][x][3])
        foot_bbox = Point(foot_loc_x, foot_loc_y)

        # save bbox point if it intersects
        for j in range(4*num_recorder): 
          if ells[j].contains(foot_bbox)[0]:
            intersect[j].append(foot_bbox)

      # count the number of intersecting people for each buffer
      for i in range(4*num_recorder):
        intersect_counts[i] = len(intersect[i])

      ########## 5. VIEW: save list of car&bus bbox points & check blocked view
      image = image.clip(0, 255).astype(np.uint8)
      palette = visualizer.dataset_meta.get('palette', None)
      data_sample = result

      coco_carbus = [2, 5] # car label: 2, bus label: 5

      if data_sample is not None:
        data_sample = data_sample.cpu()

      classes = visualizer.dataset_meta.get('classes', None)
      pred_instances = data_sample.pred_instances 
      pred_instances = pred_instances[pred_instances.scores > threshold]
      pred_instances = pred_instances[np.isin(pred_instances.labels.cpu().numpy(), coco_carbus)]

      # mask of vehicles
      if pred_instances is not None:

        masks = pred_instances.masks
        masks = masks.numpy()
        masks = masks.astype(bool)

        labels = pred_instances.labels

        max_label = int(max(labels) if len(labels) > 0 else 0)
        mask_color = palette if visualizer.mask_color is None \
                        else visualizer.mask_color
        mask_palette = get_palette(mask_color, max_label + 1)
        colors = [jitter_color(mask_palette[label]) for label in labels]

        # check overlap
        polygons = []
        
        for i, mask in enumerate(masks):
          contours, _ = bitmap_to_polygon(mask)
          polygons.extend([contours])

        overlaps = [False]*len(pred_instances)

        for i in range(len(polygons)):
          for poly in polygons[i]:
            contour = np.squeeze(poly)
            try:
              polygon = Polygon(contour)
            except ValueError:
              polygon = 0      
            
            if polygon != 0: 
              for j in range(4*num_recorder): 
                vertices = ells[j].get_verts()     # get the vertices from the ellipse object
                ellipse = Polygon(vertices)        # Turn it into a polygon

                try:
                  overlapping = ellipse.overlaps(polygon)
                except GEOSException:
                  polygon = make_valid(polygon)
                  overlapping = ellipse.overlaps(polygon)

                if overlapping:
                  view_list[j] = 1 
                  overlaps[i] = True
        
        overlaps = np.array(overlaps)
        overlaps_torch = torch.from_numpy(overlaps).bool()

        pred_instances = pred_instances[overlaps_torch]

        # if there is a bus among intersecting vehicles
        if labels is not None:
          if 5 in pred_instances.labels.cpu().tolist():
            cv2.imwrite(os.path.join(EXTRACT_DIR,video + "_bus_frame{:d}.jpg".format(frameNum)), image)

        # export frames that have cars intersecting with buses
        #if sum(overlaps) > 0:
        #  cv2.imwrite(os.path.join(EXTRACT_DIR,video + "_car_frame{:d}.jpg".format(frameNum)), image)

      ########### 6. export to csv
      intersect_counts.insert(0, frameNum)
      intersect_counts.extend(view_list)
      wr.writerow(intersect_counts)

      ########### 7. save some as images for testing purpose
      #if not frameNum%1000:
      #  cv2.imwrite(os.path.join(EXTRACT_DIR,video + "_frame{:d}.jpg".format(frameNum)), image)     # save frame as JPEG file

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
