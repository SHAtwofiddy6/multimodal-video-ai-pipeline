# Placeholder using YOLO; Replace with fine-tuned CompCars classifier if needed
from ultralytics import YOLO

vehicle_model = YOLO('yolov8n.pt')

def classify_vehicle(frame):
    results = vehicle_model(frame)
    vehicles = []
    for r in results[0].boxes.data.cpu().numpy():
        x1, y1, x2, y2, conf, cls = r
        if int(cls) in [2, 5, 7]:  # Car, Bus, Truck classes
            vehicles.append({'bbox': [int(x1), int(y1), int(x2), int(y2)], 'confidence': float(conf), 'label': int(cls)})
    return vehicles
