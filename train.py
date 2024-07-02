import sys
import argparse
import os
from ultralytics import YOLO

def main(opt):
    yaml = opt.cfg
    model = YOLO(yaml) 

    model.info()

    results = model.train(data='VOC_Aluminum.yaml',  # path to your data.yaml
                        epochs=200, 
                        imgsz=640, 
                        workers=8, 
                        batch=16,
                        )

def parse_opt(known=False):
    parser = argparse.ArgumentParser()
    # model structures yaml
    parser.add_argument('--cfg', type=str, default='ultralytics/cfg/models/v8/yolov8s-p2-bifpn.yaml', help='initial weights path')
    # pretrained weight
    parser.add_argument('--weights', type=str, default='yolov8s.pt', help='')

    opt = parser.parse_known_args()[0] if known else parser.parse_args()
    return opt

if __name__ == "__main__":
    opt = parse_opt()
    main(opt)