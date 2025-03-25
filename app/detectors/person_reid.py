pip install torchreid
# detectors/person_reid.py
import torchreid
import cv2
import numpy as np

model = torchreid.models.build_model(
    name='osnet_x1_0',
    num_classes=1000,
    pretrained=True
)
torchreid.utils.load_pretrained_weights(model, 'osnet_x1_0_imagenet.pth')
model.eval()

transform = torchreid.data.transforms.build_transform(
    model_name='osnet_x1_0',
    is_train=False
)

def extract_reid_embedding(frame, bbox):
    x1, y1, x2, y2 = bbox
    crop = frame[y1:y2, x1:x2]
    crop = cv2.resize(crop, (256, 128))
    tensor = transform(crop).unsqueeze(0)
    with torch.no_grad():
        embedding = model(tensor).squeeze().numpy()
    return embedding.tolist()
