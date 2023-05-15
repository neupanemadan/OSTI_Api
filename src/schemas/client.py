
from marshmallow import fields
from src.extensions import ma


class ClientSchema(ma.Schema):
    id = fields.Integer()
    name = fields.String(required=True)
    filename = fields.String()
    filepath = fields.String()