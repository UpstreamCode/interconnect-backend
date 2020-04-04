#!/usr/bin/env python3

import connexion

from swagger_server import encoder


def main():
    app = connexion.App(__name__, specification_dir='./swagger/')
    app.app.json_encoder = encoder.JSONEncoder
    app.add_api('swagger.yaml', arguments={'title': 'COVID-19 Global Church Hack &#39;Hello Neighbour&#39;'})
    app.run(port=8080)


if __name__ == '__main__':
    main()
