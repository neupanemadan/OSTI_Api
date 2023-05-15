from src.mixins.resource import ResourceMixin
from src.extensions import db
from flask import url_for
from sqlalchemy.sql import expression


class Gallery(db.Model, ResourceMixin):
    __tablename__ = 'galleries'

    id = db.Column(db.Integer, primary_key=True, nullable=False)
    album = db.Column(db.String(55), nullable=False)
    filename = db.Column(db.String(255))
    is_deleted = db.Column('is_deleted', db.Boolean(),
                        server_default=expression.false())

    @property
    def filepath(self):
        if self.filename:
            return url_for('GalleriesView:download',  filename=self.filename, _external=True)
        

