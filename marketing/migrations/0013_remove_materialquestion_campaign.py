# Generated by Django 4.2.6 on 2023-10-16 19:31

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('marketing', '0012_materialquestion_campaign'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='materialquestion',
            name='campaign',
        ),
    ]
