from src.mixins.resource import ResourceMixin
from src.extensions import db
from flask import url_for
from sqlalchemy.sql import expression


class Setting(db.Model, ResourceMixin):
    __tablename__ = 'setting'

    id = db.Column(db.Integer, primary_key=True, nullable=False)
    name = db.Column(db.String(55), nullable=False)
    first_address = db.Column(db.String(255), nullable=False)
    second_address = db.Column(db.String(255))
    first_phone = db.Column(db.String(255), nullable=False)
    second_phone = db.Column(db.String(255))
    first_email = db.Column(db.String(255), nullable=False)
    second_email = db.Column(db.String(255))
    facebook = db.Column(db.String(255))
    instagram = db.Column(db.String(255))
    filename = db.Column(db.String(255))


    @property
    def filepath(self):
        if self.filename:
            return url_for('SettingView:download',  filename=self.filename, _external=True)
