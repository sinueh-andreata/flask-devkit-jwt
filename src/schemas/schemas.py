from marshmallow import Schema, fields, validate

class ProductSchema(Schema):
    class Meta:
        unknown = 'EXCLUDE'
        
    id = fields.Int(dump_only=True)
    nome = fields.Str(required=True, validate=validate.Length(min=3, max=100))
    preco = fields.Float(required=True, validate=validate.Range(min=0))
    estoque = fields.Int(required=True, validate=validate.Range(min=0))
