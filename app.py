from flask import Flask, render_template, request, jsonify
import os
import random

app = Flask(__name__)

# All possible moves in the game
choices = ["Rock", "Paper", "Scissors"]


@app.route("/")
def home():
    # Show the game page
    return render_template("index.html")


@app.route("/play", methods=["POST"])
def play():
    # Read the player's selection sent by the webpage
    data = request.get_json(silent=True) or {}
    choice = data.get("choice")

    # Accept only the three valid choices
    if choice not in ["1", "2", "3"]:
        return jsonify({"error": "Please choose Rock, Paper, or Scissors."}), 400

    # Turn the player's number into a move
    user_choice = choices[int(choice) - 1]

    # The computer randomly picks a move
    computer_number = random.randint(1, 3)
    computer_choice = choices[computer_number - 1]

    # Check who won this round
    if int(choice) == computer_number:
        result = "It's a Tie!"
    elif (
        (choice == "1" and computer_number == 3) or
        (choice == "2" and computer_number == 1) or
        (choice == "3" and computer_number == 2)
    ):
        result = "You Win!"
    else:
        result = "Computer Wins!"

    # Send the moves and result back to the webpage
    return jsonify({
        "user_choice": user_choice,
        "computer_choice": computer_choice,
        "result": result
    })


if __name__ == "__main__":
    # Use Render's port when hosted, or port 5000 on your computer
    port = int(os.environ.get("PORT", 5000))
    app.run(host="0.0.0.0", port=port, debug=False)
