# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'Dicty'
        db.create_table('Smitedb_dicty', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=50)),
        ))
        db.send_create_signal('Smitedb', ['Dicty'])

        # Adding model 'KeyVal'
        db.create_table('Smitedb_keyval', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('container', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['Smitedb.Dicty'])),
            ('key', self.gf('django.db.models.fields.CharField')(max_length=240, db_index=True)),
            ('value', self.gf('django.db.models.fields.CharField')(max_length=240, db_index=True)),
        ))
        db.send_create_signal('Smitedb', ['KeyVal'])

        # Adding model 'Match'
        db.create_table('Smitedb_match', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('mapid', self.gf('django.db.models.fields.IntegerField')()),
            ('queue', self.gf('django.db.models.fields.IntegerField')()),
            ('minutes', self.gf('django.db.models.fields.IntegerField')()),
        ))
        db.send_create_signal('Smitedb', ['Match'])

        # Adding model 'Player'
        db.create_table('Smitedb_player', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=20)),
            ('created', self.gf('django.db.models.fields.DateTimeField')(null=True)),
            ('last_login', self.gf('django.db.models.fields.DateTimeField')(null=True)),
            ('wins', self.gf('django.db.models.fields.IntegerField')(null=True)),
            ('losses', self.gf('django.db.models.fields.IntegerField')(null=True)),
            ('leaves', self.gf('django.db.models.fields.IntegerField')(null=True)),
            ('rank_confidence', self.gf('django.db.models.fields.FloatField')(null=True)),
            ('rank_stat', self.gf('django.db.models.fields.FloatField')(null=True)),
            ('level', self.gf('django.db.models.fields.IntegerField')(null=True)),
            ('updated', self.gf('django.db.models.fields.DateTimeField')(auto_now=True, blank=True)),
        ))
        db.send_create_signal('Smitedb', ['Player'])

        # Adding M2M table for field matches on 'Player'
        db.create_table('Smitedb_player_matches', (
            ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True)),
            ('player', models.ForeignKey(orm['Smitedb.player'], null=False)),
            ('match', models.ForeignKey(orm['Smitedb.match'], null=False))
        ))
        db.create_unique('Smitedb_player_matches', ['player_id', 'match_id'])

        # Adding model 'Item'
        db.create_table('Smitedb_item', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=50)),
            ('description', self.gf('django.db.models.fields.CharField')(max_length=255)),
            ('secondary_description', self.gf('django.db.models.fields.CharField')(max_length=255)),
            ('item_id', self.gf('django.db.models.fields.IntegerField')()),
            ('menu_items', self.gf('django.db.models.fields.related.OneToOneField')(to=orm['Smitedb.Dicty'], unique=True)),
        ))
        db.send_create_signal('Smitedb', ['Item'])

        # Adding model 'MatchDetails'
        db.create_table('Smitedb_matchdetails', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('match', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['Smitedb.Match'])),
            ('player_name', self.gf('django.db.models.fields.CharField')(max_length=15)),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=50)),
            ('reference_name', self.gf('django.db.models.fields.CharField')(max_length=25)),
            ('win_status', self.gf('django.db.models.fields.CharField')(max_length=15)),
            ('entry_datetime', self.gf('django.db.models.fields.DateTimeField')()),
            ('damage_bot', self.gf('django.db.models.fields.IntegerField')()),
            ('damage_player', self.gf('django.db.models.fields.IntegerField')()),
            ('damage_done_magical', self.gf('django.db.models.fields.IntegerField')()),
            ('damage_done_physical', self.gf('django.db.models.fields.IntegerField')()),
            ('damage_taken', self.gf('django.db.models.fields.IntegerField')()),
            ('kills_player', self.gf('django.db.models.fields.IntegerField')()),
            ('deaths', self.gf('django.db.models.fields.SmallIntegerField')()),
            ('assists', self.gf('django.db.models.fields.SmallIntegerField')()),
            ('kills_bot', self.gf('django.db.models.fields.SmallIntegerField')()),
            ('final_match_level', self.gf('django.db.models.fields.SmallIntegerField')()),
            ('gold_earned', self.gf('django.db.models.fields.IntegerField')()),
            ('gold_per_minute', self.gf('django.db.models.fields.IntegerField')()),
            ('item_active_1', self.gf('django.db.models.fields.related.ForeignKey')(related_name='active1', to=orm['Smitedb.Item'])),
            ('item_active_2', self.gf('django.db.models.fields.related.ForeignKey')(related_name='active2', to=orm['Smitedb.Item'])),
            ('item_active_3', self.gf('django.db.models.fields.related.ForeignKey')(related_name='active3', to=orm['Smitedb.Item'])),
            ('item_purch_1', self.gf('django.db.models.fields.related.ForeignKey')(related_name='purch1', to=orm['Smitedb.Item'])),
            ('item_purch_2', self.gf('django.db.models.fields.related.ForeignKey')(related_name='purch2', to=orm['Smitedb.Item'])),
            ('item_purch_3', self.gf('django.db.models.fields.related.ForeignKey')(related_name='purch3', to=orm['Smitedb.Item'])),
            ('item_purch_4', self.gf('django.db.models.fields.related.ForeignKey')(related_name='purch4', to=orm['Smitedb.Item'])),
            ('item_purch_5', self.gf('django.db.models.fields.related.ForeignKey')(related_name='purch5', to=orm['Smitedb.Item'])),
            ('item_purch_6', self.gf('django.db.models.fields.related.ForeignKey')(related_name='purch6', to=orm['Smitedb.Item'])),
        ))
        db.send_create_signal('Smitedb', ['MatchDetails'])


    def backwards(self, orm):
        # Deleting model 'Dicty'
        db.delete_table('Smitedb_dicty')

        # Deleting model 'KeyVal'
        db.delete_table('Smitedb_keyval')

        # Deleting model 'Match'
        db.delete_table('Smitedb_match')

        # Deleting model 'Player'
        db.delete_table('Smitedb_player')

        # Removing M2M table for field matches on 'Player'
        db.delete_table('Smitedb_player_matches')

        # Deleting model 'Item'
        db.delete_table('Smitedb_item')

        # Deleting model 'MatchDetails'
        db.delete_table('Smitedb_matchdetails')


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
        'Smitedb.player': {
            'Meta': {'object_name': 'Player'},
            'created': ('django.db.models.fields.DateTimeField', [], {'null': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'last_login': ('django.db.models.fields.DateTimeField', [], {'null': 'True'}),
            'leaves': ('django.db.models.fields.IntegerField', [], {'null': 'True'}),
            'level': ('django.db.models.fields.IntegerField', [], {'null': 'True'}),
            'losses': ('django.db.models.fields.IntegerField', [], {'null': 'True'}),
            'matches': ('django.db.models.fields.related.ManyToManyField', [], {'to': "orm['Smitedb.Match']", 'symmetrical': 'False'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '20'}),
            'rank_confidence': ('django.db.models.fields.FloatField', [], {'null': 'True'}),
            'rank_stat': ('django.db.models.fields.FloatField', [], {'null': 'True'}),
            'updated': ('django.db.models.fields.DateTimeField', [], {'auto_now': 'True', 'blank': 'True'}),
            'wins': ('django.db.models.fields.IntegerField', [], {'null': 'True'})
        }
    }

    complete_apps = ['Smitedb']