# Python code for Amazon Rekognition - Object Detection

import os
import boto3
import cv2
from typing import Tuple, List, Dict
from dotenv import load_dotenv
import numpy as np

# Load environment variables
load_dotenv()

# Constants
OUTPUT_DIR = "./data"
OUTPUT_DIR_IMAGES = os.path.join(OUTPUT_DIR, "images")
OUTPUT_DIR_LABELS = os.path.join(OUTPUT_DIR, "labels")
TARGET_CLASS = "Zebra"
VIDEO_PATH = "./zebras.mp4"
FRAME_SKIP = 10
MAX_LABELS = 10
MIN_CONFIDENCE = 50


def create_directories() -> None:
    """Create output directories if they don't exist."""
    os.makedirs(OUTPUT_DIR_IMAGES, exist_ok=True)
    os.makedirs(OUTPUT_DIR_LABELS, exist_ok=True)


def get_rekognition_client() -> boto3.client:
    """Create and return AWS Rekognition client."""
    return boto3.client(
        "rekognition",
        aws_access_key_id=os.getenv("AWS_ACCESS_KEY_ID"),
        aws_secret_access_key=os.getenv("AWS_SECRET_ACCESS_KEY"),
    )


def process_frame(
    frame: np.ndarray, frame_number: int, reko_client: boto3.client
) -> None:
    """Process a single frame for object detection."""
    h, w, _ = frame.shape

    # Convert frame to jpg
    _, buffer = cv2.imencode(".jpg", frame)
    image_bytes = buffer.tobytes()

    # Detect objects
    try:
        response = reko_client.detect_labels(
            Image={"Bytes": image_bytes},
            MaxLabels=MAX_LABELS,
            MinConfidence=MIN_CONFIDENCE,
        )
    except Exception as e:
        print(f"Error detecting labels: {e}")
        return

    # Write detections
    label_file = os.path.join(
        OUTPUT_DIR_LABELS, f"frame_{str(frame_number).zfill(6)}.txt"
    )
    with open(label_file, "w") as f:
        for label in response["Labels"]:
            if label["Name"] == TARGET_CLASS:
                for instance in label["Instances"]:
                    bbox = instance["BoundingBox"]
                    x1, y1 = bbox["Left"] * w, bbox["Top"] * h
                    width, height = bbox["Width"] * w, bbox["Height"] * h
                    f.write(f"0 {x1 + width / 2} {y1 + height / 2} {width} {height}\n")

    # Save frame
    cv2.imwrite(
        os.path.join(OUTPUT_DIR_IMAGES, f"frame_{str(frame_number).zfill(6)}.jpg"),
        frame,
    )


def main() -> None:
    """Main function to process video for object detection."""
    create_directories()
    reko_client = get_rekognition_client()

    cap = cv2.VideoCapture(VIDEO_PATH)
    frame_number = 0

    while True:
        cap.set(cv2.CAP_PROP_POS_FRAMES, frame_number)
        ret, frame = cap.read()
        if not ret:
            break

        process_frame(frame, frame_number, reko_client)
        frame_number += FRAME_SKIP

    cap.release()


if __name__ == "__main__":
    main()