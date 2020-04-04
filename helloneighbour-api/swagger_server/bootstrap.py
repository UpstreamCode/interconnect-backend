import connexion

from swagger_server import encoder, config

from flask_sqlalchemy import SQLAlchemy

app = connexion.App(__name__, specification_dir='./swagger/')
app.app.json_encoder = encoder.JSONEncoder
flask_app = app.app
flask_app.config['SQLALCHEMY_DATABASE_URI'] = config.STORAGE_BACKEND
flask_app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(flask_app)
db.create_all()

from swagger_server.storage.church import Church as StorageChurch
try:
    db.session.add(StorageChurch(id=1, name="Cross Point Church", email="cross_point@example.com"))
    db.session.commit()
except:
    pass
app.add_api('swagger.yaml', arguments={'title': 'COVID-19 Global Church Hack &#39;Hello Neighbour&#39;'})
