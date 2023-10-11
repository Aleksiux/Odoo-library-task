from odoo import models, fields


class LibraryDocument(models.Model):
    """
    Library item title and description
    """
    _name = 'library.document'
    _description = 'Library Document'
    title = fields.Char(string='Title', required=True)
    description = fields.Text(string='Description')
    company_id = fields.Many2one('res.company', string='Company')

