# Copyright 2014-2018 Ivan Yelizariev <https://it-projects.info/team/yelizariev>
# Copyright 2017 Gabbasov Dinar <https://it-projects.info/team/GabbasovDinar>
# Copyright 2018 Kolushov Alexandr <https://it-projects.info/team/KolushovAlexandr>
# Copyright 2018 Ildar Nasyrov <https://it-projects.info/team/iledarn>
# License LGPL-3.0 or later (https://www.gnu.org/licenses/lgpl.html).
{
    "name": """Available quantity of products in POS""",
    "summary": """Adds available quantity at products in POS""",
    "category": "Point Of Sale",
    # "live_test_url": "http://apps.it-projects.info/shop/product/DEMO-URL?version={ODOO_BRANCH}",
    "images": [],
    "version": "12.0.1.0.0",
    "application": False,

    "author": "IT-Projects LLC, Ivan Yelizariev, " "Odoo Community Association (OCA)",
    "support": "pos@it-projects.info",
    "website": "https://github.com/OCA/pos",
    "license": "LGPL-3",
    # "price": 9.00,
    # "currency": "EUR",

    "depends": [
        'point_of_sale',
        'stock',
    ],
    "external_dependencies": {"python": [], "bin": []},
    'data': [
        'data/pos_product_qty_available_data.xml',
    ],
    'qweb': [
        'static/src/xml/pos_product_available_template.xml',
    ],

    "post_load": None,
    "pre_init_hook": None,
    "post_init_hook": None,
    "uninstall_hook": None,

    "auto_install": False,
    "installable": True,
}
