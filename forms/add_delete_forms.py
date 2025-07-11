from flask_wtf import FlaskForm
from wtforms import StringField, RadioField, SubmitField
from wtforms.validators import DataRequired, InputRequired, Length



class AddItemForm(FlaskForm):
    title = StringField('Title', name="title-add", id="title-add", validators=[Length(max=300)])
    url = StringField('URL',name="url-add", id="url-add", validators=[Length(max=500)])
    submit = SubmitField('add-link-button')

class DeleteItemsForm(FlaskForm):
    title = StringField('Title',name="title-delete", id="title-delete", validators=[Length(max=300)])
    url = StringField('URL', name="url-delete", id="url-delete", validators=[Length(max=500)])
    by_field = RadioField('delete-by-field', choices=[('title', 'Title'), ('url', 'URL'),
                                                       ('title-url', 'Title and URL')], validators=[InputRequired()])
    submit = SubmitField('delete-link-button')