
from marshmallow import fields
from src.extensions import ma


class AboutSchema(ma.Schema):
    id = fields.Integer()
    ceo_message = fields.String(required=True)
    mission = fields.String()
    vision = fields.String()
    company_description = fields.String()
    filename = fields.String()
    policy = fields.String()
    filepath = fields.String()