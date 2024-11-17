import argparse
from ultralytics import YOLO

def main(args):
    # Load a pre-trained YOLOv8 model
    model = YOLO(args.model)

    # Train the model on your dataset
    model.train(
        data=args.data,
        epochs=args.epochs,
        imgsz=800,
        batch=args.bacth,
        workers=4,
        device=0  # Use GPU if available
    )

if __name__ == "__main__":

    parser = argparse.ArgumentParser()
    parser.add_argument(
        '-d', '--data', 
        type=str, 
        required=True, 
        help="Path to the dataset.yaml file"
    )
    parser.add_argument(
        '-m', '--model', 
        type=str,
        default='yolov8n-seg.pt',
        required=False, 
        help="Path to the model"
    )
    parser.add_argument(
        '-e', '--epochs', 
        type=int, 
        default=100,
        required=False, 
        help="Number of epochs"
    )
    parser.add_argument(
        '-b', '--batch', 
        type=int, 
        default=16,
        required=False, 
        help="Batch size"
    )
    args = parser.parse_args()
    main(args)
