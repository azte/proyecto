# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'Categoria'
        db.create_table(u'app_categoria', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('titulo', self.gf('django.db.models.fields.CharField')(max_length=256)),
        ))
        db.send_create_signal(u'app', ['Categoria'])

        # Adding model 'Enlace'
        db.create_table(u'app_enlace', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('titulo', self.gf('django.db.models.fields.CharField')(max_length=140)),
            ('enlace', self.gf('django.db.models.fields.URLField')(max_length=200)),
            ('votos', self.gf('django.db.models.fields.IntegerField')(default=0)),
        ))
        db.send_create_signal(u'app', ['Enlace'])


    def backwards(self, orm):
        # Deleting model 'Categoria'
        db.delete_table(u'app_categoria')

        # Deleting model 'Enlace'
        db.delete_table(u'app_enlace')


    models = {
        u'app.categoria': {
            'Meta': {'object_name': 'Categoria'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'titulo': ('django.db.models.fields.CharField', [], {'max_length': '256'})
        },
        u'app.enlace': {
            'Meta': {'object_name': 'Enlace'},
            'enlace': ('django.db.models.fields.URLField', [], {'max_length': '200'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'titulo': ('django.db.models.fields.CharField', [], {'max_length': '140'}),
            'votos': ('django.db.models.fields.IntegerField', [], {'default': '0'})
        }
    }

    complete_apps = ['app']