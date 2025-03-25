import cv2
from detectors.face_detector import detect_faces
from detectors.pose_estimator import estimate_pose
from detectors.license_plate_reader import read_plate
from detectors.vehicle_classifier import classify_vehicle
from utils.grouping import associate_faces_with_vehicles
from utils.aws_uploader import upload_to_s3

RTMP_URL = 'rtmp://your_server_ip/live/stream'

cap = cv2.VideoCapture(RTMP_URL)

frame_count = 0
while cap.isOpened():
    ret, frame = cap.read()
    if not ret:
        break

    faces = detect_faces(frame)
    poses = estimate_pose(frame)
    plates = read_plate(frame)
    vehicle_info = classify_vehicle(frame)

    group_data = associate_faces_with_vehicles(faces, plates, vehicle_info)

    upload_to_s3(frame, faces, poses, plates, vehicle_info, group_data)

    frame_count += 1
    if frame_count % 30 == 0:
        print(f"[INFO] Processed {frame_count} frames")

cap.release()
