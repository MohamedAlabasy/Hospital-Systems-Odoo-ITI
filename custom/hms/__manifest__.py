{
    'name': 'HMS Model',
    'description': '''
    for handles hms patient
    ''',
    'version': '1.0',
    'category': 'Accounting/Accounting',
    'depends': ['crm'],
    'data': [
        'views/hms_patients_views.xml',
        'views/hms_departments_views.xml',
        'views/hms_doctors_views.xml',
        'views/hms_tags_views.xml',
        'views/hms_log_history_views.xml',
        'views/crm_customers_view.xml',
    ],
    'license': 'LGPL-3',
}
