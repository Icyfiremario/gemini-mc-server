from flask import Flask, request, jsonify

from chad import Chad

app = Flask(__name__)
#model = Chad()

instances = {}
players = []

@app.route('/', methods=['GET'])
def index():
    return "Chad lives here."

@app.route('/', methods=['GET'])
def index():
    return "Hello world"

@app.route('/chat', methods=['POST'])
def chat():
    data = request.get_json()

    #print(players)

    if 'PlayerMessage' not in data:
        return jsonify({"error": "No message provided."}), 400

    if 'PlayerName' not in data:
        return jsonify({"error": "No player given! Command invalid."}), 401



    message = data['PlayerMessage']
    player = data['PlayerName']

    if player not in players:
        players.append(player)
        instances[player] = Chad()
        #return jsonify({"error": "Instance for player not on server. Restarting the game should fix this."}), 400

    model = instances[player]

    if model is None:
        chad_response = "Chad not available"
    else:
        chad_response = model.talk(message)

    print(chad_response)

    return jsonify({"response": chad_response})


@app.route('/reset', methods=['GET'])
def reset():
    data = request.get_json()

    if 'PlayerName' not in data:
        return jsonify({"error": "No player given! Command invalid."}), 401

    player = data['PlayerName']

    model = instances[player]

    model.reboot()
    return jsonify({"reset": True})
    return jsonify({"reset": True})

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


#if __name__ == '__main__':
#    app.run(debug=True, host='0.0.0.0')