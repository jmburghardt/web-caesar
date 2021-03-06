from flask import Flask, request
from caesar import *

app = Flask(__name__)
app.config['DEBUG'] = True

form = """<!DOCTYPE html>

<html>
    <head>
        <style>
            form {{
                background-color: #eee;
                padding: 20px;
                margin: 0 auto;
                width: 540px;
                font: 16px sans-serif;
                border-radius: 10px;
            }}
            textarea {{
                margin: 10px 0;
                width: 540px;
                height: 120px;
            }}
        </style>
    </head>
    <body>
        <form action="/rotate" method="post">
            <label for="rot">Rotate by:</label>
            <input id="rot" type="text" name="rot" value="0" /></br>
            <textarea name="text">{0}</textarea>
            <input type="submit" name="text" value="Submit Query" />
      <!-- create your form here -->
    </body>
</html>
"""

@app.route("/")
def index():
    return form.format("")

@app.route("/rotate", methods=['post'])
def encrypt():
    rot = request.form['rot']
    text = request.form['text']
    encryption = rotate_string(text, rot)

    return form.format(encryption)


app.run()