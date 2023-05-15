from src.mixins.resource import ResourceMixin
from src.extensions import db
from flask import url_for
from sqlalchemy.sql import expression


class Team(db.Model, ResourceMixin):
    __tablename__ = 'teams'

    id = db.Column(db.Integer, primary_key=True, nullable=False)
    name = db.Column(db.String(55), nullable=False)
    position = db.Column(db.String(150))
    email = db.Column(db.String(155))
    filename = db.Column(db.String(255))
    facebook = db.Column(db.String(200))
    is_deleted = db.Column('is_deleted', db.Boolean(),
                        server_default=expression.false())


    @property
    def filepath(self):
        if self.filename:
            return url_for('TeamsView:download',  filename=self.filename, _external=True)
