# Generated by Django 3.2.5 on 2021-08-01 13:36

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('dataLogging', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='data_input_table',
            name='kks_description',
            field=models.ForeignKey(blank=True, db_column='kks_description', null=True, on_delete=django.db.models.deletion.CASCADE, related_name='kks_description', to='dataLogging.kks_description'),
        ),
    ]
