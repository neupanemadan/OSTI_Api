
from marshmallow import fields
from src.extensions import ma


class GallerySchema(ma.Schema):
    id = fields.Integer()
    album = fields.String(required=True)
    filename = fields.String()
    filepath = fields.String()
