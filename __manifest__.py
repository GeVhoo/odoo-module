# -*- coding: utf-8 -*-
{
    'name': "Email Tracker",

    'summary': """Записывает в лог изменение электронной почты клиента""",

    'description': """
        Проверяет атрибут email_from модели crm.lead.
        Если электронный адрес изменился, то информация записывается в лог.
    """,

    'author': "Григорий Вахрушев",
    'website': "https://github.com/GeVhoo/odoo-module",

    'category': 'Uncategorized',
    'version': '0.2',
 
    'depends': ['crm'],

    'data': [],
}
