# Copyright 2017 Oihane Crucelaegui - AvanzOSC
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl).

{
    'name': 'Contract Specification',
    'version': '11.0.1.1.0',
    'category': 'Hidden',
    'author': 'AvanzOSC',
    'license': 'AGPL-3',
    'summary': 'Define conditions and specifications',
    'depends': [
        'base',
        'mail',
    ],
    'data': [
        'security/ir.model.access.csv',
        'views/contract_condition_views.xml',
        'views/contract_condition_template_views.xml',
        'views/contract_section_views.xml',
        'views/number_translation_views.xml',
    ],
    'demo': [
        'demo/contract_condition_demo.xml',
    ],
    'installable': True,
}
