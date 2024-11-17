from flask import Flask, request, jsonify

app = Flask(__name__)

@app.route('/chat', methods=['POST'])
def chat():
    data = request.get_json()

    if 'message' not in data:
        return jsonify({"error": "No message provided"}), 400

    message = data['message']

    chad_reponse = "Chad not available"

    return jsonify({"response": chad_reponse})


if __name__ == '__main__':
    app.run(debug=True)