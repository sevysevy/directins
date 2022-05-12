# -*- coding: utf-8 -*-
{
    'name': "invoice_line data",

    'summary': """
        Ce module permet d'ajouter la date effective et la date d'échéance  sur le formulaire de facturation""",

    'description': """
        Ce module permet d'ajouter la date effective et la date d'échéance  sur le formulaire de facturation
    """,

    'author': "Yves Christian Ngah",

    # Categories can be used to filter modules in modules listing
    # Check https://github.com/odoo/odoo/blob/master/odoo/addons/base/module/module_data.xml
    # for the full list
    'category': 'Facturation',
    'version': '0.1',

    # any module necessary for this one to work correctly
    'depends': ['base','account'],

    # always loaded
    'data': [
        #'security/ir.model.access.csv',
        'views/views.xml',
        #'views/templates.xml',
    ],
    'installable': True,
    'application': True,
    'auto_install': False,
}


