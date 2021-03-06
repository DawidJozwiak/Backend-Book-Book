# Generated by Django 3.2.3 on 2021-05-29 21:56

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('api_basics', '0002_auto_20210529_2322'),
    ]

    operations = [
        migrations.AddField(
            model_name='shelves',
            name='user',
            field=models.OneToOneField(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='shelf', to='api_basics.users'),
        ),
        migrations.AlterField(
            model_name='shelves',
            name='users_fk',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='api_basics.users'),
        ),
    ]
