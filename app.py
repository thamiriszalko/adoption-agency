from flask import Flask, render_template, redirect, request, flash

from forms import PetForm
from models import connect_db, Pet, db
from flask_debugtoolbar import DebugToolbarExtension

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://localhost:5433/adopt_db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['SQLALCHEMY_ECHO'] = True
app.config['SECRET_KEY'] = "123-456"
app.config['DEBUG_TB_INTERCEPT_REDIRECTS'] = False
debug = DebugToolbarExtension(app)

connect_db(app)
db.create_all()


@app.route('/')
def home_page():
    """"List pets for adoption"""
    pets = Pet.query.all()

    return render_template("home_page.html", pets=pets)


@app.route('/pets/<int:pet_id>', methods=["POST", "GET"])
def pet_detail_edit(pet_id):
    """"You can see and update some details about the pet if you want"""
    pet = Pet.query.get_or_404(pet_id)
    form = PetForm(obj=pet)

    if form.validate_on_submit():
        pet.img_url = form.img_url.data if form.img_url.data else pet.img_url
        pet.notes = form.notes.data if form.notes.data else pet.notes
        pet.available = form.available.data if form.available.data else pet.available

        db.session.add(pet)
        db.session.commit()

        return redirect('/')
    else:
        return render_template("detail_edit_pet.html", pet=pet, form=form)


@app.route('/pets/new', methods=["POST", "GET"])
def pet_add():
    """"Add a pet"""
    form = PetForm()
    if form.validate_on_submit():
        name = form.name.data
        species = form.species.data
        age = form.age.data if form.age.data else None
        img_url = form.img_url.data if form.img_url.data else None
        notes = form.notes.data if form.notes.data else None
        available = form.available.data if form.available.data else None

        pet = Pet(
            name=name,
            species=species,
            age=age,
            img_url=img_url,
            notes=notes,
            available=available,
        )

        db.session.add(pet)
        db.session.commit()

        return redirect('/')
    else:
        return render_template("add_pet.html", form=form)
