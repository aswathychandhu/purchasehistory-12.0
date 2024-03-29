{
    'name': 'Purchase_history',
    'version': '1.0',
    'category': 'Purchase',
    'sequence': 60,
    'summary': 'Product purchase history on purchase order line',
    'description': "It shows purchase history of product in purchase line",
    'author':'Aswathy Chandhu Viswanath',
    'depends': ['purchase'],
    'data': ['wizard/purchase_line_wiz.xml',
       'view/purchase_custom.xml'],
    'installable': True,
    'auto_install': False,
    'application': False,
}
