# Generated by Django 2.2.3 on 2019-09-16 12:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('fireapp', '0006_order'),
    ]

    operations = [
        migrations.AddField(
            model_name='food',
            name='FoodImage',
            field=models.ImageField(default='', upload_to='media'),
        ),
    ]
