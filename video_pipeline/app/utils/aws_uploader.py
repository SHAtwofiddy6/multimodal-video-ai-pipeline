import boto3
import uuid
import json
import cv2

s3 = boto3.client('s3')
BUCKET = 'your-s3-bucket-name'

def upload_to_s3(frame, faces, poses, plates, vehicles, groups):
    key_id = str(uuid.uuid4())

    # Upload frame
    frame_path = f"/tmp/{key_id}.jpg"
    cv2.imwrite(frame_path, frame)
    s3.upload_file(frame_path, BUCKET, f'frames/{key_id}.jpg')

    # Upload metadata
    metadata = {
        'faces': faces,
        'poses': poses.tolist() if hasattr(poses, 'tolist') else poses,
        'plates': plates,
        'vehicles': vehicles,
        'groups': groups
    }
    s3.put_object(Bucket=BUCKET, Key=f'metadata/{key_id}.json', Body=json.dumps(metadata))
