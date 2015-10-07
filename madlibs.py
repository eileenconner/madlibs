from random import sample

from flask import Flask, render_template, request


# "__name__" is a special Python variable for the name of the current module
# Flask wants to know this to know what any imported things are relative to.
app = Flask(__name__)

# route to handle the landing page of a website.
@app.route('/')
def start_here():
    return "Hi! This is the home page."

# route to display a simple web page
@app.route('/hello')
def say_hello():
    return render_template("hello.html")

@app.route('/greet')
def greet_person():
    player = request.args.get("person")

    AWESOMENESS = [
        'awesome', 'terrific', 'fantastic', 'neato', 'fantabulous', 'wowza', 'oh-so-not-meh',
        'brilliant', 'ducky', 'coolio', 'incredible', 'wonderful', 'smashing', 'lovely']

    compliments = sample(AWESOMENESS, 3)

    return render_template("compliment.html", person=player, compliments=compliments)

@app.route("/game")
def show_game_form():
    response = request.args.get("choice")

    if response == "no":
        return render_template("goodbye.html")
    elif response == "yes":
        return render_template("game.html")

@app.route("/madlib")
def show_madlib():
    person = request.args.get("person")
    color = request.args.get("color")
    noun = request.args.get("noun")
    adjective = request.args.get("adjective") 
    ghost_story = request.args.get("ghost")
    animal_choices = request.args.getlist("animal")

    if ghost_story == "yes":
        return render_template("madlib2.html", person=person, color=color, noun=noun, adjective=adjective)
    else:
        return render_template("madlib.html", person=person, color=color, noun=noun, adjective=adjective, animal_choices=animal_choices)


if __name__ == '__main__':
    # debug=True gives us error messages in the browser and also "reloads" our web app
    # if we change the code.
    app.run(debug=True)
