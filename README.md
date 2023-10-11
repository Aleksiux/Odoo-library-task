# Odoo Library Module

This Odoo module allows you to store information about various documents or books. It creates a new document model to store the title, description, and a link to a company using a Many2one field.

## Installation

1. Make sure you have Odoo 13 and Python 3.7 installed on your system.

2. Create a new directory for your module within the Odoo `extra_addons` directory, for example: `/path/to/odoo/extra_addons/library_management`.

3. Inside the `library_management` directory, create the following files and directories or just use auto demo creation 
folder structure by using command in the terminal:
```
"C:\Program Files (x86)\Odoo 13.0\python\python.exe" "C:\Program Files (x86)\Odoo 13.0\server\odoo-bin" scaffold (name of the folder) "..Library-management-37\Odoo-library\extra_addons"
```
<font color="red"><b>Extra addons location should be absolute path! </b></font>

```python
library_management/
├── init.py
├── manifest.py
├── models/
│ ├── init.py
│ └── models.py
├── views/
│ └── library_document_view.xml
├── security/
│ └── ir.model.access.csv

```

4. Define the Document Model: In `models.py` file, define the new model for storing documents:

```python
from odoo import models, fields

class LibraryDocument(models.Model):
    _name = 'library.document'
    _description = 'Library Document'

    title = fields.Char(string='Title', required=True)
    description = fields.Text(string='Description')
    company_id = fields.Many2one('res.company', string='Company')
```
1. Create Menu Action: In library_document_view.xml file, create a menu action for accessing the tree view of the data:
```
<odoo>
    <data>
        <record id="action_library_document_tree" model="ir.actions.act_window">
            <field name="name">Library Documents</field>
            <field name="res_model">library.document</field>
            <field name="view_mode">tree,form</field>
        </record>
        <menuitem id="menu_library_documents" name="Library Documents" parent="base.menu_sales"
                  action="action_library_document_tree" sequence="10"/>
    </data>
</odoo>
```
2. Define Access Rights: In the ir.model.access.csv file, define the access rights for your model:
```
id,name,model_id:id,group_id:id,perm_read,perm_write,perm_create,perm_unlink
access_library_document,Library Document,model_library_document,base.group_user,1,1,1,1
```
3. Update the Manifest File: __manifest__.py file in the root of your module directory with the necessary module information.

4. Install Module: via the Odoo web interface.
5. Accessing Your Module
Once the module is installed and upgraded, you can access your library documents via the "Library Documents" menu item under the Sales menu in Odoo.