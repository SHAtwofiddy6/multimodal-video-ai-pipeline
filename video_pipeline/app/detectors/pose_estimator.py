from ultralytics import YOLO

pose_model = YOLO('yolov8n-pose.pt')  # Pretrained for human pose

def estimate_pose(frame):
    results = pose_model(frame)
    return results[0].keypoints.xy.cpu().numpy()  # Returns list of (x, y) coords
