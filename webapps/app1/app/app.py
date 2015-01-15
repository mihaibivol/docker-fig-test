from flask import Flask
from redis import Redis
from common.lib import dummy

app = Flask(__name__)
redis = Redis(host="redis_1", port=6379)


@app.route('/')
def hello():
    redis.incr('hits_app1')
    div = "<div>%s</div>" % dummy.dummy()
    return div + 'Hello World app1! %s' % redis.get('hits_app1')


if __name__ == '__main__':
    app.run(host='0.0.0.0', debug=True)
