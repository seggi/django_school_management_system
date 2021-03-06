# Generated by Django 3.0.8 on 2020-07-11 16:00

from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('shule', '0002_auto_20200708_1635'),
    ]

    operations = [
        migrations.RenameField(
            model_name='faculty',
            old_name='shulde_admin',
            new_name='classe',
        ),
        migrations.RenameField(
            model_name='periode',
            old_name='shulde_admin',
            new_name='level',
        ),
        migrations.RemoveField(
            model_name='classe',
            name='shulde_admin',
        ),
        migrations.AddField(
            model_name='classe',
            name='level',
            field=models.OneToOneField(default=django.utils.timezone.now, on_delete=django.db.models.deletion.CASCADE, to='shule.Level'),
            preserve_default=False,
        ),
    ]
