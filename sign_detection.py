import torch
import cv2

model = torch.hub.load('ultralytics/yolov5', 'custom', path='model/best.pt')
cap = cv2.VideoCapture(0)

def detect_sign():
    ret, frame = cap.read()
    if not ret:
        return 'none'

    results = model(frame)
    labels = results.names
    if results.pred[0].shape[0]:
        return labels[int(results.pred[0][0][5])]
    return 'none'
