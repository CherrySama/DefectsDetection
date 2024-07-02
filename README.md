# 😶‍🌫️Defects Detection

## 📝Introduction

This project is a defect detection web UI based on the EBM-YOLOv8 model. 

EBM-YOLOv8 = YOLOv8(Backbone) + EMA(Neck) + BiFPN(Neck) + Alpha-MPDIou(Bbox. Loss) + Mish(Activation Function for Convolution)

![img](https://raw.githubusercontent.com/CherrySama/DefectsDetection/main/docs/EBM-YOLOv8.png)

## 😎Author 
   Yinghao He, a graduated student from the North University of China.

## 🎯How to start

### 📦Clone the repository:

   ```bash
   git clone https://github.com/CherrySama/DefectsDetection.git
   ```

### 🚀Install the required packages:

Pip install the ultralytics package including all [requirements](https://github.com/ultralytics/ultralytics/blob/main/pyproject.toml) in a [**Python>=3.8**](https://www.python.org/) environment with [**PyTorch>=1.8**](https://pytorch.org/get-started/locally/).

   ```bash
   pip install ultralytics
   pip install streamlit
   ```

### 🤯Usage:
#### Dataset:
this project do not have its own dataset, you can write your own dataset yaml cfg and put your dateset in the 'datasets' floder.
And if you want to use `train.py` to train your model, you should revise line12 in `train.py` to make sure that you could train your model successfully:
```python
    results = model.train(data='VOC_Aluminum.yaml',  # path to your data.yaml
                        epochs=200, 
                        imgsz=640, 
                        workers=8, 
                        batch=16,
                        )
```
##### Example usage: yolo train data=VOC_Aluminum.yaml
parent  
├── ultralytics  
└── datasets
#### Train the model:
#### CLI
you can train the YOLOv8 model with a yolo command:
```bash
yolo train --data data/defects.yaml --weights yolov8n.pt --epochs 300 --batch-size 16 --device 0 --project runs/train --name defects
```
`yolo` can be used for a variety of tasks and modes and accepts additional arguments, i.e. `imgsz=640`. See the YOLOv8 [CLI Docs](https://docs.ultralytics.com/usage/cli) for examples.
#### Python
you can also train the YOLOv8 model with a python script:
```python
import torch
from ultralytics import YOLO

model = YOLO("yolov8n.pt")  # load a pretrained model (recommended for training)

model.train(data="data/defects.yaml", epochs=200, batch-size=16, device=0, project="runs/train", name="defects")  # Train the model
metrics = model.val()  # evaluate model performance on the validation set
results = model("https://ultralytics.com/images/bus.jpg")  # predict on an image
path = model.export(format="onnx")  # export the model to ONNX format
```
or you can simply use the `train.py` script to train the model:
```bash
python train.py 
```
See YOLOv8 [Python Docs](https://docs.ultralytics.com/usage/python) for more examples.

### 🗺️Run the web UI:

   ```bash
   streamlit run demo.py
   ```
Open the web browser and visit `http://localhost:8501` to start the web UI.

## 😮‍💨Last words
This is my graduation project, I'll be glad that you could use it as your baseline model or just simply have a look.  
If you have any questions or suggestions, please feel free to contact me at the following Email address 925782272@qq.com or create a new issue.