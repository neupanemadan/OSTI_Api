from src.mixins.resource import ResourceMixin
from src.extensions import db
from flask import url_for
from sqlalchemy.sql import expression


class Slider(db.Model, ResourceMixin):
    __tablename__ = 'sliders'

    id = db.Column(db.Integer, primary_key=True, nullable=False)
    name = db.Column(db.String(55), nullable=False)
    description = db.Column(db.String(755), nullable=False)
    filename = db.Column(db.String(255))
    is_deleted = db.Column('is_deleted', db.Boolean(),
                        server_default=expression.false())

    @property
    def filepath(self):
        if self.filename:
            return url_for('SlidersView:download',  filename=self.filename, _external=True)
