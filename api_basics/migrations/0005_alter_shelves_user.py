# Generated by Django 3.2.3 on 2021-05-29 22:53

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('api_basics', '0004_auto_20210530_0049'),
    ]

    operations = [
        migrations.AlterField(
            model_name='shelves',
            name='user',
            field=models.OneToOneField(blank=True, default=1, on_delete=django.db.models.deletion.CASCADE, related_name='shelf', to='api_basics.users'),
        ),
    ]
