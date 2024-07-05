# Generated by Django 5.0.6 on 2024-06-06 20:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Musician', '0003_musician_instrument_type'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='musician',
            name='phone_number',
        ),
        migrations.AddField(
            model_name='musician',
            name='phonenumber_field',
            field=models.CharField(default=1, max_length=11),
            preserve_default=False,
        ),
    ]
