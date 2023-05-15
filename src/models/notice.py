from src.mixins.resource import ResourceMixin
from src.extensions import db
from flask import url_for
from sqlalchemy.sql import expression


class Notice(db.Model, ResourceMixin):
    __tablename__ = 'notices'

    id = db.Column(db.Integer, primary_key=True, nullable=False)
    name = db.Column(db.String(55), nullable=False)
    filename = db.Column(db.String(255))
    link = db.Column(db.String(255))
    date = db.Column(db.DateTime)
    is_deleted = db.Column('is_deleted', db.Boolean(),
                        server_default=expression.false())

    @property
    def filepath(self):
        if self.filename:
            return url_for('NoticesView:download',  filename=self.filename, _external=True)
