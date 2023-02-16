from ultralytics import YOLO

#instantiate the model object
model = YOLO("yolov8n.pt")

#Streaming from a webcam
results = model.predict(source="",save=True, show=True)  # save predictions as labels
boxes = results[0].boxes
for detected in boxes.cls:
    if detected == 0:
        print("human found")
    else:
        print("not human")



