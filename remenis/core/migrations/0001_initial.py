# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'User'
        db.create_table('core_user', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('fbid', self.gf('django.db.models.fields.CharField')(max_length=20)),
            ('first_name', self.gf('django.db.models.fields.CharField')(max_length=30)),
            ('last_name', self.gf('django.db.models.fields.CharField')(max_length=40)),
            ('full_name', self.gf('django.db.models.fields.CharField')(max_length=70)),
        ))
        db.send_create_signal('core', ['User'])

        # Adding model 'Story'
        db.create_table('core_story', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('authorid', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['core.User'])),
            ('title', self.gf('django.db.models.fields.CharField')(max_length=100, blank=True)),
            ('story', self.gf('django.db.models.fields.CharField')(max_length=500)),
            ('story_date', self.gf('django.db.models.fields.DateField')(blank=True)),
        ))
        db.send_create_signal('core', ['Story'])

        # Adding model 'TaggedUser'
        db.create_table('core_taggeduser', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('fbid', self.gf('django.db.models.fields.CharField')(max_length=20)),
            ('storyid', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['core.Story'])),
        ))
        db.send_create_signal('core', ['TaggedUser'])


    def backwards(self, orm):
        # Deleting model 'User'
        db.delete_table('core_user')

        # Deleting model 'Story'
        db.delete_table('core_story')

        # Deleting model 'TaggedUser'
        db.delete_table('core_taggeduser')


    models = {
        'core.story': {
            'Meta': {'object_name': 'Story'},
            'authorid': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['core.User']"}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'story': ('django.db.models.fields.CharField', [], {'max_length': '500'}),
            'story_date': ('django.db.models.fields.DateField', [], {'blank': 'True'}),
            'title': ('django.db.models.fields.CharField', [], {'max_length': '100', 'blank': 'True'})
        },
        'core.taggeduser': {
            'Meta': {'object_name': 'TaggedUser'},
            'fbid': ('django.db.models.fields.CharField', [], {'max_length': '20'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'storyid': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['core.Story']"})
        },
        'core.user': {
            'Meta': {'object_name': 'User'},
            'fbid': ('django.db.models.fields.CharField', [], {'max_length': '20'}),
            'first_name': ('django.db.models.fields.CharField', [], {'max_length': '30'}),
            'full_name': ('django.db.models.fields.CharField', [], {'max_length': '70'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'last_name': ('django.db.models.fields.CharField', [], {'max_length': '40'})
        }
    }

    complete_apps = ['core']