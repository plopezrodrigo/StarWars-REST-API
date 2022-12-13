"""
This module takes care of starting the API Server, Loading the DB and Adding the endpoints
"""
import os
from flask import Flask, request, jsonify, url_for
from flask_migrate import Migrate
from flask_swagger import swagger
from flask_cors import CORS
from utils import APIException, generate_sitemap
from admin import setup_admin
from models import db, User, Character, Planet
#from models import Person

app = Flask(__name__)
app.url_map.strict_slashes = False

db_url = os.getenv("DATABASE_URL")
if db_url is not None:
    app.config['SQLALCHEMY_DATABASE_URI'] = db_url.replace("postgres://", "postgresql://")
else:
    app.config['SQLALCHEMY_DATABASE_URI'] = "sqlite:////tmp/test.db"
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

MIGRATE = Migrate(app, db)
db.init_app(app)
CORS(app)
setup_admin(app)

# Handle/serialize errors like a JSON object
@app.errorhandler(APIException)
def handle_invalid_usage(error):
    return jsonify(error.to_dict()), error.status_code

# generate sitemap with all your endpoints
@app.route('/')
def sitemap():
    return generate_sitemap(app)

@app.route('/people', methods=['GET'])
def get_people():
    people = Character.query.all()
    all_people = list(map(lambda x: x.serialize(), people))
    return ({"results":all_people}), 200

@app.route('/people/<int:people_id>', methods=['GET'])
def get_peopleID():
    characters_id = Character.query.get(id)
    return jsonify(Character.serialize()), 200

@app.route('/planet', methods=['GET'])
def get_planet():
    planets = Planet.query.all()
    data = [Planet.serialize() for Planet in planets]
    return jsonify(data), 200

@app.route('/planet/<int:planet_id>', methods=['GET'])
def get_planetID():
    planets_id = Planet.query.get(id)
    return jsonify(Planet.serialize()), 200

@app.route('/user', methods=['GET'])
def get_users():
    users = User.query.all()
    data = [User.serialize() for User in users]
    return jsonify(data), 200

@app.route('/favorite/planet/<int:planet_id>', methods=['POST'])
def add_new_favorite_planet():
    request_body_planet = request.get_json()
    favoritesPlanet = FavoritePlanet(id=request_body_planet)
    db.session.add(favoritesPlanet)
    db.session.commit()
    return jsonify(request_body_planet),200

@app.route('/favorite/people/<int:people_id>', methods=['POST'])
def add_new_favorite_people():
    request_body_people = request.get_json()
    favoritesPeople = FavoritePeople(id=request_body_people)
    db.session.add(favoritesPeople)
    db.session.commit()
    return jsonify(request_body_people),200

@app.route('/favorite/planet/<int:planet_id>', methods=['DELETE'])
def delete_favorite_planet(position):
    favorite_planet.remove(favorite_planet[position])
    print("This is the position to delete: ",position)
    return jsonify(favorite_planet)

@app.route('/favorite/people/<int:people_id>', methods=['DELETE'])
def delete_favorite_people(position):
    
    favoritePeople1 = favoritePeople.query.get(favoritePeople_id)
    if favoritePeople1 is None:
            raise APIException("Favorite People not found", status_code=404)
    db.session.delete(favoritePeople1)
    db.session.commit()

# this only runs if `$ python src/app.py` is executed
if __name__ == '__main__':
    PORT = int(os.environ.get('PORT', 3000))
    app.run(host='0.0.0.0', port=PORT, debug=False)
