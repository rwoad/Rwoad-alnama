# -*- coding: utf-8 -*-
{
    'name': 'Edit Invoice Direction',
    'category': 'Accounting/Accounting',
    "depends": ["account",'l10n_gcc_invoice', 'l10n_sa'],
    "data": [
        'views/report_invoice.xml',
    ],

    'installable': True,
    'auto_install': False,
    'application': False,
}
