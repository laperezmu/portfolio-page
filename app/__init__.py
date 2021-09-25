#Import standard modules
import os

#Import third party modules
from flask import Flask

#Internal modules


def create_app():
    app = Flask(__name__)

    app.config.from_mapping(
        SENDGRID_KEY = os.environ.get('SENDGRID_KEY')
    )

    from . import portfolio
    app.register_blueprint(portfolio.bp)

    return app