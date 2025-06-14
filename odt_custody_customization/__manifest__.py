# -*- coding: utf-8 -*-
{
    'name': "Employee Custody Customization",

    'author': "OdooTec",
    'website': "http://www.odootec.com",

    # Categories can be used to filter modules in modules listing
    # Check https://github.com/odoo/odoo/blob/master/odoo/addons/base/module/module_data.xml
    # for the full list
    'category': 'HR',
    'version': '0.1',

    # any module necessary for this one to work correctly
    'depends': ['odt_custody',],

    # always loaded
    'data': [
        'security/hr_custody_security.xml',
        # 'views/hr_clearance_view.xml',
        'views/employee_custody_view.xml',
    ],
}
