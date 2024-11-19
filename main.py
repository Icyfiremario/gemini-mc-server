from flask import Flask, request, jsonify

from chad import Chad

app = Flask(__name__)
model = Chad()

@app.route('/chat', methods=['POST'])
def chat():
    data = request.get_json()

    if 'message' not in data:
        return jsonify({"error": "No message provided"}), 400

    message = data['message']
    print(message)

    #chad_response = "Chad not available"
    chad_response = model.talk(message)

    print(chad_response)

    return jsonify({"response": chad_response})


@app.route('/reset', methods=['GET'])
def reset():
    model.reboot()
    return jsonify({"reset": True})

if __name__ == '__main__':
    app.run(debug=True)