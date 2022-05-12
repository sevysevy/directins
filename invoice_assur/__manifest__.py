# -*- coding: utf-8 -*-
{
    'name': "invoice_assur",

    'summary': 
    """
        Ce module prend en compte la gestion des clients pour Direct Inssurance
    """,

    'description': 
    """
        Ce module prend en compte la gestion des clients pour Direct Inssurance
    """,

    'author': "Yves C",

    # Categories can be used to filter modules in modules listing
    # Check https://github.com/odoo/odoo/blob/master/odoo/addons/base/module/module_data.xml
    # for the full list
    'category': 'Crm',
    'version': '0.1',

    # any module necessary for this one to work correctly
    'depends': ['base','crm','invoice_line_data'],

    # always loaded
    'data': [
        #'security/ir.model.access.csv',
        'views/invoice_assur.xml'
        #'views/templates.xml',
    ],
    # only loaded in demonstration mode
    #'demo': [
     #   'demo/demo.xml',
   # ],
    'installable': True,
    'application': True,
    'auto_install': False,
}


