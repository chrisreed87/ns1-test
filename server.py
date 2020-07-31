# [X] 1. accepts a POST to /messages, contents of the message should be a string
# [X] 2. response to the POST should be a SHA 
# [] 3. a get to /messages/<SHA> should return the message
# [X] 4. /metrics should return some kind of metrics
# [X] 5. Wrap it in a Dockerfile
# [] 6. README how to run


from flask import Flask, jsonify, request, abort
from flask_hashing import Hashing
from prometheus_flask_exporter import PrometheusMetrics

app = Flask(__name__)
hashing = Hashing(app)
metrics = PrometheusMetrics(app)

db = []


@app.route('/health')
def hello_world():
    return 'OK'


@app.route('/messages', methods=['POST'])
def post_messages():
  val_hash = hashing.hash_value(request.json['message'])
  message = {
    'id': val_hash,
    'message': request.json['message']
  }
  db.append(message)
  return jsonify({'digest': val_hash}), 201


@app.route('/messages', methods=['GET']) #TODO remove this endpoint when done debugging
def get_db():
  return jsonify({'db': db})


@app.route('/messages/<string:db_id>', methods=['GET'])
def get_messages(db_id):
  message = [message for message in db if message['id'] == db_id]
  return message[0] #TODO need to figure out how to filter just the message piece


if __name__ == '__main__':
    app.run(host='0.0.0.0')