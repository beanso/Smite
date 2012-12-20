# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'MatchSummary'
        db.create_table('Smitedb_matchsummary', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('active_1', self.gf('django.db.models.fields.related.ForeignKey')(related_name='active_1', null=True, to=orm['Smitedb.Item'])),
            ('active_2', self.gf('django.db.models.fields.related.ForeignKey')(related_name='active_2', null=True, to=orm['Smitedb.Item'])),
            ('active_3', self.gf('django.db.models.fields.related.ForeignKey')(related_name='active_3', null=True, to=orm['Smitedb.Item'])),
            ('item_1', self.gf('django.db.models.fields.related.ForeignKey')(related_name='item_1', null=True, to=orm['Smitedb.Item'])),
            ('item_2', self.gf('django.db.models.fields.related.ForeignKey')(related_name='item_2', null=True, to=orm['Smitedb.Item'])),
            ('item_3', self.gf('django.db.models.fields.related.ForeignKey')(related_name='item_3', null=True, to=orm['Smitedb.Item'])),
            ('item_4', self.gf('django.db.models.fields.related.ForeignKey')(related_name='item_4', null=True, to=orm['Smitedb.Item'])),
            ('item_5', self.gf('django.db.models.fields.related.ForeignKey')(related_name='item_5', null=True, to=orm['Smitedb.Item'])),
            ('item_6', self.gf('django.db.models.fields.related.ForeignKey')(related_name='item_6', null=True, to=orm['Smitedb.Item'])),
            ('kills', self.gf('django.db.models.fields.IntegerField')()),
            ('deaths', self.gf('django.db.models.fields.IntegerField')()),
            ('assists', self.gf('django.db.models.fields.IntegerField')()),
            ('gold', self.gf('django.db.models.fields.IntegerField')()),
            ('level', self.gf('django.db.models.fields.IntegerField')()),
            ('match', self.gf('django.db.models.fields.IntegerField')()),
            ('match_time', self.gf('django.db.models.fields.DateTimeField')()),
            ('minutes', self.gf('django.db.models.fields.IntegerField')()),
            ('queue', self.gf('django.db.models.fields.CharField')(max_length=25)),
            ('win_status', self.gf('django.db.models.fields.CharField')(max_length=5)),
        ))
        db.send_create_signal('Smitedb', ['MatchSummary'])


    def backwards(self, orm):
        # Deleting model 'MatchSummary'
        db.delete_table('Smitedb_matchsummary')


    models = {
        'Smitedb.dicty': {
            'Meta': {'object_name': 'Dicty'},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '50'})
        },
        'Smitedb.item': {
            'Meta': {'object_name': 'Item'},
            'description': ('django.db.models.fields.CharField', [], {'max_length': '255'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'item_id': ('django.db.models.fields.IntegerField', [], {}),
            'menu_items': ('django.db.models.fields.related.OneToOneField', [], {'to': "orm['Smitedb.Dicty']", 'unique': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '50'}),
            'secondary_description': ('django.db.models.fields.CharField', [], {'max_length': '255'})
        },
        'Smitedb.keyval': {
            'Meta': {'object_name': 'KeyVal'},
            'container': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['Smitedb.Dicty']"}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'key': ('django.db.models.fields.CharField', [], {'max_length': '240', 'db_index': 'True'}),
            'value': ('django.db.models.fields.CharField', [], {'max_length': '240', 'db_index': 'True'})
        },
        'Smitedb.match': {
            'Meta': {'object_name': 'Match'},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'mapid': ('django.db.models.fields.IntegerField', [], {}),
            'minutes': ('django.db.models.fields.IntegerField', [], {}),
            'queue': ('django.db.models.fields.IntegerField', [], {})
        },
        'Smitedb.matchdetails': {
            'Meta': {'object_name': 'MatchDetails'},
            'assists': ('django.db.models.fields.SmallIntegerField', [], {}),
            'damage_bot': ('django.db.models.fields.IntegerField', [], {}),
            'damage_done_magical': ('django.db.models.fields.IntegerField', [], {}),
            'damage_done_physical': ('django.db.models.fields.IntegerField', [], {}),
            'damage_player': ('django.db.models.fields.IntegerField', [], {}),
            'damage_taken': ('django.db.models.fields.IntegerField', [], {}),
            'deaths': ('django.db.models.fields.SmallIntegerField', [], {}),
            'entry_datetime': ('django.db.models.fields.DateTimeField', [], {}),
            'final_match_level': ('django.db.models.fields.SmallIntegerField', [], {}),
            'gold_earned': ('django.db.models.fields.IntegerField', [], {}),
            'gold_per_minute': ('django.db.models.fields.IntegerField', [], {}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'item_active_1': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'active1'", 'to': "orm['Smitedb.Item']"}),
            'item_active_2': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'active2'", 'to': "orm['Smitedb.Item']"}),
            'item_active_3': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'active3'", 'to': "orm['Smitedb.Item']"}),
            'item_purch_1': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'purch1'", 'to': "orm['Smitedb.Item']"}),
            'item_purch_2': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'purch2'", 'to': "orm['Smitedb.Item']"}),
            'item_purch_3': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'purch3'", 'to': "orm['Smitedb.Item']"}),
            'item_purch_4': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'purch4'", 'to': "orm['Smitedb.Item']"}),
            'item_purch_5': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'purch5'", 'to': "orm['Smitedb.Item']"}),
            'item_purch_6': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'purch6'", 'to': "orm['Smitedb.Item']"}),
            'kills_bot': ('django.db.models.fields.SmallIntegerField', [], {}),
            'kills_player': ('django.db.models.fields.IntegerField', [], {}),
            'match': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['Smitedb.Match']"}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '50'}),
            'player_name': ('django.db.models.fields.CharField', [], {'max_length': '15'}),
            'reference_name': ('django.db.models.fields.CharField', [], {'max_length': '25'}),
            'win_status': ('django.db.models.fields.CharField', [], {'max_length': '15'})
        },
        'Smitedb.matchsummary': {
            'Meta': {'object_name': 'MatchSummary'},
            'active_1': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'active_1'", 'null': 'True', 'to': "orm['Smitedb.Item']"}),
            'active_2': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'active_2'", 'null': 'True', 'to': "orm['Smitedb.Item']"}),
            'active_3': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'active_3'", 'null': 'True', 'to': "orm['Smitedb.Item']"}),
            'assists': ('django.db.models.fields.IntegerField', [], {}),
            'deaths': ('django.db.models.fields.IntegerField', [], {}),
            'gold': ('django.db.models.fields.IntegerField', [], {}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'item_1': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'item_1'", 'null': 'True', 'to': "orm['Smitedb.Item']"}),
            'item_2': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'item_2'", 'null': 'True', 'to': "orm['Smitedb.Item']"}),
            'item_3': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'item_3'", 'null': 'True', 'to': "orm['Smitedb.Item']"}),
            'item_4': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'item_4'", 'null': 'True', 'to': "orm['Smitedb.Item']"}),
            'item_5': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'item_5'", 'null': 'True', 'to': "orm['Smitedb.Item']"}),
            'item_6': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'item_6'", 'null': 'True', 'to': "orm['Smitedb.Item']"}),
            'kills': ('django.db.models.fields.IntegerField', [], {}),
            'level': ('django.db.models.fields.IntegerField', [], {}),
            'match': ('django.db.models.fields.IntegerField', [], {}),
            'match_time': ('django.db.models.fields.DateTimeField', [], {}),
            'minutes': ('django.db.models.fields.IntegerField', [], {}),
            'queue': ('django.db.models.fields.CharField', [], {'max_length': '25'}),
            'win_status': ('django.db.models.fields.CharField', [], {'max_length': '5'})
        },
        'Smitedb.player': {
            'Meta': {'object_name': 'Player'},
            'created': ('django.db.models.fields.DateTimeField', [], {'null': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'last_login': ('django.db.models.fields.DateTimeField', [], {'null': 'True'}),
            'leaves': ('django.db.models.fields.IntegerField', [], {'null': 'True'}),
            'level': ('django.db.models.fields.IntegerField', [], {'null': 'True'}),
            'losses': ('django.db.models.fields.IntegerField', [], {'null': 'True'}),
            'matches': ('django.db.models.fields.related.ManyToManyField', [], {'to': "orm['Smitedb.MatchSummary']", 'symmetrical': 'False'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '20'}),
            'rank_confidence': ('django.db.models.fields.FloatField', [], {'null': 'True'}),
            'rank_stat': ('django.db.models.fields.FloatField', [], {'null': 'True'}),
            'updated': ('django.db.models.fields.DateTimeField', [], {'auto_now': 'True', 'blank': 'True'}),
            'wins': ('django.db.models.fields.IntegerField', [], {'null': 'True'})
        }
    }

    complete_apps = ['Smitedb']