
from ultralytics import YOLO

# Load the YOLOv8 model
model = YOLO("/home/urvish/yolov8/runs/segment/train12/weights/nano_best_augmented.pt")

# Export the model to TensorRT format
model.export(format="engine", dynamic=True, batch=8, workspace=4, int8=True, data="/home/urvish/yolov8/Dataset/augumented_yolo_dataset/dataset.yaml")