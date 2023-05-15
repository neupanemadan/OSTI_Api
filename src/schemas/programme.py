
from marshmallow import fields
from src.extensions import ma


class ProgrammeSchema(ma.Schema):
    id = fields.Integer()
    name = fields.String(required=True)
    description = fields.String(required=True)
    filename = fields.String()
    date = fields.DateTime(format='%Y-%m-%d')
    is_deleted = fields.Boolean()
    is_featured = fields.Boolean()
    filepath = fields.String()