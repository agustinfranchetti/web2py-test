db.define_table('proyectos',
                Field('id_proyecto'),
                Field('legajo_propietario', 'reference students'),
                primarykey=['id_proyecto']
                )