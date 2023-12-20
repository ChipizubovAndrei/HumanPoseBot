from ultralytics import YOLO

MODEL_PATH = 'models/yolov8n-pose.pt'
poseEstimator = YOLO(MODEL_PATH)