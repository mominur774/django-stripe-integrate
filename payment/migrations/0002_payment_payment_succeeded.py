# Generated by Django 3.1.7 on 2022-07-05 17:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('payment', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='payment',
            name='payment_succeeded',
            field=models.BooleanField(default=False),
        ),
    ]
