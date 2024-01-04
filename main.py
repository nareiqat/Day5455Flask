from flask import Flask
import random

random_number = random.randint(0, 9)
print(random_number)

app = Flask(__name__)

@app.route("/")
def hello_world():
    return ("<h1>Guess a number between 0 and 9</p>"
            "<img src='https://media.giphy.com/media/3o7aCSPqXE5C6T8tBC/giphy.gif' />")


@app.route("/<int:guess>")
def check_answer(guess):
    if guess > random_number:
        return "<h1>too high!</h1>"
    elif guess < random_number:
        return "<h1>too low</h1>"
    else:
        return "<h1>Correct</h1>"


if __name__ == "__main__":
    app.run(debug=True)
