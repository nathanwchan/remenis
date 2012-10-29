# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Deleting field 'Story.story_date'
        db.delete_column('core_story', 'story_date')

        # Adding field 'Story.story_date_year'
        db.add_column('core_story', 'story_date_year',
                      self.gf('django.db.models.fields.IntegerField')(null=True, blank=True),
                      keep_default=False)

        # Adding field 'Story.story_date_month'
        db.add_column('core_story', 'story_date_month',
                      self.gf('django.db.models.fields.IntegerField')(null=True, blank=True),
                      keep_default=False)

        # Adding field 'Story.story_date_day'
        db.add_column('core_story', 'story_date_day',
                      self.gf('django.db.models.fields.IntegerField')(null=True, blank=True),
                      keep_default=False)


    def backwards(self, orm):
        # Adding field 'Story.story_date'
        db.add_column('core_story', 'story_date',
                      self.gf('django.db.models.fields.DateField')(default='', blank=True),
                      keep_default=False)

        # Deleting field 'Story.story_date_year'
        db.delete_column('core_story', 'story_date_year')

        # Deleting field 'Story.story_date_month'
        db.delete_column('core_story', 'story_date_month')

        # Deleting field 'Story.story_date_day'
        db.delete_column('core_story', 'story_date_day')


    models = {
        'core.story': {
            'Meta': {'object_name': 'Story'},
            'authorid': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['core.User']"}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'post_date': ('django.db.models.fields.DateTimeField', [], {'null': 'True', 'blank': 'True'}),
            'story': ('django.db.models.fields.CharField', [], {'max_length': '500'}),
            'story_date_day': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'story_date_month': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'story_date_year': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'title': ('django.db.models.fields.CharField', [], {'max_length': '100', 'blank': 'True'})
        },
        'core.storycomment': {
            'Meta': {'object_name': 'StoryComment'},
            'comment': ('django.db.models.fields.CharField', [], {'max_length': '200'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'post_date': ('django.db.models.fields.DateTimeField', [], {'null': 'True', 'blank': 'True'}),
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
            'email': ('django.db.models.fields.EmailField', [], {'max_length': '75', 'blank': 'True'}),
            'fbid': ('django.db.models.fields.CharField', [], {'max_length': '20'}),
            'first_name': ('django.db.models.fields.CharField', [], {'max_length': '30'}),
            'full_name': ('django.db.models.fields.CharField', [], {'max_length': '70'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'last_name': ('django.db.models.fields.CharField', [], {'max_length': '40'})
        }
    }

    complete_apps = ['core']