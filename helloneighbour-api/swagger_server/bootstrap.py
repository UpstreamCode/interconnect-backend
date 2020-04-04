import connexion

from swagger_server import encoder

from flask_sqlalchemy import SQLAlchemy

app = connexion.App(__name__, specification_dir='./swagger/')
app.app.json_encoder = encoder.JSONEncoder
app.add_api('swagger.yaml', arguments={'title': 'COVID-19 Global Church Hack &#39;Hello Neighbour&#39;'})
flask_app = app.app
flask_app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:////tmp/test.db'
flask_app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(flask_app)
db.create_all()
