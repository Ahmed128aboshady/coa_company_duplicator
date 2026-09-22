# -*- coding: utf-8 -*-
{
    'name': 'COA Duplicate Company Configuration PRO',
    'version': '19.0.1.0.0',
    'category': 'Administration',
    'summary': 'Duplicate Chart of Accounts, Taxes, Journals, and Warehouses across companies in a multi-company Odoo setup',
    'description': """
COA Duplicate Company Configuration PRO
========================================
Seamlessly duplicate essential accounting and inventory configurations
from one company to another in a multi-company Odoo environment.
Supports Chart of Accounts, Taxes, Journals, Warehouses and more.
Fully compatible with Odoo 19 shared accounts architecture.
    """,
    'author': 'Community of accountants (COA-Egypt)',
    'website': 'https://www.coa-egy.com',
    'support': 'info@coa-egy.com',
    'images': ['static/description/banner.png'],
    'depends': ['base', 'account', 'stock'],
    'data': [
        'security/ir.model.access.csv',
        'views/wizard_views.xml',
    ],
    'price': 49.00,
    'currency': 'USD',
    'license': 'OPL-1',
    'installable': True,
    'application': True,
    'auto_install': False,
}
