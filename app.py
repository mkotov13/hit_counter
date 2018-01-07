from flask import Flask
from redis import Redis

app = Flask(__name__)
redis = Redis(host='localhost', port=6379)

@app.route("/count")
def hello():
    redis.incr('hits')
    return "Hey Stranger, you've seen this page {} times".format(int(redis.get('hits')))
  
if __name__ == "__main__":
    app.run()