import click
from flask.cli import with_appcontext
from src.services.user import UserService
from src.models.user import User


@click.group()
@with_appcontext
def user():
    """
    import ipalet users.
    """
    pass


@click.command()
@with_appcontext
def import_user():
    users = [
        {
            'username': '667',
            'email': 'admin@admin.com',
            'password': '667',
            'role': User.ROLE_USER,
            'is_active': True,
            'profile': {
                'name': 'admin',
                'name_kana': 'admin'
            }
        },
        {
            'username': '668',
            'email': 'madan@madan.com',
            'password': '668',
            'role': User.ROLE_ADMIN,
            'is_active': True,
            'profile': {
                'name': 'madan',
                'name_kana': 'madan'
            }
        }
    ]

    for user in users:
        UserService.create(user)


user.add_command(import_user)
