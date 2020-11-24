# -*- coding: utf-8 -*-
db.define_table('students',
                Field('name'),
                Field('legajo', 'integer'),
                primarykey=['legajo']
               )


db.define_table('employee',
                Field('name'),
                Field('email'),
                Field('age', 'integer'),
                Field('id_boss','reference employee')
                )

db.define_table('proyectos',
                Field('id_proyecto'),
                Field('legajo_propietario', 'reference students')
                )