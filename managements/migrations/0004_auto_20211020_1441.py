# Generated by Django 2.2 on 2021-10-20 19:41

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('managements', '0003_auto_20211020_1423'),
    ]

    operations = [
        migrations.AddField(
            model_name='appointments',
            name='created_date',
            field=models.DateTimeField(default=django.utils.timezone.now),
        ),
        migrations.AddField(
            model_name='appointments',
            name='updated_date',
            field=models.DateTimeField(auto_now_add=True, default=django.utils.timezone.now),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='appointments',
            name='time',
            field=models.CharField(blank=True, default='mm/dd/yyyy', max_length=20, null=True),
        ),
    ]
