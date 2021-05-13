# -*- coding: utf-8 -*-
{
    'name':
    "Demo",
    'summary':
    """
        Demo module""",
    'description':
    """
        Long description of module's purpose
    """,
    'author':
    "Andrey Torkin",
    'website':
    "http://www.yourcompany.com",

    # Categories can be used to filter modules in modules listing
    # Check https://github.com/odoo/odoo/blob/14.0/odoo/addons/base/data/ir_module_category_data.xml
    # for the full list
    'category':
    'Uncategorized',
    'version':
    '0.1',

    # any module necessary for this one to work correctly
    'depends': ['base', 'contacts', 'crm', 'mail'],

    # always loaded
    'data': [
        'security/ir.model.access.csv',
        'views/demo.xml',
        'views/lead.xml',
        'views/menu.xml',
    ],
    # only loaded in demonstration mode
    'demo': [
        'demo/demo.xml',
    ],
}