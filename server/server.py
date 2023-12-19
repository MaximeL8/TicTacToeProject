from flask import Flask, jsonify, request
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

def calculate_winner(squares, board_size):
    def check_direction(start, step):
        line = [start + step * i for i in range(board_size)]
        return all(squares[index] == start for index in line)

    for i in range(board_size):
        row_start = i * board_size
        if check_direction(squares[row_start], 1):
            return squares[row_start]

    for i in range(board_size):
        col_start = i
        if check_direction(squares[col_start], board_size):
            return squares[col_start]

    if check_direction(squares[0], board_size + 1):
        return squares[0]

    if check_direction(squares[board_size - 1], board_size - 1):
        return squares[board_size - 1]

    return None

@app.route("/calcul", methods=['GET', 'POST'])
def calculate():
    if request.method == 'GET':
        # Handle GET request for initial data
        # You can include the initial board size in the response
        return {"data" : {"boardSize" : "5"}}  # Adjust the default value as needed

    elif request.method == 'POST':
        # Handle POST request for game calculations
        data = request.get_json()
        squares = data.get('squares', [])
        board_size = int(data.get('boardSize', 3))

        # Implement your game logic here
        winner = calculate_winner(squares, board_size)

        # Return the result to the client
        return jsonify(winner=winner)

if __name__ == "__main__":
    app.run(debug=True)
