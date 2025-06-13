from flask_wtf import FlaskForm
from wtforms import StringField, RadioField, SubmitField
from wtforms.validators import ValidationError, DataRequired, Optional, InputRequired, Length
from flask import flash

URL_MISSING_ERROR_STRING = "Please fill in URL."
TITLE_MISSING_ERROR_STRING = "Please fill in title."

MISSING_FIELD_STRINGS = {"URL": URL_MISSING_ERROR_STRING, "title": TITLE_MISSING_ERROR_STRING}



class AddItemForm(FlaskForm):
    title = StringField('title', name="title-add", id="title-add", validators=[DataRequired(), Length(max=100)])
    url = StringField('url',name="url-add", id="url-add", validators=[DataRequired(), Length(max=100)])
    submit = SubmitField('add-link-button')


class DeleteItemsForm(FlaskForm):
    title = StringField('title',name="title-delete", id="title-delete", validators=[Length(max=100)])
    url = StringField('url', name="url-delete", id="url-delete", validators=[Length(max=100)])
    by_field = RadioField('delete-by-field', choices=[('title', 'title'), ('url', 'url'),
                                                       ('title-url', 'Title and URL')], validators=[InputRequired()])
    submit = SubmitField('delete-link-button')
    def validate_title(self, field):
        if self.by_field.data == "title" or self.by_field.data == "title-url":
            if not field.data or field.data.isspace():
                flash(TITLE_MISSING_ERROR_STRING)
                raise ValidationError(TITLE_MISSING_ERROR_STRING)
    def validate_url(self, field):
        if self.by_field.data == "url" or self.by_field.data == "title-url":
            if not field.data or field.data.isspace():
                flash(URL_MISSING_ERROR_STRING)
                raise ValidationError(URL_MISSING_ERROR_STRING)
    