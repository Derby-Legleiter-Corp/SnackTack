# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'VenueType'
        db.create_table(u'web_venuetype', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('type_text', self.gf('django.db.models.fields.CharField')(max_length=16)),
        ))
        db.send_create_signal(u'web', ['VenueType'])

        # Adding model 'Event'
        db.create_table(u'web_event', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('name_text', self.gf('django.db.models.fields.CharField')(max_length=128)),
            ('description_text', self.gf('django.db.models.fields.CharField')(max_length=2048)),
            ('owner', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['auth.User'])),
            ('start_date', self.gf('django.db.models.fields.DateTimeField')()),
            ('end_date', self.gf('django.db.models.fields.DateTimeField')()),
            ('location_text', self.gf('django.db.models.fields.CharField')(max_length=64)),
        ))
        db.send_create_signal(u'web', ['Event'])

        # Adding model 'EventType'
        db.create_table(u'web_eventtype', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('venue_type', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['web.VenueType'])),
            ('event', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['web.Event'])),
        ))
        db.send_create_signal(u'web', ['EventType'])

        # Adding model 'CostType'
        db.create_table(u'web_costtype', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('type_text', self.gf('django.db.models.fields.CharField')(max_length=64)),
        ))
        db.send_create_signal(u'web', ['CostType'])

        # Adding model 'EventCost'
        db.create_table(u'web_eventcost', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('cost_type', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['web.CostType'])),
            ('event', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['web.Event'])),
            ('value', self.gf('web.fields.CurrencyField')(max_digits=10, decimal_places=2)),
        ))
        db.send_create_signal(u'web', ['EventCost'])


    def backwards(self, orm):
        # Deleting model 'VenueType'
        db.delete_table(u'web_venuetype')

        # Deleting model 'Event'
        db.delete_table(u'web_event')

        # Deleting model 'EventType'
        db.delete_table(u'web_eventtype')

        # Deleting model 'CostType'
        db.delete_table(u'web_costtype')

        # Deleting model 'EventCost'
        db.delete_table(u'web_eventcost')


    models = {
        u'auth.group': {
            'Meta': {'object_name': 'Group'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '80'}),
            'permissions': ('django.db.models.fields.related.ManyToManyField', [], {'to': u"orm['auth.Permission']", 'symmetrical': 'False', 'blank': 'True'})
        },
        u'auth.permission': {
            'Meta': {'ordering': "(u'content_type__app_label', u'content_type__model', u'codename')", 'unique_together': "((u'content_type', u'codename'),)", 'object_name': 'Permission'},
            'codename': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'content_type': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['contenttypes.ContentType']"}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '50'})
        },
        u'auth.user': {
            'Meta': {'object_name': 'User'},
            'date_joined': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now'}),
            'email': ('django.db.models.fields.EmailField', [], {'max_length': '75', 'blank': 'True'}),
            'first_name': ('django.db.models.fields.CharField', [], {'max_length': '30', 'blank': 'True'}),
            'groups': ('django.db.models.fields.related.ManyToManyField', [], {'symmetrical': 'False', 'related_name': "u'user_set'", 'blank': 'True', 'to': u"orm['auth.Group']"}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'is_active': ('django.db.models.fields.BooleanField', [], {'default': 'True'}),
            'is_staff': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'is_superuser': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'last_login': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now'}),
            'last_name': ('django.db.models.fields.CharField', [], {'max_length': '30', 'blank': 'True'}),
            'password': ('django.db.models.fields.CharField', [], {'max_length': '128'}),
            'user_permissions': ('django.db.models.fields.related.ManyToManyField', [], {'symmetrical': 'False', 'related_name': "u'user_set'", 'blank': 'True', 'to': u"orm['auth.Permission']"}),
            'username': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '30'})
        },
        u'contenttypes.contenttype': {
            'Meta': {'ordering': "('name',)", 'unique_together': "(('app_label', 'model'),)", 'object_name': 'ContentType', 'db_table': "'django_content_type'"},
            'app_label': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'model': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '100'})
        },
        u'web.costtype': {
            'Meta': {'object_name': 'CostType'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'type_text': ('django.db.models.fields.CharField', [], {'max_length': '64'})
        },
        u'web.event': {
            'Meta': {'object_name': 'Event'},
            'description_text': ('django.db.models.fields.CharField', [], {'max_length': '2048'}),
            'end_date': ('django.db.models.fields.DateTimeField', [], {}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'location_text': ('django.db.models.fields.CharField', [], {'max_length': '64'}),
            'name_text': ('django.db.models.fields.CharField', [], {'max_length': '128'}),
            'owner': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['auth.User']"}),
            'start_date': ('django.db.models.fields.DateTimeField', [], {})
        },
        u'web.eventcost': {
            'Meta': {'object_name': 'EventCost'},
            'cost_type': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['web.CostType']"}),
            'event': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['web.Event']"}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'value': ('web.fields.CurrencyField', [], {'max_digits': '10', 'decimal_places': '2'})
        },
        u'web.eventtype': {
            'Meta': {'object_name': 'EventType'},
            'event': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['web.Event']"}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'venue_type': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['web.VenueType']"})
        },
        u'web.venuetype': {
            'Meta': {'object_name': 'VenueType'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'type_text': ('django.db.models.fields.CharField', [], {'max_length': '16'})
        }
    }

    complete_apps = ['web']