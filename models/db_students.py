# -*- coding: utf-8 -*-
db.define_table('students',
                Field('name'),
                Field('legajo', 'integer'),
                primarykey=['legajo']
                )
