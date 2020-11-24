# -*- coding: utf-8 -*-

db.define_table('employee',
                Field('name'),
                Field('email'),
                Field('age', 'integer'),
                )