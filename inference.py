import cv2
from ultralytics import YOLO
import argparse

def process_video(model, input_video_path, output_video_path):
    # Open the input video file
    cap = cv2.VideoCapture(input_video_path)

    # Get video properties
    width = int(cap.get(cv2.CAP_PROP_FRAME_WIDTH))
    height = int(cap.get(cv2.CAP_PROP_FRAME_HEIGHT))
    fps = cap.get(cv2.CAP_PROP_FPS)
    fourcc = cv2.VideoWriter_fourcc(*'mp4v')

    # Create a VideoWriter object to save the output video
    out = cv2.VideoWriter(output_video_path, fourcc, fps, (width, height))

    while cap.isOpened():
        ret, frame = cap.read()
        if not ret:
            break

        # Perform segmentation on the frame
        results = model(frame, verbose=False)

        # Visualize the results on the frame
        annotated_frame = results[0].plot()

        # Write the frame to the output video
        out.write(annotated_frame)

    # Release the video capture and writer objects
    cap.release()
    out.release()

def main(args):
    # Load the trained YOLOv8 model
    model = YOLO(args.model)

    # Paths to the input and output videos
    input_video_path = 'zed_test.mp4'
    output_video_path = 'output_segmentation_zed.mp4'

    # Process the video
    process_video(model, input_video_path, output_video_path)

if __name__ == "__main__":

    parser = argparse.ArgumentParser()
    parser.add_argument(
        '-m', '--model', 
        type=str,
        default='yolov8n-seg.pt',
        required=False, 
        help="Path to the model"
    )
    args = parser.parse_args()
    main(args)