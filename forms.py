from wtforms import Form
from wtforms import StringField

class FileForm(Form):
    filename = StringField('filename')


