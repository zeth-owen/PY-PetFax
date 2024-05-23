from flask import Flask
from flask_migrate import Migrate 

def create_app():
    app = Flask(__name__)


    app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://postgres:Spikearoo89!@localhost:5433/petfax'
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False  

    from . import models 
    models.db.init_app(app) 
    migrate = Migrate(app, models.db)

    @app.route('/')
    def hello():
        return 'Hello, PetFax!'
    from . import pet
    app.register_blueprint(pet.bp)

    from . import fact
    app.register_blueprint(fact.bp)

    return app











