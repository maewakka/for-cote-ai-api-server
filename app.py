from flask import Flask, request, jsonify, Response
from service.optimizator import Optimizator

app = Flask(__name__)

optimizator = Optimizator()

@app.route('/optimize', methods=['POST'])
def optimize_code():
    data = request.get_json()
    code = data.get("code")
    if code:
        optimized_code = optimizator.optimize_code(code)
        return Response(optimized_code, mimetype="text/plain")
    else:
        return jsonify({"error": "Code not provided"}), 400


if __name__ == '__main__':
    app.run()
