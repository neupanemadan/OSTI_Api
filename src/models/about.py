from src.mixins.resource import ResourceMixin
from src.extensions import db
from flask import url_for
from sqlalchemy.sql import expression


class About(db.Model, ResourceMixin):
    __tablename__ = 'about'

    id = db.Column(db.Integer, primary_key=True, nullable=False)
    mission = db.Column(db.String(1000))
    vision = db.Column(db.String(1000))
    company_description = db.Column(db.String(1000))
    ceo_message = db.Column(db.String(1000))
    policy = db.Column(db.String(1000))
    filename = db.Column(db.String(255))


    @property
    def filepath(self):
        if self.filename:
            return url_for('AboutView:download',  filename=self.filename, _external=True)
