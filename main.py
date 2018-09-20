from flask import Flask

app = Flask(__name__)
app.config['DEBUG'] = True

"""<!DOCTYPE html>

<html>
    <head>
        <style>
            form {
                background-color: #eee;
                padding: 20px;
                margin: 0 auto;
                width: 540px;
                font: 16px sans-serif;
                border-radius: 10px;
            }
            textarea {
                margin: 10px 0;
                width: 540px;
                height: 120px;
            }
        </style>
    </head>
    <body>
      <!-- create your form here -->
      <form action="?" method="POST">
      <label for="rotate_box">Rotate by:</label>
      <textarea name="text" type="text">
      <input name="rot" type="number" value="0">
      <button>Submit</button>
      
    </body>
</html>"""
@app.route("/")
def index():
    return "Hello World"
app.run()