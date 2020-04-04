#!/usr/bin/env python3

from swagger_server.bootstrap import app, db
from swagger_server.storage import *


def main():
    db.create_all()
    app.run(port=8080)


if __name__ == '__main__':
    main()
