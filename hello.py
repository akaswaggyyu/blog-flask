from flask import Flask, render_template

#Create a Flask Instance
app = Flask(__name__)

@app.route('/')
def index():
    first_name = 'Simon'
    stuff = 'This is bold text'
    favorite_pizza =["pepperoni", "cheese", "bacon", 41]
    return render_template("index.html", 
        name = first_name, 
        stuff = stuff,
        favorite_pizza=favorite_pizza)


@app.route('/user/<name>')
def user(name):
    return render_template("user.html", name=name)

# Create Custom Error Pages

# Invalid URL
@app.errorhandler(404)
def page_not_found(e):
    return render_template("404.html"), 404

# Interal Server Error
@app.errorhandler(500)
def page_not_found(e):
    return render_template("500.html"), 500
 