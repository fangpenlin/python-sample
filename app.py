import os
import time
from flask import Flask
from flask import redirect

app = Flask(__name__)

@app.route('/')
def hello():
    return 'Hello World!'


@app.route('/loading.gif')
def loading_gif():
    time.sleep(10)
    return redirect('https://i.giphy.com/media/y1ZBcOGOOtlpC/200.gif')


@app.route('/longcat.jpg')
def longcat():
    return redirect('http://i0.kym-cdn.com/photos/images/facebook/000/002/110/longcat.jpg')


if __name__ == '__main__':
    # Bind to PORT if defined, otherwise default to 5000.
    port = int(os.environ.get('PORT', 5000))
    app.run(host='0.0.0.0', port=port)
