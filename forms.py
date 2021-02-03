from flask_wtf import FlaskForm
from wtforms import StringField, BooleanField, SelectField
from wtforms.validators import InputRequired, Optional, URL


class PetForm(FlaskForm):
    name = StringField(
        "Name",
        validators=[InputRequired(message="Name cannot be blank")]
    )
    species = SelectField(
        'Species',
        choices=[
            ('cat', 'Cat'),
            ('dog', 'Dog'),
            ('por', 'Porcupine')
        ]
    )
    img_url = StringField(
        "Picture",
        validators=[Optional(), URL()]
    )
    age = StringField(
        "Age",
        validators=[Optional()]
    )
    notes = StringField(
        "Notes",
        validators=[Optional()]
    )
    available = BooleanField(
        "Available",
        validators=[Optional()]
    )



