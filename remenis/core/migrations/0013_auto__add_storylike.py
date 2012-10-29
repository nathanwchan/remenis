# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'StoryLike'
        db.create_table('core_storylike', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('storyid', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['core.Story'])),
            ('authorid', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['core.User'])),
        ))
        db.send_create_signal('core', ['StoryLike'])


    def backwards(self, orm):
        # Deleting model 'StoryLike'
        db.delete_table('core_storylike')


    models = {
        'core.betaemail': {
            'Meta': {'object_name': 'BetaEmail'},
            'email': ('django.db.models.fields.EmailField', [], {'max_length': '75', 'null': 'True', 'blank': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'submit_date': ('django.db.models.fields.DateTimeField', [], {'null': 'True', 'blank': 'True'})
        },
        'core.story': {
            'Meta': {'object_name': 'Story'},
            'authorid': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['core.User']"}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'is_private': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'post_date': ('django.db.models.fields.DateTimeField', [], {'null': 'True', 'blank': 'True'}),
            'story': ('django.db.models.fields.TextField', [], {}),
            'story_date_day': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'story_date_month': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'story_date_year': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'title': ('django.db.models.fields.CharField', [], {'max_length': '100', 'blank': 'True'})
        },
        'core.storycomment': {
            'Meta': {'object_name': 'StoryComment'},
            'authorid': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['core.User']", 'null': 'True', 'blank': 'True'}),
            'comment': ('django.db.models.fields.TextField', [], {}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'post_date': ('django.db.models.fields.DateTimeField', [], {'null': 'True', 'blank': 'True'}),
            'storyid': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['core.Story']"})
        },
        'core.storylike': {
            'Meta': {'object_name': 'StoryLike'},
            'authorid': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['core.User']"}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'storyid': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['core.Story']"})
        },
        'core.taggeduser': {
            'Meta': {'object_name': 'TaggedUser'},
            'fbid': ('django.db.models.fields.CharField', [], {'max_length': '20'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'storyid': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['core.Story']"})
        },
        'core.user': {
            'Meta': {'object_name': 'User'},
            'email': ('django.db.models.fields.EmailField', [], {'max_length': '75', 'null': 'True', 'blank': 'True'}),
            'fbid': ('django.db.models.fields.CharField', [], {'max_length': '20'}),
            'first_name': ('django.db.models.fields.CharField', [], {'max_length': '50', 'blank': 'True'}),
            'full_name': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'is_registered': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'last_name': ('django.db.models.fields.CharField', [], {'max_length': '50', 'blank': 'True'})
        }
    }

    complete_apps = ['core']