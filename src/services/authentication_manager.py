import datetime

from flask import current_app
from flask_jwt_extended import create_access_token, create_refresh_token
from werkzeug.exceptions import Unauthorized, Forbidden

from src.utils.flask_mailplus import send_template_message
from src.models.revoked_token import RevokedToken
from src.models.user import User
from src.schemas.user import UserSchema

user_schema = UserSchema()


class AuthenticationManager:
    """
    Handles all authentication related tasks
    """

    @classmethod
    def initialize_password_reset(cls, user):
        """
        Generate a token to reset the password for a specific user.

        :param user: User object
        :type user: User
        :return: User instance
        """
        reset_token = cls.serialize_token(user)

        ctx = {'user': user, 'reset_url': cls._get_reset_url(reset_token)}

        return send_template_message(subject='Password reset',
                                     recipients=[user.email],
                                     template='user/mail/password_reset', ctx=ctx)

    @classmethod
    def find_by_identity(cls, identity):
        """
        Find a user by their e-mail or username.

        :param identity: Email or username
        :type identity: str
        :return: User instance
        """
        return User.query.filter(
            (User.email == identity) | (User.username == identity)).first()

    def login(self, data):
        user = User.find_by_identity(data['username'])

        if not user or not user.authenticated(password=data['password']):
            raise Unauthorized()

        if not user.is_active:
            raise Forbidden()

        access_token_expire_in = self._get_access_token_expires_in()
        access_token = create_access_token(
            identity=user,
            expires_delta=access_token_expire_in
        )

        refresh_token = create_refresh_token(
            identity=user,
            expires_delta=self._get_refresh_token_expires_in()
        )

        return {
            'expires_in': access_token_expire_in.total_seconds(),
            'access_token': access_token,
            'refresh_token': refresh_token
        }

    def refresh_token(self, identity):
        user = User.find_by_identity(identity)

        if not user.is_active:
            return {'message': 'User is disabled, please contact admin'}, 401

        access_token_expire_in = self._get_access_token_expires_in()
        access_token = create_access_token(
            identity=user,
            expires_delta=access_token_expire_in
        )
        refresh_token = create_refresh_token(
            identity=user,
            expires_delta=self._get_refresh_token_expires_in()
        )

        return {
            'access_token': access_token,
            'refresh_token': refresh_token,
            'expires_in': access_token_expire_in.total_seconds()
        }

    @staticmethod
    def reset_password(user, password):
        """
        reset password of given user
        :param user: User object
        :type user: User
        :return: boolean
        """
        user.password = User.encrypt_password(password)
        user.save()

    @staticmethod
    def revoke_token(jti):
        revoked_token = RevokedToken(jti=jti)
        revoked_token.save()

        return revoked_token

    @staticmethod
    def _get_access_token_expires_in():
        return datetime.timedelta(minutes=current_app.config['ACCESS_TOKEN_EXPIRES_IN'])

    @staticmethod
    def _get_refresh_token_expires_in():
        return datetime.timedelta(minutes=current_app.config['REFRESH_TOKEN_EXPIRES_IN'])

    @staticmethod
    def _get_reset_url(token):
        """"""
        return f"{current_app.config['CLIENT_APP_URL']}/reset_password/{token}"
