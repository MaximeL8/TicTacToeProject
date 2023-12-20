import json
from flask import Flask, jsonify, request
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

LOG_FILE_PATH = 'game_logs.json'

def initialize_game_logs():
    # Clear the contents of the game logs file
    with open(LOG_FILE_PATH, 'w') as file:
        file.write('[]')

def load_game_logs():
    try:
        with open(LOG_FILE_PATH, 'r') as file:
            data = file.read()
            if not data:
                return []
            return json.loads(data)
    except FileNotFoundError:
        return []
    except json.decoder.JSONDecodeError:
        return []


def save_game_logs(logs):
    with open(LOG_FILE_PATH, 'w') as file:
        json.dump(logs, file, indent=2)

def check_winner(squares):
    # Get the dimensions of the board
    board_size = int(len(squares) ** 0.5)

    # Check rows, columns, and diagonals for a winner
    for i in range(board_size):
        # Check rows
        row_start = i * board_size
        if all(squares[row_start + j] == squares[row_start] for j in range(1, board_size)):
            return squares[row_start]

        # Check columns
        col_start = i
        if all(squares[col_start + j * board_size] == squares[col_start] for j in range(1, board_size)):
            return squares[col_start]

    # Check main diagonal
    if all(squares[i * (board_size + 1)] == squares[0] for i in range(1, board_size)):
        return squares[0]

    # Check anti-diagonal
    if all(squares[i * (board_size - 1)] == squares[board_size - 1] for i in range(1, board_size)):
        return squares[board_size - 1]

    # No winner
    return None

initialize_game_logs()

@app.route("/params", methods=['GET'])
def params():
    if request.method == 'GET':
        return {"data" : {"boardSize" : "3"}}

@app.route("/calculate", methods=['POST'])
def calculate():
    if request.method == 'POST':
        # Get the JSON data from the request body
        data = request.get_json()

        # Extract the 'squares' array from the received data
        squares = data.get('squares', [])

        # Check for a winner
        winner = check_winner(squares)

        # Log the game data
        game_log = {
            "squares": squares,
            "winner": winner
        }

        game_logs = load_game_logs()
        game_logs.append(game_log)
        save_game_logs(game_logs)

        # Respond with the result
        response_data = {"winner": winner}

        # Send the response as JSON
        return jsonify(response_data)

if __name__ == "__main__":
    app.run(debug=True)
