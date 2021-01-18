from flask import Flask
from redis import Redis
import os
app = Flask(__name__)
HOST = os.getenv('HOST', 'redis')
redis = Redis(host=HOST, port=6379)

@app.route('/')
def hello():
    count = redis.incr('hits')
    return 'Hello from Docker, This is Flask 1! I have been seen {} times.\n'.format(count)

if __name__ == "__main__":
    app.run(host="0.0.0.0", debug=True)
