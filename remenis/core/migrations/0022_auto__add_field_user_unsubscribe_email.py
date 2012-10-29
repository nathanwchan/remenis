# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding field 'User.unsubscribe_email'
        db.add_column('core_user', 'unsubscribe_email',
                      self.gf('django.db.models.fields.BooleanField')(default=False),
                      keep_default=False)


    def backwards(self, orm):
        # Deleting field 'User.unsubscribe_email'
        db.delete_column('core_user', 'unsubscribe_email')


    models = {
        'core.betaemail': {
            'Meta': {'object_name': 'BetaEmail'},
            'email': ('django.db.models.fields.EmailField', [], {'max_length': '75', 'null': 'True', 'blank': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'submit_date': ('django.db.models.fields.DateTimeField', [], {'null': 'True', 'blank': 'True'})
        },
        'core.notification': {
            'Meta': {'object_name': 'Notification'},
            'count': ('django.db.models.fields.IntegerField', [], {'default': '0'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'storyid': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['core.Story']"}),
            'type': ('django.db.models.fields.CharField', [], {'max_length': '20'}),
            'userid': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['core.User']"})
        },
        'core.pageview': {
            'Meta': {'object_name': 'PageView'},
            'count': ('django.db.models.fields.IntegerField', [], {'default': '0'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'page': ('django.db.models.fields.CharField', [], {'max_length': '40'})
        },
        'core.story': {
            'Meta': {'object_name': 'Story'},
            'authorid': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['core.User']"}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'is_private': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'page_views': ('django.db.models.fields.IntegerField', [], {'default': '0'}),
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
        'core.storyoftheday': {
            'Meta': {'object_name': 'StoryOfTheDay'},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'text': ('django.db.models.fields.TextField', [], {})
        },
        'core.taggeduser': {
            'Meta': {'object_name': 'TaggedUser'},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'storyid': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['core.Story']"}),
            'taggeduserid': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['core.User']", 'null': 'True', 'blank': 'True'})
        },
        'core.user': {
            'Meta': {'object_name': 'User'},
            'email': ('django.db.models.fields.EmailField', [], {'max_length': '75', 'null': 'True', 'blank': 'True'}),
            'fbid': ('django.db.models.fields.CharField', [], {'max_length': '20'}),
            'first_name': ('django.db.models.fields.CharField', [], {'max_length': '50', 'blank': 'True'}),
            'full_name': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'is_registered': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'last_date': ('django.db.models.fields.DateTimeField', [], {'null': 'True', 'blank': 'True'}),
            'last_name': ('django.db.models.fields.CharField', [], {'max_length': '50', 'blank': 'True'}),
            'page_views': ('django.db.models.fields.IntegerField', [], {'default': '0'}),
            'unsubscribe_email': ('django.db.models.fields.BooleanField', [], {'default': 'False'})
        }
    }

    complete_apps = ['core']