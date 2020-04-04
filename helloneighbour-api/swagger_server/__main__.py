#!/usr/bin/env python3

import connexion

from swagger_server import encoder
import swagger_server.storage as storage


def main():
    app = connexion.App(__name__, specification_dir='./swagger/')
    app.app.json_encoder = encoder.JSONEncoder
    app.add_api('swagger.yaml', arguments={'title': 'COVID-19 Global Church Hack &#39;Hello Neighbour&#39;'})
    flask_app = app.app
    flask_app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:////tmp/test.db'
    flask_app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
    storage.init(flask_app)
    app.run(port=8080)


if __name__ == '__main__':
    main()
