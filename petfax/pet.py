from flask import ( Blueprint, render_template ) 
import json 

pets = json.load(open('pets.json'))

bp = Blueprint('pet', __name__, url_prefix="/pets")

@bp.route('/')
def index(): 
    return render_template('pets/index.html', pets=pets)

@bp.route('/<int:id>')
def show(id): 
    pet = pets[id - 1]
    pet_photo = pet.get('pet_photo')  # Safely retrieve the value of 'pet_photo' from the pet dictionary
    if pet_photo is not None:
        print("Pet Photo Filename:", pet_photo)
    else:
        print("Pet photo not found for this pet.")

    return render_template('pets/show.html', pet=pet)

