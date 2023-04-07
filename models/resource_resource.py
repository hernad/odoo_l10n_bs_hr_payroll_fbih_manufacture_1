from odoo import fields, models

class ResourceFB(models.Model):
    _inherit = 'resource.resource'
    _description = "Resource fbih_manufacture_1"

    _sql_constraints = [
        ('name_unique', 'unique(company_id,resource_type,name)', 'Ime resursa u preduzeću mora biti jedinstveno.')
    ]