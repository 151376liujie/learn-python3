import threading
import time
from flask import Flask
from flask import request

app = Flask(__name__)


def inspect():
    print(threading.current_thread().name, "start work.", time.ctime())
    time.sleep(30)
    print(threading.current_thread().name, "work done.", time.ctime())


@app.route('/')
def hello_world():
    return 'OK'


@app.route('/form', methods=['GET'])
def form():
    print(request.args)
    name = request.args.get('name')

    return name


@app.route('/inspect')
def index():
    t = threading.Thread(target=inspect, args=(), name="t2")
    t.setDaemon(True)
    t.start()
    return 'OK'


if __name__ == '__main__':
    app.run(host="0.0.0.0", port=8888, debug=True)
