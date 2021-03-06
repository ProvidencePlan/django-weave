# encoding: utf-8
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models

class Migration(SchemaMigration):

    def forwards(self, orm):
        
        # Adding model 'Category'
        db.create_table('weave_category', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('parent', self.gf('django.db.models.fields.related.ForeignKey')(blank=True, related_name='children', null=True, to=orm['weave.Category'])),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=300)),
        ))
        db.send_create_signal('weave', ['Category'])

        # Adding model 'KeyUnitType'
        db.create_table('weave_keyunittype', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('name', self.gf('django.db.models.fields.CharField')(unique=True, max_length=100)),
        ))
        db.send_create_signal('weave', ['KeyUnitType'])

        # Adding model 'DataTable'
        db.create_table('weave_datatable', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=100)),
            ('key_unit_type', self.gf('django.db.models.fields.CharField')(max_length=100)),
        ))
        db.send_create_signal('weave', ['DataTable'])

        # Adding model 'AttributeColumn'
        db.create_table('weave_attributecolumn', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('content_type', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['contenttypes.ContentType'], null=True)),
            ('object_id', self.gf('django.db.models.fields.PositiveIntegerField')(null=True)),
            ('data_table', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['weave.DataTable'])),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=100)),
            ('display_name', self.gf('django.db.models.fields.CharField')(max_length=255)),
            ('category', self.gf('django.db.models.fields.related.ForeignKey')(blank=True, related_name='indicators', null=True, to=orm['weave.Category'])),
            ('key_unit_type', self.gf('django.db.models.fields.CharField')(max_length=100)),
            ('data_type', self.gf('django.db.models.fields.CharField')(max_length=6)),
            ('data_with_keys_query', self.gf('django.db.models.fields.TextField')()),
            ('min', self.gf('django.db.models.fields.IntegerField')(null=True, blank=True)),
            ('max', self.gf('django.db.models.fields.IntegerField')(null=True, blank=True)),
            ('year', self.gf('django.db.models.fields.CharField')(max_length=50, null=True, blank=True)),
        ))
        db.send_create_signal('weave', ['AttributeColumn'])

        # Adding unique constraint on 'AttributeColumn', fields ['name', 'key_unit_type', 'year']
        db.create_unique('weave_attributecolumn', ['name', 'key_unit_type', 'year'])

        # Adding model 'DataFilter'
        db.create_table('weave_datafilter', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('file', self.gf('django.db.models.fields.files.FileField')(max_length=100, blank=True)),
            ('name', self.gf('django.db.models.fields.CharField')(unique=True, max_length=100)),
            ('display', self.gf('django.db.models.fields.BooleanField')(default=True, blank=True)),
            ('key_unit_type', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['weave.KeyUnitType'], null=True)),
        ))
        db.send_create_signal('weave', ['DataFilter'])

        # Adding model 'DataFilterKey'
        db.create_table('weave_datafilterkey', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('data_filter', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['weave.DataFilter'])),
            ('key_value', self.gf('django.db.models.fields.CharField')(max_length=100)),
        ))
        db.send_create_signal('weave', ['DataFilterKey'])

        # Adding model 'ClientConfiguration'
        db.create_table('weave_clientconfiguration', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('name', self.gf('django.db.models.fields.CharField')(unique=True, max_length=100)),
            ('slug', self.gf('django.db.models.fields.SlugField')(unique=True, max_length=50, db_index=True)),
            ('file', self.gf('django.db.models.fields.files.FileField')(max_length=100, null=True, blank=True)),
        ))
        db.send_create_signal('weave', ['ClientConfiguration'])

        # Adding model 'GeometryCollection'
        db.create_table('weave_geometrycollection', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=100)),
            ('key_unit_type', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['weave.KeyUnitType'], null=True)),
        ))
        db.send_create_signal('weave', ['GeometryCollection'])


    def backwards(self, orm):
        
        # Deleting model 'Category'
        db.delete_table('weave_category')

        # Deleting model 'KeyUnitType'
        db.delete_table('weave_keyunittype')

        # Deleting model 'DataTable'
        db.delete_table('weave_datatable')

        # Deleting model 'AttributeColumn'
        db.delete_table('weave_attributecolumn')

        # Removing unique constraint on 'AttributeColumn', fields ['name', 'key_unit_type', 'year']
        db.delete_unique('weave_attributecolumn', ['name', 'key_unit_type', 'year'])

        # Deleting model 'DataFilter'
        db.delete_table('weave_datafilter')

        # Deleting model 'DataFilterKey'
        db.delete_table('weave_datafilterkey')

        # Deleting model 'ClientConfiguration'
        db.delete_table('weave_clientconfiguration')

        # Deleting model 'GeometryCollection'
        db.delete_table('weave_geometrycollection')


    models = {
        'contenttypes.contenttype': {
            'Meta': {'unique_together': "(('app_label', 'model'),)", 'object_name': 'ContentType', 'db_table': "'django_content_type'"},
            'app_label': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'model': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '100'})
        },
        'weave.attributecolumn': {
            'Meta': {'unique_together': "(('name', 'key_unit_type', 'year'),)", 'object_name': 'AttributeColumn'},
            'category': ('django.db.models.fields.related.ForeignKey', [], {'blank': 'True', 'related_name': "'indicators'", 'null': 'True', 'to': "orm['weave.Category']"}),
            'content_type': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['contenttypes.ContentType']", 'null': 'True'}),
            'data_table': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['weave.DataTable']"}),
            'data_type': ('django.db.models.fields.CharField', [], {'max_length': '6'}),
            'data_with_keys_query': ('django.db.models.fields.TextField', [], {}),
            'display_name': ('django.db.models.fields.CharField', [], {'max_length': '255'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'key_unit_type': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'max': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'min': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'object_id': ('django.db.models.fields.PositiveIntegerField', [], {'null': 'True'}),
            'year': ('django.db.models.fields.CharField', [], {'max_length': '50', 'null': 'True', 'blank': 'True'})
        },
        'weave.category': {
            'Meta': {'object_name': 'Category'},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '300'}),
            'parent': ('django.db.models.fields.related.ForeignKey', [], {'blank': 'True', 'related_name': "'children'", 'null': 'True', 'to': "orm['weave.Category']"})
        },
        'weave.clientconfiguration': {
            'Meta': {'object_name': 'ClientConfiguration'},
            'file': ('django.db.models.fields.files.FileField', [], {'max_length': '100', 'null': 'True', 'blank': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '100'}),
            'slug': ('django.db.models.fields.SlugField', [], {'unique': 'True', 'max_length': '50', 'db_index': 'True'})
        },
        'weave.datafilter': {
            'Meta': {'object_name': 'DataFilter'},
            'display': ('django.db.models.fields.BooleanField', [], {'default': 'True', 'blank': 'True'}),
            'file': ('django.db.models.fields.files.FileField', [], {'max_length': '100', 'blank': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'key_unit_type': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['weave.KeyUnitType']", 'null': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '100'})
        },
        'weave.datafilterkey': {
            'Meta': {'object_name': 'DataFilterKey'},
            'data_filter': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['weave.DataFilter']"}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'key_value': ('django.db.models.fields.CharField', [], {'max_length': '100'})
        },
        'weave.datatable': {
            'Meta': {'object_name': 'DataTable'},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'key_unit_type': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '100'})
        },
        'weave.geometrycollection': {
            'Meta': {'object_name': 'GeometryCollection'},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'key_unit_type': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['weave.KeyUnitType']", 'null': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '100'})
        },
        'weave.keyunittype': {
            'Meta': {'object_name': 'KeyUnitType'},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '100'})
        }
    }

    complete_apps = ['weave']
