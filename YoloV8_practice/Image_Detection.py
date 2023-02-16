from ultralytics import YOLO

#instantiate the model object
model = YOLO("yolov8n.pt")

#detect on a image and save the results
results = model.predict(source="https://github.com/AndrewFelton23/Spiderweb_practice/blob/39d3fa14de106049d1c3f3eb8b40c8f4dfd9445e/YoloV8_practice/resource/test_image.jpg",save=True, show=True)  # save predictions as labels
boxes = results[0].boxes
for detected in boxes.cls:
    if detected == 0:
        print("human found")
    else:
        print("not human")



