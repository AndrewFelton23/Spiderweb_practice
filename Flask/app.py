from flask import Flask


app = Flask(__name__)

@app.route('/hello/<string:name>')
def hello_name(name):
   return 'Hello %s!' % name



if __name__ == '__main__':
    app.run(host='127.0.0.1',port=8080)

