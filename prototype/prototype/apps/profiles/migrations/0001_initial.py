# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'ProfileType'
        db.create_table(u'profiles_profiletype', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('URI', self.gf('django.db.models.fields.CharField')(max_length=75)),
            ('display_name', self.gf('django.db.models.fields.CharField')(max_length=200)),
            ('introduction', self.gf('django.db.models.fields.TextField')(blank=True)),
            ('description', self.gf('django.db.models.fields.TextField')(blank=True)),
            ('profile_type', self.gf('django.db.models.fields.IntegerField')()),
        ))
        db.send_create_signal(u'profiles', ['ProfileType'])


    def backwards(self, orm):
        # Deleting model 'ProfileType'
        db.delete_table(u'profiles_profiletype')


    models = {
        u'profiles.profiletype': {
            'Meta': {'object_name': 'ProfileType'},
            'URI': ('django.db.models.fields.CharField', [], {'max_length': '75'}),
            'description': ('django.db.models.fields.TextField', [], {'blank': 'True'}),
            'display_name': ('django.db.models.fields.CharField', [], {'max_length': '200'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'introduction': ('django.db.models.fields.TextField', [], {'blank': 'True'}),
            'profile_type': ('django.db.models.fields.IntegerField', [], {})
        }
    }

    complete_apps = ['profiles']