# Generated by Django 3.2.3 on 2021-05-29 22:54

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('api_basics', '0006_auto_20210530_0054'),
    ]

    operations = [
        migrations.AlterField(
            model_name='shelves',
            name='users_fk',
            field=models.ForeignKey(blank=True, default=1, null=True, on_delete=django.db.models.deletion.CASCADE, to='api_basics.users'),
        ),
    ]
