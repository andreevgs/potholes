import json

from ultralytics import YOLO

model = YOLO('weights/potholes.pt')
# model.predict(['data/pothole1.png', 'data/pothole2.png', 'data/pothole3.png'], save=True)
results = model(['data/pothole1.png', 'data/pothole2.png', 'data/pothole3.png'])

for i, r in enumerate(results):
    output = {'confidence': json.dumps(r.boxes.conf.tolist()), 'name': 'pothole'}
    print(f"Potholes on image {i+1}: {output}")