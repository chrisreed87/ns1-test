from flask import Flask, jsonify, request, abort
from flask_hashing import Hashing
from prometheus_flask_exporter import PrometheusMetrics

app = Flask(__name__)
hashing = Hashing(app)
metrics = PrometheusMetrics(app)

db = []


@app.route('/messages', methods=['POST'])
def post_messages():
  val_hash = hashing.hash_value(request.json['message'])
  message = {
    'id': val_hash,
    'message': request.json['message']
  }
  db.append(message)
  return jsonify({'digest': val_hash}), 201


@app.route('/messages/<string:db_id>', methods=['GET'])
def get_messages(db_id):
  message = [message for message in db if message['id'] == db_id]
  if len(message) == 0:
    return jsonify({"error": "unable to find message", "message_sha256": db_id }), 404
  return message[0]


if __name__ == '__main__':
    app.run(host='0.0.0.0')