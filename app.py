from flask import Flask, request, jsonify
from bot import handle_user_input

app = Flask(__name__)

# Define route for handling user input
@app.route('/chat', methods=['POST'])
def chat():
    user_input = request.json['user_input']
    bot_response = handle_user_input(user_input)
    return jsonify({'bot_response': bot_response})

if __name__ == '__main__':
    app.run(debug=True)
