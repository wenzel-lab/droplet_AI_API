from ultralytics import YOLO as Yolo
from get_dimentions import get_dimentions

# initializing
model = Yolo("latest_weight.pt")
results = model.predict("empty_image.jpg", imgsz = 640, conf=0.9, max_det=500, verbose=False)
# model ready
print("AI started")

def detect_droplets(image, image_size, pixel_ratio):
    results = model.predict(image, imgsz=max(image_size), conf=0.75, max_det = 500, verbose=False)
    diameter, diameter_stats, volume, volume_stats = get_dimentions(results, pixel_ratio)
    return diameter, diameter_stats, volume, volume_stats