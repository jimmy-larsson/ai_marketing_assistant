# Generated by Django 4.2.6 on 2023-10-16 17:14

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('marketing', '0007_alter_campaign_cron_schedule'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='campaign',
            name='cron_schedule',
        ),
    ]
