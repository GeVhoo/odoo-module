# -*- coding: utf-8 -*-
{
    'name': "Email Tracker",

    'summary': """Записывает в лог изменение электронной почты клиента""",

    'description': """
        Проверяет атрибут email_from модели crm.lead.
        Если электронный адрес изменился, то информация записывается в лог.
    """,

    'author': "Григорий Вахрушев",
    'website': "https://github.com/GeVhoo",

    'category': 'Uncategorized',
    'version': '0.1',
 
    'depends': ['base'],

    'data': [
        # 'security/ir.model.access.csv',
        'views/views.xml',
        'views/templates.xml',
    ],
}
