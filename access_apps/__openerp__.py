{
    'name': 'Control access to Apps',
    'version': '1.0.1',
    'author': 'IT-Projects LLC, Ivan Yelizariev',
    'category': 'Access',
    'website': 'https://twitter.com/yelizariev',
    'price': 10.00,
    'currency': 'EUR',
    'depends': [
        'web_settings_dashboard',
        'access_restricted'
    ],
    'data': [
        'views/access_apps.xml',
        'security/access_apps_security.xml',
        'security/ir.model.access.csv',
    ],
    'installable': True
}
