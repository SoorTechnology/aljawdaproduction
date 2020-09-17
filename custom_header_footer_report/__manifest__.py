{
    'name': 'Custom PDF Report Header/Footer',
    'description': 'Customize the Invoice/Quotation/Sale order PDF layouts',
    'author': 'Younis',
    'category': 'Custom',
    'depends': ['account'],
    'data': [
        'reports/invoice_templates.xml',
        'reports/quotation_template.xml',
    ],
    'installable': True,
}