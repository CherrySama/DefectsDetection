"""
-------------------------------------------------
   @File Name:     config.py
   @Author:        Yinghao.He
   @Date:          2024/5/24
   @Description: configuration file
-------------------------------------------------
"""
from pathlib import Path
import sys
import streamlit as st

# Get the absolute path of the current file
file_path = Path(__file__).resolve() # E:\myObj\yolov5\ultralytics\config.py

# Get the parent directory of the current file
root_path = file_path.parent # E:\myObj\yolov5\ultralytics

# Add the root path to the sys.path list if it is not already there
if root_path not in sys.path:
    sys.path.append(str(root_path))
    
# Get the relative path of the root directory with respect to the current working directory
ROOT = root_path.relative_to(Path.cwd())

# Source
SOURCES_LIST = ["Image", "Video", "Webcam"]

# trained model weights config
DETECTION_MODEL_DIR = ROOT / 'runs' / 'detect_autodl'

YOLOv8s = "train16/weights/best.pt"
YOLOv8s_EMA = "train13/weights/best.pt"
YOLOv8s_BiFPN = "train14/weights/best.pt"
YOLOv8s_Mpdiou = "train18/weights/best.pt"
YOLOv8s_Mish = "train12/weights/best.pt"
YOLOv8s_EBM = "train19/weights/best.pt"

DETECTION_MODEL_LIST = [
    'YOLOv8s',
    'YOLOv8s_EMA',
    'YOLOv8s_BiFPN',
    'YOLOv8s_Mpdiou',
    'YOLOv8s_Mish',
    'YOLOv8s_EBM']

@st.cache_resource
def selectModel(type):
    if type == "YOLOv8s":
        return YOLOv8s
    if type == "YOLOv8s_EMA":
        return YOLOv8s_EMA
    if type == "YOLOv8s_BiFPN":
        return YOLOv8s_BiFPN
    if type == "YOLOv8s_Mpdiou":
        return YOLOv8s_Mpdiou
    if type == "YOLOv8s_Mish":
        return YOLOv8s_Mish
    if type == "YOLOv8s_EBM":
        return YOLOv8s_EBM