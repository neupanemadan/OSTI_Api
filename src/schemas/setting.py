
from marshmallow import fields
from src.extensions import ma


class SettingSchema(ma.Schema):
    id = fields.Integer()
    name = fields.String(required=True)
    first_address = fields.String(required=True)
    first_phone = fields.String(required=True)
    first_email = fields.String(required=True)
    second_address = fields.String()
    second_phone = fields.String()
    second_email = fields.String()
    facebook = fields.String()
    instagram = fields.String()
    filename = fields.String()
    filepath = fields.String()