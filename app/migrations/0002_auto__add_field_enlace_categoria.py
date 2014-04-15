# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding field 'Enlace.categoria'
        db.add_column(u'app_enlace', 'categoria',
                      self.gf('django.db.models.fields.related.ForeignKey')(default=2, to=orm['app.Categoria']),
                      keep_default=False)


    def backwards(self, orm):
        # Deleting field 'Enlace.categoria'
        db.delete_column(u'app_enlace', 'categoria_id')


    models = {
        u'app.categoria': {
            'Meta': {'object_name': 'Categoria'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'titulo': ('django.db.models.fields.CharField', [], {'max_length': '256'})
        },
        u'app.enlace': {
            'Meta': {'object_name': 'Enlace'},
            'categoria': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['app.Categoria']"}),
            'enlace': ('django.db.models.fields.URLField', [], {'max_length': '200'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'titulo': ('django.db.models.fields.CharField', [], {'max_length': '140'}),
            'votos': ('django.db.models.fields.IntegerField', [], {'default': '0'})
        }
    }

    complete_apps = ['app']