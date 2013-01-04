# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'UserCount'
        db.create_table('md_playerpointer_users_usercount', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('creation_date', self.gf('django.db.models.fields.DateTimeField')()),
            ('value', self.gf('django.db.models.fields.PositiveIntegerField')()),
        ))
        db.send_create_signal('md_playerpointer_users', ['UserCount'])


    def backwards(self, orm):
        # Deleting model 'UserCount'
        db.delete_table('md_playerpointer_users_usercount')


    models = {
        'md_playerpointer_users.usercount': {
            'Meta': {'object_name': 'UserCount'},
            'creation_date': ('django.db.models.fields.DateTimeField', [], {}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'value': ('django.db.models.fields.PositiveIntegerField', [], {})
        }
    }

    complete_apps = ['md_playerpointer_users']