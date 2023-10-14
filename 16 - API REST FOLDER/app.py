from flask import Flask
from aula16.models.models import db
from aula16.controllers.estudante import estudante_controller

def create_app():
    app = Flask(__name__, template_folder='templates')
    app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///estudantes.sqlite3'
    app.register_blueprint(estudante_controller, url_prefix="/estudante/")
    
    db.init_app(app)
    
    with app.app_context():
        db.create_all()

    return app

if __name__ == '__main__':
    app = create_app()
    app.run(debug=True)
