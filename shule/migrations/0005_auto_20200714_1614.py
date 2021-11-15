# Generated by Django 3.0.8 on 2020-07-14 16:14

from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('shule', '0004_auto_20200711_1606'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='periode',
            name='level',
        ),
        migrations.AddField(
            model_name='periode',
            name='admin',
            field=models.ForeignKey(default=django.utils.timezone.now, on_delete=django.db.models.deletion.CASCADE, to='shule.Admin'),
            preserve_default=False,
        ),
        migrations.CreateModel(
            name='ProductSell',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('designation', models.TextField()),
                ('sold_amount', models.FloatField()),
                ('balance', models.FloatField()),
                ('remaing', models.IntegerField()),
                ('product', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='shule.Product')),
                ('school', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='shule.Admin')),
            ],
        ),
    ]