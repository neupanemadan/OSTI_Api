
from marshmallow import fields
from src.extensions import ma


class TeamSchema(ma.Schema):
    id = fields.Integer()
    name = fields.String(required=True)
    position = fields.String()
    email = fields.String()
    facebook = fields.String()
    filename = fields.String()
    is_deleted = fields.Boolean()
    filepath = fields.String()