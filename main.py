from flask import Flask, request, jsonify

from chad import Chad

app = Flask(__name__)

instances = {}
players = []

@app.route('/', methods=['GET'])
def index():
    return "Chad lives here."

@app.route('/chat', methods=['POST'])
def chat():
    data = request.get_json()

    if 'PlayerMessage' not in data:
        return jsonify({"error": "No message provided."}), 400

    if 'PlayerName' not in data:
        return jsonify({"error": "No player given! Command invalid."}), 401



    message = data['PlayerMessage']
    player = data['PlayerName']

    if player not in players:
        players.append(player)
        instances[player] = Chad()

    model = instances[player]

    if model is None:
        chad_response = "Chad not available"
    else:
        chad_response = model.talk(message)

    print(chad_response)

    return jsonify({"response": chad_response}), 400


@app.route('/reset', methods=['POST'])
def reset():
    data = request.get_json()

    if 'PlayerName' not in data:
        return jsonify({"error": "No player given! Command invalid."}), 401

    player = data['PlayerName']

    model = instances[player]

    model.reboot()
    print(f"AI reset for player: {player}")
    return jsonify({"reset": True}), 400

'''
@app.route('/init', methods=['POST'])
def init():
    data = request.get_json()

    if 'PlayerName' not in data:
        return jsonify({"error": "No player name given."}), 400

    player = data['PlayerName']

    if player not in players:
        print("Created player instance")
        players.append(player)
        instances[player] = Chad()
        return jsonify({"info": "Instance for player created on server"}), 400
    else:
        return jsonify({"info": "Player instance already exists on server"}), 400
'''

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')