
from ultralytics import YOLO

def main():
    # Load a pre-trained YOLOv8 model
    model = YOLO('yolov8n-seg.pt')

    # Train the model on your dataset
    model.train(
        data='/home/urvish/yolov8/Dataset/augumented_yolo_dataset/dataset.yaml',
        epochs=500,
        imgsz=800,
        batch=16,
        workers=4,
        device=0  # Use GPU if available
    )

if __name__ == "__main__":
    main()
