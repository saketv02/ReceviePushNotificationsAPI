#!/usr/bin/env python3
#Author:Saket Vishwasrao

import connexion
from controllers import default_controller

if __name__ == '__main__':
    app = connexion.App(__name__, specification_dir='./swagger/')
    app.add_api('swagger.yaml', arguments={'title': ''})
    app.run(port=8080)
