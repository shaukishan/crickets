# -*- coding: utf-8 -*-
# Part of Odoo. See LICENSE file for full copyright and licensing details.
{
    'name': 'Cricket Team Management',
    'version': '1.1',
    'summary': 'Manage Cricket Team for India',
    'sequence': 30,
    'description': """
    Manage Cricket Team for India
    """,
    'category': 'Cricket',
    'website': 'https://www.apagen.com',
    'depends': ['base'],
    'data': [
        'team_view.xml'
    ],
    'installable': True,
    'application': True,
    'auto_install': False,
}
