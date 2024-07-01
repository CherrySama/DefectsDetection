from ultralytics import YOLO
 
# 加载训练好的模型或者网络结构配置文件
# model = YOLO('yolov8s.pt')
model = YOLO('ultralytics/cfg/models/v8/yolov8s-ebm.yaml')

print(model.info(detailed=True))
