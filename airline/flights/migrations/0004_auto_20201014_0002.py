# Generated by Django 3.1.2 on 2020-10-14 00:02

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('flights', '0003_passenger'),
    ]

    operations = [
        migrations.RenameField(
            model_name='passenger',
            old_name='flight',
            new_name='flights',
        ),
    ]
