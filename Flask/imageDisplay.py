from flask import Flask, Response
import cv2


app = Flask(__name__)

@app.route('/img/')
def img_display():
    return Response(gen(),
                    mimetype='multipart/x-mixed-replace;boundary=frame')
def gen():
    #process the image
    img = cv2.imread("https://github.com/AndrewFelton23/Spiderweb_practice/blob/9215a9bb47fe94cd174a5c264a58d010ffe4e387/Flask/resources/test_image.jpg")
    #encode the image as a jpeg file
    _,enc_img = cv2.imencode('.jpg',img)
    #convert the coded image to bytes
    frame_img = enc_img.tobytes()
    #return the coded image as a flask response
    yield (b'--frame\r\n'
            b'Content-Type: image/jpeg\r\n\r\n' + frame_img +b'\r\n\r\n')


if __name__ == '__main__':
    app.run(host='127.0.0.1',port=8080)
