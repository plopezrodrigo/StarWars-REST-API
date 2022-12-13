from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(120), unique=True, nullable=False)
    password = db.Column(db.String(80), unique=False, nullable=False)
    is_active = db.Column(db.Boolean(), unique=False, nullable=False)


    def __repr__(self):
        return '<User %>' % self.username

    def serialize(self):
        return {
            "id": self.id,
            "email": self.email,
            # do not serialize the password, its a security breach
        }

class Character(db.Model):
    __tablename__ = 'character'
    # Here we define columns for the table address.
    # Notice that each column is also a normal Python instance attribute.
    id = db.Column(db.Integer, primary_key=True)
    character_name = db.Column(db.String(250), unique=False, nullable=False)
    description = db.Column(db.String(500), unique=False, nullable=False)
    birthday_year = db.Column(db.Integer, unique=False, nullable=False)
    gender = db.Column(db.String(250), unique=False, nullable=False)
    height = db.Column(db.Integer, unique=False, nullable=False)
    skin_color = db.Column(db.String(250), unique=False, nullable=False)
    eye_color = db.Column(db.String(250), unique=False, nullable=False)

    def __repr__(self):
        return '<Character %>' % self.character_name

    def serialize(self):
        return {
            "id": self.id,
            "character_name": self.character_name,
            "description": self.description,
            "birthday_year": self.birthday_year,
            "gender": self.gender,
            "height": self.height,
            "skin_color": self.skin_color,
            "eye_color": self.eye_color,
            # do not serialize the password, its a security breach
        }

class Planet(db.Model):
    __tablename__ = 'planet'
    # Here we define columns for the table address.
    # Notice that each column is also a normal Python instance attribute.
    id = db.Column(db.Integer, primary_key=True, unique=True, nullable=False)
    planet_name = db.Column(db.String(250), unique=True, nullable=False)
    description = db.Column(db.String(500), unique=True, nullable=False)
    population = db.Column(db.Integer, unique=True, nullable=False)
    climate = db.Column(db.String(250), unique=True, nullable=False)
    orbital_period = db.Column(db.Integer, unique=True, nullable=False)
    rotation_period = db.Column(db.Integer, unique=True, nullable=False)
    diameter = db.Column(db.Integer, unique=True, nullable=False)
    created_date = db.Column(db.String(250), unique=True, nullable=False)
    update_date = db.Column(db.String(250), unique=True, nullable=False)
    url = db.Column(db.String(250), unique=True, nullable=False)

    def __repr__(self):
        return '<Planet %>' % self.planet_name

    def serialize(self):
        return {
            "id": self.id,
            "planet_name": self.planet_name,
            "description": self.description,
            "population": self.population,
            "climate": self.climate,
            "orbital_period": self.orbital_period,
            "rotation_period": self.rotation_period,
            "diameter": self.diameter,
            "created_date": self.created_date,
            "update_date": self.update_date,
            "url": self.url,
            # do not serialize the password, its a security breach
        }

class CharactersFavourites(db.Model):
    __tablename__ = 'CharactersFavourites'
    # Here we define columns for the table address.
    # Notice that each column is also a normal Python instance attribute.
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id') , unique=True, nullable=False)
    characters_id = db.Column(db.Integer, db.ForeignKey('character.id') , unique=True, nullable=False)
    characters_fav = db.relationship('Character', backref = 'Charactersfavourites')

    def __repr__(self):
        return '<CharactersFavourites %>' % self.id

    def serialize(self):
        return {
            "id": self.id,
            "user_id": self.user_id,
            "characters_id": self.characters_id,
            "characters_fav": self.characters_fav,
            # do not serialize the password, its a security breach
        }

class PlanetsFavourites(db.Model):
    __tablename__ = 'PlanetsFavourites'
    # Here we define columns for the table address.
    # Notice that each column is also a normal Python instance attribute.
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id') , unique=True, nullable=False)
    planets_id = db.Column(db.Integer, db.ForeignKey('planet.id') , unique=True, nullable=False)
    planets_fav = db.relationship('Planet', backref = 'PlanetsFavorites')

    def __repr__(self):
        return '<PlanetsFavourites %>' % self.id

    def serialize(self):
        return {
            "id": self.id,
            "user_id": self.user_id,
            "planets_id": self.planets_id,
            "planets_fav": self.planets_fav,
            # do not serialize the password, its a security breach
        }