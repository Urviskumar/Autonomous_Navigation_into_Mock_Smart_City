import cv2
import numpy as np
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

        # Check if masks are available
        if results[0].masks is not None:
            # Extract the segmentation masks
            masks = results[0].masks.data.cpu().numpy()

            # Initialize an empty frame to draw the edges
            edge_frame = frame.copy()

            # Process each mask to find the edges
            for mask in masks:
                # Convert the mask to a binary image
                mask = (mask > 0.5).astype(np.uint8) * 255

                # Resize the mask to match the frame dimensions
                mask = cv2.resize(mask, (width, height))

                # Find the edges in the mask
                edges = cv2.Canny(mask, 100, 200)

                # Dilate the edges to make them more visible
                kernel = np.ones((3, 3), np.uint8)
                edges = cv2.dilate(edges, kernel, iterations=1)

                # Draw the edges on the frameROS2_Starter
                edge_frame[edges != 0] = [0, 0, 255]  # Draw edges in red color

            # Write the frame with edges to the output video
            out.write(edge_frame)
        else:
            # If no masks are detected, write the original frame to the output video
            out.write(frame)

    # Release the video capture and writer objects
    cap.release()
    out.release()

def main(args):
    # Load the trained YOLOv8 model
    model = YOLO(args.model)

    # Paths to the input and output videos
    input_video_path = 'test.mp4'
    output_video_path = 'output_edge_detected.mp4'

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