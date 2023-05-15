
from marshmallow import fields
from src.extensions import ma


class NoticeSchema(ma.Schema):
    id = fields.Integer()
    name = fields.String(required=True)
    filename = fields.String()
    date = fields.DateTime(format='%Y-%m-%d')
    link = fields.String()
    filepath = fields.String()