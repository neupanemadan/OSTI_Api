from src.mixins.resource import ResourceMixin
from src.extensions import db
from flask import url_for
from sqlalchemy.sql import expression


class Inquiry(db.Model, ResourceMixin):
    __tablename__ = 'inquiries'

    id = db.Column(db.Integer, primary_key=True, nullable=False)
    name = db.Column(db.String(55), nullable=False)
    email = db.Column(db.String(255))
    phone = db.Column(db.String(255))
    company = db.Column(db.String(255))
    subject = db.Column(db.String(255))
    message = db.Column(db.String(755), nullable=False)
    is_deleted = db.Column('is_deleted', db.Boolean(),
                        server_default=expression.false())

