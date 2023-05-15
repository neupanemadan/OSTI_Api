from flask import Flask
from flask_cors import CORS
from werkzeug.debug import DebuggedApplication

from cli import register_cli_commands
from src.models.user import User
from src.models.revoked_token import RevokedToken
from src.exceptions.api_exception_handler import ApiExceptionHandler
from src import routes
from src.extensions import (
    db,
    migrate,
    ma,
    mail,
    jwt,
    apispec
)
# from flask_sqlalchemy import get_debug_queries


def create_app(settings_override=None):
    """
    Create a Flask application using the app factory pattern.

    :param settings_override: Override settings
    :return: Flask app
    """
    app = Flask(__name__, static_folder='../public', static_url_path='')

    app.config.from_object('config.settings')

    if settings_override:
        app.config.update(settings_override)

    # initialize cors
    CORS(app,
         supports_credentials=True,
         allow_headers="*",
         resources={
             r"/*": {
                 "origins": "*"
             }
         })
    app.config['CORS_HEADERS'] = 'Content-Type'

    extensions(app)
    routes.register(app)
    ApiExceptionHandler(app)

    if app.debug:
        app.wsgi_app = DebuggedApplication(app.wsgi_app, evalex=True)

    register_cli_commands(app)
    jwt_callbacks(app, User)

    # @app.after_request
    # def record_queries(response):
    #     for info in get_debug_queries():
    #         print(info)

    #     return response

    return app


def extensions(app):
    """
    Register 0 or more extensions (mutates the app passed in).

    :param app: Flask application instance
    :return: None
    """
    db.init_app(app)
    ma.init_app(app)
    migrate.init_app(app=app, db=db)
    mail.init_app(app)
    jwt.init_app(app)
    apispec.init_app(app, info=dict(description="A minimal flask API"),)


    return None


def jwt_callbacks(app, user_model):
    @jwt.user_identity_loader
    def user_identity_lookup(user):
        return user.email

    @jwt.additional_claims_loader
    def add_claims_to_access_token(user):
        return {'role': user.role}

    @jwt.token_in_blocklist_loader
    def check_if_token_in_blacklist(jwt_header, jwt_payload):
        jti = jwt_payload['jti']
        return RevokedToken.is_jti_blacklisted(jti)

    @jwt.user_lookup_loader
    def user_loader_callback(jwt_header, jwt_data):
        identity = jwt_data['sub']
        return user_model.find_by_identity(identity)
