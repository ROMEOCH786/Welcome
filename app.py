from flask import Flask, request, Response
import requests
import time
import json

app = Flask(__name__)

def send_requests(key, token, number):
    url = 'http://abtalkapi.oneway-tech.com/credits/v3/ad/reward'

    headers = {
        'version': '167465',
        'token': token,
        'deviceid': key,
        'content-type': 'application/json; charset=UTF-8',
    }

    data = {
        "requestTime": 1702555980794,
        "sign": "TKyQ1b8oydBSd8wPxhUqFM4Vcc2IIXHT1PePm55ms1CvU3UvDtMHDS0d2OUHg/QN9u6vLd09qW1sQPiWfc6PjOVNkAyvJGp95S8t8TLDBJeQCgYXadkWJRjk0yPLeQE59hByKlIifzDMwCzcKzifG5m+WPLzIhW5kLYzcm+Y0g96gougnjpC3SSvEkDg9GiyQYeYoqTZ42nKZj2tkVb4fX8xP3Za2qnNU4gyhBQTOnVUlohqm2FZQrdfj7D+D0nndXtnZJ9XUlY0mChpBqzWbWx6ymqjBrjSseuWfzKOgmRwpeL0PzCwevgkWM3qeyJ/R8btUt/FR9XliSFt0FP2hw==",
        "creditAmount": 999,
        "projectId": "DT_2022102902",
    }

    flag = [False]  # Flag as a mutable list

    def generate():
        while not flag[0]:
            try:
                response = requests.post(url, json=data, headers=headers)
                response_json = response.json()
                yield json.dumps(response_json) + '\n'

                credit_amount = response_json.get('data', {}).get('creditsAmount')
                if credit_amount is not None and credit_amount >= number:
                    flag[0] = True
                    yield json.dumps({"message": "done"})

            except Exception as e:
                yield json.dumps({"error": str(e)}) + '\n'

            time.sleep(10)

    return generate()

@app.route('/send_requests', methods=['GET'])
def handle_request():
    key = request.args.get('key')
    token = request.args.get('token')
    number = int(request.args.get('number'))

    return Response(send_requests(key, token, number), content_type='application/json')

if __name__ == '__main__':
    app.run(debug=True, port=5000)
