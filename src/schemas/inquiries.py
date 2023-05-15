
from marshmallow import fields
from src.extensions import ma


class InquiriesSchema(ma.Schema):
    id = fields.Integer()
    name = fields.String(required=True)
    email = fields.String()
    phone = fields.String()
    company = fields.String()
    subject = fields.String()
    message = fields.String()