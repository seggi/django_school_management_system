# Generated by Django 3.0.8 on 2020-07-14 16:46

from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('shule', '0005_auto_20200714_1614'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='productsell',
            name='school',
        ),
        migrations.AddField(
            model_name='productsell',
            name='secretary',
            field=models.ForeignKey(default=django.utils.timezone.now, on_delete=django.db.models.deletion.CASCADE, to='shule.Staff'),
            preserve_default=False,
        ),
    ]
