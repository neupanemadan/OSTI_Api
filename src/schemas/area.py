
from marshmallow import fields
from src.extensions import ma


class AreaSchema(ma.Schema):
    id = fields.Integer()
    name = fields.String(required=True)
    description = fields.String()
    filename = fields.String()
    filepath = fields.String()