from ultralytics import YOLO
from ultralytics.models.yolo.detect.predict import DetectionPredictor
import cv2

model = YOLO(r"C:\Users\Fachri B\OneDrive\Desktop\KULIAH\TA\cobra8\cam\f9s.pt")

results = model.predict(source="0", show=True)

print(results)