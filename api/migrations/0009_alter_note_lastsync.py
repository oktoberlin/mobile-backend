# Generated by Django 3.2.11 on 2022-03-04 16:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0008_alter_note_lastsync'),
    ]

    operations = [
        migrations.AlterField(
            model_name='note',
            name='lastSync',
            field=models.CharField(blank=True, max_length=128, null=True),
        ),
    ]