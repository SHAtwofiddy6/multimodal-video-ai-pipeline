from ultralytics import YOLO

face_model = YOLO('yolov8n-face.pt')  # Small face model

def detect_faces(frame):
    results = face_model(frame)
    faces = []
    for r in results[0].boxes.data.cpu().numpy():
        x1, y1, x2, y2, conf, cls = r
        faces.append({'bbox': [int(x1), int(y1), int(x2), int(y2)], 'confidence': float(conf)})
    return faces
