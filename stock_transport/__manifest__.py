{
    'name': "stock transport",
    'version': '1.0',
    'author': "nihp-odoo",
    'category': "Inventory",
    'depends': ['stock_picking_batch', 'fleet'],
    'data': [
        'security/ir.model.access.csv',
        'views/fleet_category.xml',
        'views/stock_picking.xml',
        'views/stock_picking_batch.xml',
    ],
    'application': True,
    'installable': True,
    'license': 'LGPL-3',
}
