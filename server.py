from flask import Flask
from flask import render_template

import forms

app = Flask(__name__)
#app = Flask(__name__, template_folder="folder name") IN CASE TEMPLASTES FOLDER IS NOT NAME TEMPLATES
@app.route('/')
def index():
    fileform = forms.FileForm()
    title = 'Flask'
    return render_template('index.html',title = title, form = fileform)

if __name__ == '__main__':
    app.run(debug = True, port = 5000)
