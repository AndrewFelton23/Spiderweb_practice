from flask import Flask, Response
import cv2


app = Flask(__name__)

@app.route('/img/')
def img_display():
    return Response(gen(),
                    mimetype='multipart/x-mixed-replace;boundary=frame')
def gen():
    #process the image
    _capture = cv2.VideoCapture(0)
    #check if the image successfully opened
    if not _capture.isOpened():
        print("Unable to open video")
        exit()
    while (True):
        #capture the current frame
        success,frame = _capture.read()
        #check if the current frame was read correctly
        if not success:
            print("Unable to recieve frame (possibly end of stream)")
            break
        #encode the image as a jpeg file
        _,enc_img = cv2.imencode('.jpg',frame)
        #convert the coded image to bytes
        frame_img = enc_img.tobytes()
        #return the coded image as a flask response
        yield (b'--frame\r\n'
                b'Content-Type: image/jpeg\r\n\r\n' + frame_img +b'\r\n\r\n')


if __name__ == '__main__':
    app.run(host='127.0.0.1',port=8080)