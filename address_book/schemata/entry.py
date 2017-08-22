"""Module that handles methods for the entry schema"""

from marshmallow import fields, Schema

class EntrySchema(Schema):
    """Schema for address entries"""
    first_name = fields.String(required=True)
    last_name = fields.String(required=True)
    home_number = fields.String(required=True)
    mobile_number = fields.String(required=True)
    work_number = fields.String(required=True)
    address = fields.String(required=False)
    city = fields.String(required=False)
    state = fields.String(required=False)
    zipcode = fields.String(required=True)
